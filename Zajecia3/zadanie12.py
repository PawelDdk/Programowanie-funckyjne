def rotate_list(lst, steps):
    if not lst:
        return lst
    steps = steps % len(lst)
    return lst[-steps:] + lst[:-steps]

letters = ['a', 'b', 'c', 'd', 'e']
print(rotate_list(letters, 2))