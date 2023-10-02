# from gpt_parser import parse_string

# def iterate_lists(lst):
#     for i in lst:
#         if isinstance(i, list):
#             iterate_lists(i)

#     print()
#     print(lst)

# def check_parentheses(s):
#     stack = []
#     for char in s:
#         if char == '(':
#             stack.append(char)
#         elif char == ')':
#             if not stack:
#                 return False
#             stack.pop()
#     return not stack

# # s = "(ite (suffixof ' US' _arg_0) (substr _arg_0 0 (- (length _arg_0) (length ' US'))) (ite (suffixof ' CAN' _arg_0) (substr _arg_0 0 (- (length _arg_0) (length ' CAN'))) _arg_0))"
# s = "(suffixof ' US' _arg_0)"
# print(check_parentheses(s))

# # lst = [['ite', ['contains', '_arg_0', ' US'], ['replace', '_arg_0', ' US', ''], ['ite', ['contains', '_arg_0', ' CAN'], ['replace', '_arg_0', ' CAN', ''], '_arg_0']]] ['ite', 'contains', '_arg_0', ' US', 'replace', '_arg_0', ' US', '', 'ite', 'contains', '_arg_0', ' CAN', 'replace', '_arg_0', ' CAN', '', '_arg_0']
# # # lst = [['replace', '_arg_0', ' US', ''], ['replace', '_arg_0', ' CAN', '']]
# parsed_string = parse_string(s)
# print("Parsed String: ", parsed_string)
# iterate_lists(parsed_string[0])

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

def build_ast(input_list):
    if isinstance(input_list, list):
        node = Node(input_list[0])
        for item in input_list[1:]:
            node.add_child(build_ast(item))
        return node
    else:
        return Node(input_list)

def replace_node(root, level, old_data, new_subtree):
    if level == 0 and root.data == old_data:
        return new_subtree
    for i in range(len(root.children)):
        if root.children[i].data == old_data and level == 1:
            root.children[i] = new_subtree
        else:
            replace_node(root.children[i], level - 1, old_data, new_subtree)
    return root

# Test the function
input_list = ['concat', 'lastname', ['concat', ', ', ['concat', ['substr', 'firstname', '0', '1'], '.']]]
ast = build_ast(input_list)

ast.print_tree()
print()

new_subtree = build_ast(['concat', 'new_lastname', ['concat', ', ', ['concat', ['substr', 'new_firstname', '0', '1'], '.']]])

# Replace the old subtree with the new one
ast = replace_node(ast, 1, 'concat', new_subtree)

# Print the modified tree
ast.print_tree()

def dfs(node):
    if node is not None:
        for child in node.children:
            dfs(child)
    print(node.data)

# Test the function
# dfs(ast)
