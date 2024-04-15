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
    A CFG for string manipulation tasks, explanation of the CFG and some input-output examples will be provided. \
    Your task is to synthesize a program within <program></program> tag following the CFG by finding out the string manipulation task \
    applied to the given inputs to obtain the corresponding outputs. Do not write any part of the program that does not \
    satisfy the given CFG.
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

def construct_user_message(string_variables, string_literals, integer_variables, integer_literals, input_output_examples):
    str_var = ""
    str_lit = ""
    int_var = ""
    int_lit = ""

    vars_and_lits = ""
    io_examples = ""

    if (string_variables):
        vars_and_lits += ', '.join(string_variables) + ": String Variable(s)\n    "
        str_var = ' | '.join(string_variables) + ' | '
    if (string_literals):
        vars_and_lits += ', '.join(map(repr, string_literals)) + ": String Literal(s)\n    "
        str_lit = ' | '.join(map(repr, string_literals)) + ' | '
    if (integer_variables):
        vars_and_lits += ', '.join(integer_variables) + ": Integer Variable(s)\n    "
        int_var = ' | '.join(integer_variables) + ' | '
    if (integer_literals):
        vars_and_lits += ', '.join(map(repr, integer_literals)) + ": Integer Literal(s)\n    "
        int_lit = ' | '.join(map(repr, integer_literals)) + ' | '

    for i in range(len(input_output_examples)):
        formatted_pairs = [f'{key}: "{value}"' for key, value in input_output_examples[i].items()]
        io_examples += str((i+1)) + ". " + ', '.join(formatted_pairs) + "\n    "

    DSL = f"""
    I have the following CFG for string manipulation task:

    CFG:
    ```
    Start —> S
    S —> {str_var}{str_lit}(replace S S S) | (concat S S) | (substr S I I) | (ite B S S) | (int.to.str I) | (at S I)
    B —> true | false | (= I I) | (contains S S) | (suffixof S S) | (prefixof S S)
    I —> {int_var}{int_lit}(str.to.int S) | (+ I I) | (-I I) | (length S) | (ite B I I) | (indexof S S I)
    ```
    """

    DSL_explanation = f"""
    Here is the explanation of the above CFG:

    CFG Explanation:
    ```
    {vars_and_lits}: string and integer variables and literals
    true, false: boolean literals
    replace S S S: replace s x y, replaces first occurrence of string literal or argument x in string argument s with string literal or argument y
    concat S S: concat x y, concatenates string literal or argument x and string literal or argument y
    substr S I I: substr x y z, extracts substring of length z, from index y, where the index starts from 0
    ite B S S: ite x y z, returns string literal or argument y if x is true, otherwise string literal or argument z
    int.to.str I: int.to.str x, converts int x to a string
    at S I: at x, y returns the character at index y in string x
    = I I: = x y, returns true if integer literal or argument x equals integer literal or argument y
    contains S S: contains x y, returns true if string literal or argument x contains string literal or argument y
    suffixof S S: suffixof x y, returns true if string x literal or argument is the suffix of string literal or argument y
    prefixof S S: prefixof x y, returns true if string literal or argument x is the prefix of string literal or argument y
    str.to.int S: str.to.int x, converts string x to an integer
    + I I: + x y, sums integer literal or argument x and integer literal or argument y
    - I I: - x y, subtracts integer literal or argument y from integer literal or argument x
    length S: length x, returns length of string x
    ite B I I: ite x y z, returns integer y if x is true, otherwise integer z
    indexof S S I: indexof x y z, returns index of y in x, starting at index z
    ```
    """

    constraints = f"""
    Now I am providing {len(input_output_examples)} examples. Each example contains the input to the string and/or integer argument(s) and an output (out). Here are the examples:

    {io_examples}
    """

    user_message = DSL + DSL_explanation + constraints

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

    total_terms_and_nonterms = [
        'replace', 'concat', 'substr', 'ite', 'int.to.str', 'at',
        'true', 'false', '=', 'contains', 'suffixof', 'prefixof',
        'str.to.int', '+', '-', 'length', 'ite', 'indexof'
    ]

    with open(config_directory+"bustle_benchmarks.txt") as f:
        benchmarks = f.read().splitlines()

        string_variables = []
        string_literals = []
        integer_variables = []
        integer_literals = []

        benchmark = None
        filename = benchmarks[TaskId]
        print("filename =", filename)

        benchmark = filename

        specification_parser = StrParser(benchmark)
        specifications = specification_parser.parse()
        logging.info("\n")

        string_variables = specifications[0]
        string_literals = specifications[1]
        integer_variables = specifications[2]
        integer_literals = specifications[3]
        
        input_output_examples = specifications[4]

    total_terms_and_nonterms = total_terms_and_nonterms + string_variables + string_literals + integer_variables + [str(num) for num in integer_literals]
    # print(total_terms_and_nonterms)

    user_message = construct_user_message(string_variables, string_literals, integer_variables, integer_literals, input_output_examples)

    if (error_message):
        user_message += f"""
        The last program obtained from you was ```{last_gpt_program}``` which threw the following error message:
        ```
        {error_message}
        ```
        Please check if the program satisfies the given CFG. Then update this program and make it functional to obtain the expected output.
        """
    elif (latest_io_log):
        user_message += f"""
        The last program obtained from you was: ```{last_gpt_program}```.
        The output and the expected output do not match. \
        They look like the following:
        ```
        {latest_io_log}
        ```
        Please check if the program satisfies the given CFG. Then update this program and make it functional to obtain the expected output.
        """

    print("=================Request================")
    print(user_message)
    print()
    response = get_response_from_api(user_message)
    print("=================Response===============")
    print(response)
    print()

    # Define a regular expression pattern to match text inside <program></program> tags
    pattern = r'<program>(.*?)<\/program>'

    # Use re.findall to find all matches of the pattern in the input string
    matches = re.findall(pattern, response, re.DOTALL)

    # Print the extracted text
    program = matches[0].strip()
    logging.info("Program: " + program + "\n")
    program = program.replace('\n', '').replace("'", '"')
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

    return program, input_output_examples, string_variables, integer_variables

