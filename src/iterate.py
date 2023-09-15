from gpt_parser import parse_string

def iterate_lists(lst):
    for i in lst:
        if isinstance(i, list):
            iterate_lists(i)

    print()
    print(lst)

def check_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

# # s = "(ite (suffixof ' US' _arg_0) (substr _arg_0 0 (- (length _arg_0) (length ' US'))) (ite (suffixof ' CAN' _arg_0) (substr _arg_0 0 (- (length _arg_0) (length ' CAN'))) _arg_0))"
# s = "(suffixof ' US' _arg_0)"
# print(check_parentheses(s))

# # lst = [['ite', ['contains', '_arg_0', ' US'], ['replace', '_arg_0', ' US', ''], ['ite', ['contains', '_arg_0', ' CAN'], ['replace', '_arg_0', ' CAN', ''], '_arg_0']]] ['ite', 'contains', '_arg_0', ' US', 'replace', '_arg_0', ' US', '', 'ite', 'contains', '_arg_0', ' CAN', 'replace', '_arg_0', ' CAN', '', '_arg_0']
# # # lst = [['replace', '_arg_0', ' US', ''], ['replace', '_arg_0', ' CAN', '']]
# parsed_string = parse_string(s)
# print("Parsed String: ", parsed_string)
# iterate_lists(parsed_string[0])
