list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

def sum_lists(list, other_list):
    result = tuple(sum(pair) for pair in zip(list, other_list))
    return result

print(sum_lists(list1, list2))