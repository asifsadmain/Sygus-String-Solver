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

def replace_node(root, level, old_data, new_subtree, replaced=False):
    if level == 0 and root.data == old_data and not replaced:
        return new_subtree, True
    for i in range(len(root.children)):
        if root.children[i].data == old_data and level == 1 and not replaced:
            root.children[i] = new_subtree
            replaced = True
        else:
            root.children[i], replaced = replace_node(root.children[i], level - 1, old_data, new_subtree, replaced)
    return root, replaced

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

def replace_placeholders(lst, variable, value):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            replace_placeholders(lst[i], variable, value)
        elif isinstance(lst[i], str):
            lst[i] = lst[i].replace(variable, value)

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
    # print("After removing unnecessary brackets: ", input_list)
    input_list = convert_str_to_int(input_list)
    ast = build_ast(input_list)

    return ast

def evaluate(ast):
    while (ast.children):
        current_level = ast.get_leaves_level() - 1
        parents_of_leaves = ast.get_nodes_at_level(current_level)
        
        for parent_node in parents_of_leaves:
            term = parent_node.data

            if (term == 'concat'):
                new_term = parent_node.children[0].data + parent_node.children[1].data
            elif (term == 'substr'):
                new_term = parent_node.children[0].data[parent_node.children[1].data : parent_node.children[1].data + parent_node.children[2].data]
            elif (term == 'replace'):
                new_term = parent_node.children[0].data.replace(parent_node.children[1].data, parent_node.children[2].data)
            elif (term == 'ite'):
                if (parent_node.children[0].data):
                    new_term = parent_node.children[1].data
                else:
                    new_term = parent_node.children[2].data
            elif (term == 'int.to.str'):
                new_term = str(parent_node.children[0].data)
            elif (term == 'at'):
                new_term = parent_node.children[0].data[parent_node.children[1].data]
            elif (term == '='):
                if (parent_node.children[0].data == parent_node.children[1].data):
                    new_term = True
                else:
                    new_term = False
            elif (term == 'contains'):
                if parent_node.children[1].data in parent_node.children[0].data:
                    new_term = True
                else:
                    new_term = False
            elif (term == 'suffixof'):
                if parent_node.children[1].data.endswith(parent_node.children[0].data):
                    new_term = True
                else:
                    new_term = False
            elif (term == 'prefixof'):
                if parent_node.children[1].data.startswith(parent_node.children[0].data):
                    new_term = True
                else:
                    new_term = False
            elif (term == 'str.to.int'):
                new_term = int(parent_node.children[0].data)
            elif (term == '+'):
                new_term = parent_node.children[0].data + parent_node.children[1].data
            elif (term == '-'):
                new_term = parent_node.children[0].data - parent_node.children[1].data
            elif (term == 'length'):
                new_term = len(parent_node.children[0].data)
            elif (term == 'indexof'):
                new_term = parent_node.children[0].data.index(parent_node.children[1].data, parent_node.children[2].data)
            else:
                new_term = term
            ast, _ = replace_node(ast, current_level, parent_node.data, build_ast([new_term]))
        # ast.print_tree()

    return ast

# Test the function
# input_list = ['concat', ['concat', 'lastname', ', '], ['concat', ['at', 'firstname', '0'], '.']]
# input_list = ['substr', '938-242-504', '4', '3']
# input_list = convert_str_to_int(input_list)
# ast = get_ast(input_list)
# ast = evaluate(ast)
# ast.print_tree()
# print(ast.data)

# new_subtree = build_ast(['concat', 'new_lastname', ['concat', ', ', ['concat', ['substr', 'new_firstname', '0', '1'], '.']]])

# ast = replace_node(ast, 0, 'concat', build_ast([1]))
# ast.print_tree()

# print(ast.get_nodes_at_level(ast.get_leaves_level()-1))
