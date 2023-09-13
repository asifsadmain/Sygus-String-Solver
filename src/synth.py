def string_manipulation(input_string):
    # Define the CFG rules for string manipulation
    def S(input_string):
        return input_string

    def replace(input_string, x, y):
        return input_string.replace(x, y)

    def concat(x, y):
        return x + y

    # Split the input into tokens
    tokens = input_string.split()

    # Apply the CFG rules based on the examples
    if len(tokens) == 1:
        return S(input_string)
    elif len(tokens) == 2:
        # Handle cases with "US" or "CAN"
        if tokens[1] in ["US", "CAN"]:
            return replace(input_string, " " + tokens[1], "")
        else:
            return S(input_string)
    elif len(tokens) == 3:
        # Handle cases where the last token is "US" or "CAN"
        if tokens[2] in ["US", "CAN"]:
            return replace(input_string, " " + tokens[2], "")
        else:
            return S(input_string)
    else:
        return S(input_string)

# Test the code with the provided examples
print(string_manipulation("Mining US"))  # Output: "Mining"
print(string_manipulation("Soybean Farming CAN"))  # Output: "Soybean Farming"
print(string_manipulation("Soybean Farming"))  # Output: "Soybean Farming"
print(string_manipulation("Oil Extraction US"))  # Output: "Oil Extraction"
print(string_manipulation("Fishing"))  # Output: "Fishing"
