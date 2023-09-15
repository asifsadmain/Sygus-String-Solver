def iterate_lists(lst):
    for i in lst:
        if isinstance(i, list):
            iterate_lists(i)
    print(lst)


def generate_string(parsed):
    if isinstance(parsed, str):
        return parsed
    elif isinstance(parsed, list):
        if parsed[0] == 'replace':
            s1 = generate_string(parsed[1])
            s2 = generate_string(parsed[2])
            s3 = generate_string(parsed[3])
            return f'(replace {s1} {s2} {s3})'
        elif parsed[0] == 'concat':
            s1 = generate_string(parsed[1])
            s2 = generate_string(parsed[2])
            return f'(concat {s1} {s2})'
        elif parsed[0] == 'substr':
            s = generate_string(parsed[1])
            i1 = generate_string(parsed[2])
            i2 = generate_string(parsed[3])
            return f'(substr {s} {i1} {i2})'
        elif parsed[0] == 'ite':
            b = generate_string(parsed[1])
            s1 = generate_string(parsed[2])
            s2 = generate_string(parsed[3])
            return f'(ite {b} {s1} {s2})'
        elif parsed[0] == 'int.to.str':
            i = generate_string(parsed[1])
            return f'(int.to.str {i})'
        elif parsed[0] == 'at':
            s = generate_string(parsed[1])
            i = generate_string(parsed[2])
            return f'(at {s} {i})'
        elif parsed[0] in ['true', 'false', '=', 'contains', 'suffixof', 'prefixof']:
            i1 = generate_string(parsed[1])
            i2 = generate_string(parsed[2])
            return f'({parsed[0]} {i1} {i2})'
        elif parsed[0] in ['1', '0', '-1']:
            return parsed[0]
        else:
            raise SyntaxError(f'Unexpected token: {parsed[0]}')
    else:
        raise SyntaxError(f'Unexpected input type: {type(parsed)}')

# Example usage:
# parsed_input = ['concat', '"US"', ['replace', '"CAN"', '"CA"', '""']]
# parsed_input = [['replace', '"US"', '"CA"']['replace', ['concat', '" "', '"CAN"'], '""']]
# result = generate_string(parsed_input)
# print(result)
