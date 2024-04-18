def remove_whitespace(str_list):
    return [string.replace(" ", "") for string in str_list]

strings = ["  hello  ", "  world  ", "  python  "]
print(remove_whitespace(strings))