def symmetric_differnece (list1, list2):
    list_1 = set(list1)
    list_2 = set(list2)

    return list_1.symmetric_difference(list_2)

print(symmetric_differnece([1, 2, 3, 4], [3, 4, 5, 6]))