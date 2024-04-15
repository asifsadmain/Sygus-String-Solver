import openai
from datetime import datetime
import logging
import os
from copy import deepcopy
from utils import *
from sygus_parser import StrParser
from itertools import product
import sys
import re
from sygus_string_dsl import *
from gpt_parser import parse_string, flatten_list, iterate_lists
from feedback import get_dsl_match_not_found
from iterate import *


PATH_TO_STR_BENCHMARKS = "../sygus_string_tasks/"
config_directory = "../config/"
logs_directory = "../logs/"

def get_response_from_api(user_message):
    openai.api_key = "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"

    system_message = f"""
    Your task is to write a python function named 'manipulate' that takes the given arguments and returns the expected outputs inside a <python></python> tag.
    """

    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
    temperature=0.5,
    # max_tokens=256
    )

    return response['choices'][0]['message']['content']

def construct_user_message(input_output_examples):
    io_examples = ""

    for i in range(len(input_output_examples)):
        formatted_pairs = [f'{key}: "{value}"' for key, value in input_output_examples[i].items()]
        io_examples += str((i+1)) + ". " + ', '.join(formatted_pairs) + "\n    "

    constraints = f"""
    I am providing {len(input_output_examples)} examples. Each example contains the input to the string and/or integer argument(s) and an output (out). Here are the examples:

    {io_examples}
    """

    user_message = constraints

    return user_message


def synthesize(last_gpt_program, error_message, latest_io_log):
    log_filename = logs_directory + "/gpt.log"
    slurm_task_id = sys.argv[1]
    TaskId = int(slurm_task_id) - 1
    logging.basicConfig(filename=log_filename,
                            filemode='a',
                            format='%(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)
    logging.info("[Task: " + str(TaskId) + "]")

    with open(config_directory+"bustle_benchmarks.txt") as f:
        benchmarks = f.read().splitlines()

        benchmark = None
        filename = benchmarks[TaskId]
        print("filename =", filename)

        benchmark = filename

        specification_parser = StrParser(benchmark)
        specifications = specification_parser.parse()
        logging.info("\n")

        args = specifications[0] + specifications[2]      
        input_output_examples = specifications[4]
        print(input_output_examples)

    user_message = construct_user_message(input_output_examples)

    if (error_message):
        user_message += f"""
        The last program obtained from you was ```{last_gpt_program}``` which threw the following error message:
        ```
        {error_message}
        ```
        Please update this program fixing the error(s) and make it functional to obtain the expected output.
        """
    elif (latest_io_log):
        user_message += f"""
        The last program obtained from you was: ```{last_gpt_program}```.
        The output and the expected output do not match. \
        They look like the following:
        ```
        {latest_io_log}
        ```
        Please update this program and make it functional to obtain the expected output.
        """

    print("=================Request================")
    print(user_message)
    print()
    response = get_response_from_api(user_message)
    print("=================Response===============")
    print(response)
    print()

    # Define a regular expression pattern to match text inside <program></program> tags
    pattern = r'<python>(.*?)<\/python>'

    # Use re.findall to find all matches of the pattern in the input string
    matches = re.findall(pattern, response, re.DOTALL)

    # Print the extracted text
    if (matches):
        program = matches[0].strip()
    else:
        pattern = r'```python(.*?)```'
        matches = re.findall(pattern, response, re.DOTALL)
        program = matches[0].strip()

    logging.info("Program: " + program + "\n")
    # program = program.replace('\n', '').replace("'", '"')
    # program_list = parse_string(program)

    # is_success = True
    # # print(program_list)
    # # print()
    # logging.info("Expected Output\t\t\tGPT Output")
    # logging.info("-----------------------------------------------------")
    # io_log = ""
    # for example in input_output_examples:
    #     example_program_list = deepcopy(program_list)
    #     for var in string_variables + integer_variables:
    #         replace_placeholders(example_program_list, var, example[var])
    #     # print("======================")
    #     # print(example_program_list)
    #     # print("======================")
    #     ast = get_ast(example_program_list)
    #     ast = evaluate(ast)
    #     io_log += example['out'] + "\t\t\t" + ast.data + "\n"
    #     if (example['out'] != ast.data):
    #         is_success = False
    # logging.info(io_log)

    return program, args, input_output_examples

def validate(program, args, input_output_examples):
    is_success = True
    # print(program_list)
    # print()
    logging.info("Expected Output\t\t\tGPT Output")
    logging.info("-----------------------------------------------------")
    io_log = ""
    expected_vs_obtained = ""
    
    for example in input_output_examples:
        driver_code = "\noutput = manipulate("
        for i in range(len(args)):
            driver_code += '"' + example[args[i]] + '"'
            if (i != (len(args) - 1)):
                driver_code += ", "
        driver_code += ")"

        source_code = program + driver_code
        print(source_code)

        namespace = {}
        exec(source_code, namespace)
        gpt_output = namespace['output']
            
        io_log += example['out'] + "\t\t\t" + gpt_output + "\n"
        print(gpt_output)

        if ((example['out']) != gpt_output):
            # expected_vs_obtained += "Expected output is " + example['out'] + ", but obtained " + ast.data + "\n"
            expected_vs_obtained += f"""For argument(s) {[example[arg] for arg in args]}, expected output is "{example['out']}", but obtained "{gpt_output}"\n"""

        if (example['out'] != gpt_output):
            is_success = False
    logging.info(io_log)

    return is_success, expected_vs_obtained


# slurm_task_id = sys.argv[1]
# TaskId = int(slurm_task_id) - 1

# with open(config_directory+"bustle_benchmarks.txt") as f:
#     benchmarks = f.read().splitlines()
#     benchmark = None
#     filename = benchmarks[TaskId]
#     print("filename =", filename)

#     benchmark = filename

#     specification_parser = StrParser(benchmark)
#     specifications = specification_parser.parse()

#     user_message = construct_user_message(specifications[4])
    # response = get_response_from_api(user_message)

    # print(user_message)
    # print(response)

found = False
last_program = None
latest_io_log = None
error_message = None
count = 0

# program, args, input_output_examples = synthesize(last_program, error_message, latest_io_log)
# found, io_log = validate(program, args, input_output_examples)

while(not found):
    if (count == 10):
        break

    try:
        program, args, input_output_examples = synthesize(last_program, error_message, latest_io_log)
    except:
        continue

    try:
        found, io_log = validate(program, args, input_output_examples)
        latest_io_log = io_log
    except Exception as e:
        error_message = e
    
    last_program = program
    count += 1

if (found):
    logging.info("Result: Success")
else:
    logging.info("Result: Failed")
logging.info("\n\n\n")
