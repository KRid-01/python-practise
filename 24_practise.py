def filter_even(num = None):
    if num == None:
        num = []
    return [x for x in num if x%2 == 0]
print(filter_even([1,2,3,4,5,6,7,8]) ) 

# def filter_even(num):
#     return [x for x in num if x % 2 == 0]

# print(filter_even([1, 2, 3, 4, 5, 6, 7, 8]))
