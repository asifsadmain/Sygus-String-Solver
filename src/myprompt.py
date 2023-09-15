import openai

openai.api_key = "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"

user_message = f"""
I have a python string that looks like this:
"(ite (suffixof ' US' _arg_0) (substr _arg_0 0 (- (length _arg_0) (length ' US'))) (ite (suffixof ' CAN' _arg_0) (substr _arg_0 0 (- (length _arg_0) (length ' CAN'))) _arg_0))"

Write a python code that check if any parentheses is missing or if there is any unexpected parentheses.
"""

response = openai.ChatCompletion.create(
model="gpt-4",
messages=[
        {"role": "user", "content": user_message}
    ],
temperature=0,
max_tokens=256
)

print(response['choices'][0]['message']['content'])
