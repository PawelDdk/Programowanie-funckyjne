def find_max_min_diff(lst):
    if not lst:
        return None
    max_val = max(lst)
    min_val = min(lst)
    return max_val - min_val

numbers = [10, 5, 8, 3, 12]
print(find_max_min_diff(numbers))