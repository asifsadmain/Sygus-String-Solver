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
        print(' ' * level + str(self.data) + ' (Level: ' + str(level) + ')')
        for child in self.children:
            child.print_tree(level + 1)

    def get_leaves_level(self, level=0):
        if not self.children:
            return level
        return max(child.get_leaves_level(level + 1) for child in self.children)

    def get_nodes_at_level(self, level, current_level=0):
        if level == current_level:
            return [self]
        else:
            nodes = []
            for child in self.children:
                nodes.extend(child.get_nodes_at_level(level, current_level + 1))
            return nodes

def replace_node(root, level, old_data, new_subtree):
    if level == 0 and root.data == old_data:
        return new_subtree
    for i in range(len(root.children)):
        if root.children[i].data == old_data and level == 1:
            root.children[i] = new_subtree
        else:
            replace_node(root.children[i], level - 1, old_data, new_subtree)
    return root
```

For the function "replace_node", if there are duplicate old_data at the same level, update the code so that it only replaces the first occurence.
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
