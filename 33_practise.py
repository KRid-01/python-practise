def remove_duplicates(my_list=[]):
    result = []
    for item in my_list:
        if item not in result:
            result.append(item)

    return result


print(remove_duplicates([4, 7, 4, 9, 2, 9, 5, 1]))