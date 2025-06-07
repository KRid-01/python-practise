# def second_largest(my_list=[]):
#     return max([num for num in my_list if num!= max(my_list) ])
# print(second_largest([10,20,4,45,99,99]))

def second_largest(my_list=[]):
    unique_numbers = list(set(my_list))

    if len(unique_numbers) < 2:
        return None
    
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

print(second_largest([10, 20, 4, 45, 99, 99]))
print(second_largest([5, 5, 5]))