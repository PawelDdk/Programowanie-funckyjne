def cumulative_sum(lst):
    cum_sum = []
    total = 0
    for num in lst:
        total += num
        cum_sum.append(total)
    return cum_sum


numbers = [1, 2, 3, 4, 5]
print(cumulative_sum(numbers))