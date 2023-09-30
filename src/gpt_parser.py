def iterate_lists(lst):
    for i in lst:
        if isinstance(i, list):
            iterate_lists(i)
    
    if lst[0] == 'substr':
        print(">>>>>>>>>>>>>>>>>>>>>>>")
        print(lst[1][int(lst[2]):int(lst[3])])
        lst = lst[1][int(lst[2]):int(lst[3])]
    print(lst)

def flatten_list(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result

def parse_string(s):
    stack = [[]]
    word = ''
    quote = False
    for c in s:
        if c == '(':
            stack.append([])
        elif c == ')':
            if word:
                stack[-1].append(word)
                word = ''
            temp = stack.pop()
            stack[-1].append(temp)
        elif c == ' ':
            if quote:
                word += c
            elif word:
                stack[-1].append(word)
                word = ''
        elif c == '"':
            if quote:
                stack[-1].append(word)
                word = ''
            quote = not quote
        else:
            word += c
    if word:
        stack[-1].append(word)
    subprograms = stack[0]

    return subprograms

# s = '(concat lastname (concat ", " (concat (substr firstname 0 1) ".")))'
# print(parse_string(s))
# iterate_lists(s[0])
