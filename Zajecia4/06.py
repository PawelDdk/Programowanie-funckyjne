numbers = [1, 2, 3, 4, 5]

def apply_function_to_list(lst, func):
    return [func(x) for x in lst]

def square_function(x):
    return x ** 2

print(apply_function_to_list(numbers, square_function)) 