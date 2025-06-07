def difference_elements(list1 = [], list2 = []):

    list_1 = set(list1)
    list_2 = set(list2)

    # return list_1 - list_2
    return list_1.difference(list_2)
   
print(difference_elements([1, 2, 3, 4], [3, 4, 5, 6]))