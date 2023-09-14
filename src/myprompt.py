import openai

openai.api_key = "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"

user_message = f"""
I have a python list of lists. For example, it can be like [[1,2],[3,[4,5]]]. \
I want to iterate through the list from the innermost to the outermost. \
The output for the above list should be [4,5]\n[3,[4,5]]\n[1,2],\n[[1,2],[3,[4,5]]].

Write a python code to achieve these.
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
