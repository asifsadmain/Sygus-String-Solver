def get_dsl_match_not_found(unavailable_elems):
    unavailable_elems = list(set(unavailable_elems))    # remove duplicates
    message = "The following items could not be found in the given CFG: "

    for i in range(len(unavailable_elems)):
        if i == len(unavailable_elems) - 1:
            message += f"'{unavailable_elems[i]}'.\n"
        else:
            message += f"'{unavailable_elems[i]}', "
    message+= f"""
    Hints:
    1. Check if you are considering more than one string literals together without applying concatenation operation.
    2. Re-read the CFG and stick with the grammar while writing the program.
    """

    return message
