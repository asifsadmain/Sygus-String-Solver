import openai
from datetime import datetime
import logging
import os
from utils import *
from sygus_parser import StrParser
from itertools import product
import sys
import re
from sygus_string_dsl import *
from gpt_parser import parse_string


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
    temperature=0,
    max_tokens=256
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
        formatted_pairs = [f'{key}: {value}' for key, value in input_output_examples[i].items()]
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
    {vars_and_lits}true, false: boolean literals
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
    - I I: - y y, subtracts integer literal or argument y from integer literal or argument x
    length S: length x, returns length of string x
    ite B I I: ite x y z, returns integer y if x is true, otherwise integer z
    indexof S S I: indexof x y z, returns index of y in x, starting at index z
    ```
    """

    constraints = f"""
    Now I am providing {len(input_output_examples)} examples. Each example contains the input to the string and/or integer argument(s) \
    and an output (out). Here are the examples:

    {io_examples}
    """

    user_message = DSL + DSL_explanation + constraints

    return user_message


slurm_task_id = sys.argv[1]
TaskId = int(slurm_task_id) - 1

with open(config_directory+"sygus_string_benchmarks.txt") as f:
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

user_message = construct_user_message(string_variables, string_literals, integer_variables, integer_literals, input_output_examples)

response = get_response_from_api(user_message)
print(response)

# Define a regular expression pattern to match text inside <program></program> tags
pattern = r'<program>(.*?)<\/program>'

# Use re.findall to find all matches of the pattern in the input string
matches = re.findall(pattern, response, re.DOTALL)

# Print the extracted text
program = matches[0].strip()
program = program.replace('\n', '')
print(parse_string(program))
