import openai

openai.api_key = "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"

user_message = f"""
I have this following code in python:
```code
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def print_tree(self, level=0):
        print(' ' * level + str(self.data))
        for child in self.children:
            child.print_tree(level + 1)

def build_ast(input_list):
    if isinstance(input_list, list):
        node = Node(input_list[0])
        for item in input_list[1:]:
            node.add_child(build_ast(item))
        return node
    else:
        return Node(input_list)

# Test the function
input_list = ['concat', 'lastname', ['concat', ', ', ['concat', ['substr', 'firstname', '0', '1'], '.']]]
ast = build_ast(input_list)

ast.print_tree() 

def dfs(node):
    if node is not None:
        for child in node.children:
            dfs(child)
    print(node.data)
```

Now write a function that can print the level of each node of the tree.
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