def validate(program, input_output_examples, string_variables, integer_variables):
    program_list = parse_string(program)

    is_success = True
    # print(program_list)
    # print()
    logging.info("Expected Output\t\t\tGPT Output")
    logging.info("-----------------------------------------------------")
    io_log = ""
    expected_vs_obtained = ""
    for example in input_output_examples:
        example_program_list = deepcopy(program_list)
        for var in string_variables + integer_variables:
            replace_placeholders(example_program_list, var, example[var])
        # print("======================")
        # print(example_program_list)
        # print("======================")
        ast = get_ast(example_program_list)
        ast = evaluate(ast)
        io_log += example['out'] + "\t\t\t" + ast.data + "\n"

        if ((example['out']) != ast.data):
            # expected_vs_obtained += "Expected output is " + example['out'] + ", but obtained " + ast.data + "\n"
            expected_vs_obtained += f"""For argument(s) {[example[arg] for arg in string_variables + integer_variables]}, expected output is "{example['out']}", but obtained "{ast.data}"\n"""

        if (example['out'] != ast.data):
            is_success = False
    logging.info(io_log)

    return is_success, expected_vs_obtained

found = False
last_program = None
latest_io_log = None
error_message = None
count = 0

while(not found):
    if (count == 10):
        break

    try:
        program, input_output_examples, string_variables, integer_variables = synthesize(last_program, error_message, latest_io_log)
    except:
        continue

    try:
        found, io_log = validate(program, input_output_examples, string_variables, integer_variables)
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

# unavailable_elems = [item for item in flatten_program_list if item not in total_terms_and_nonterms]

# if unavailable_elems:
#     print(get_dsl_match_not_found(unavailable_elems))

# iterate_lists(program_list)
