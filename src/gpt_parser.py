def iterate_lists(lst):
    for i in lst:
        if isinstance(i, list):
            iterate_lists(i)
    print(lst)

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

# s = '(concat (concat lastname ", ") (concat (at firstname 0) "."))'
# print(parse_string(s))
