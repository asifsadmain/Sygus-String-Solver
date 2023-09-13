import openai

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


DSL = f"""
I have the following CFG for string manipulation task:

CFG:
```
Start —> S
S —> arg0 | "" | " " | "US" | "CAN" | (replace S S S) | (concat S S) | (substr S I I) | (ite B S S) | (int.to.str I) | (at S I)
B —> true | false | (= I I) | (contains S S) | (suffixof S S) | (prefixof S S)
I —> 1 | 0 | -1 | (str.to.int S) | (+ I I) | (-I I) | (length S) | (ite B I I) | (indexof S S I)
```
"""

DSL_explanation = f"""
Here is the explanation of the above CFG:

CFG Explanation:
```
arg0: string variables
"", " ", "US", "CAN": string literals
1, 0, -1: integer literals
true, false: boolean literals
replace S S S: replace s x y, replaces first occurrence of x in s with y
concat S S: concat x y, concatenates x and y
substr S I I: substr x y z, extracts substring of length z, from index y
ite B S S: ite x y z, returns y if x is true, otherwise z
int.to.str I: int.to.str x converts int x to a string
at S I: at x, y returns the character at index y in string x
= I I: = x y, returns true if x equals y
contains S S: contains x y, returns true if x equals y
suffixof S S: suffixof x y, returns true if x is the suffix of y
prefixof S S: prefixof x y, returns true if x is the prefix of y
str.to.int S: str.to.int x, converts string x to an integer
+ I I: + x y, sums x and y
- I I: - y y, subtracts y from x
length S: length x, returns length of x
ite B I I: ite x y z, returns y if x is true, otherwise x
indexof S S I: indexof x y z, returns index of y in x, starting at index z
```
"""

constraints = f"""
Now I am providing some examples. Each example contains one or many inputs and an output. Here are the examples:

Example 1:
```
input: Mining US
output: Mining
```
Example 2:
```
input: Soybean Farming CAN
output: Soybean Farming
```
Example 3:
```
input: Soybean Farming
output: Soybean Farming
```
Example 4:
```
input: Oil Extraction US
output: Oil Extraction
```
Example 5:
```
input: Fishing
output: Fishing
```
"""

user_message = DSL + DSL_explanation + constraints

response = get_response_from_api(user_message)
print(response)
