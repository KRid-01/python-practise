nums = [3, 6, 1, 8, 5, 2]

squares_index = {index: values**2 for index, values in enumerate(nums) if values % 2 == 0}
print(squares_index)