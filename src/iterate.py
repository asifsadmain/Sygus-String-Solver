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

def replace_node(root, level, old_data, new_subtree):
    if level == 0 and root.data == old_data:
        return new_subtree
    for i in range(len(root.children)):
        if root.children[i].data == old_data and level == 1:
            root.children[i] = new_subtree
        else:
            replace_node(root.children[i], level - 1, old_data, new_subtree)
    return root

def convert_str_to_int(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(convert_str_to_int(item))
        elif isinstance(item, str) and item.isdigit():
            result.append(int(item))
        else:
            result.append(item)
    return result

def remove_unnecessary_brackets(lst):
    if len(lst) == 1 and isinstance(lst[0], list):
        return remove_unnecessary_brackets(lst[0])
    return [remove_unnecessary_brackets(item) if isinstance(item, list) else item for item in lst]

def build_ast(input_list):
    if isinstance(input_list, list):
        node = Node(input_list[0])
        for item in input_list[1:]:
            node.add_child(build_ast(item))
        return node
    else:
        return Node(input_list)

def get_ast(input_list):
    input_list = remove_unnecessary_brackets(input_list)
    input_list = convert_str_to_int(input_list)
    ast = build_ast(input_list)

    return ast

# Test the function
# input_list = ['concat', 'lastname', ['concat', ', ', ['concat', ['substr', 'firstname', '0', '1'], '.']]]
# input_list = convert_str_to_int(input_list)
# ast = build_ast(input_list)

# ast.print_tree()
# print()

# new_subtree = build_ast(['concat', 'new_lastname', ['concat', ', ', ['concat', ['substr', 'new_firstname', '0', '1'], '.']]])

# ast = replace_node(ast, 2, 'concat', new_subtree)
# ast.print_tree()
