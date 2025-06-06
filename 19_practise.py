matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]

# positive = [x for x in matrix[0] if x > 0 ]
# positive_2 = [y for y in matrix[1] if y > 0 ]
# positive_3 = [z for z in matrix[2] if z > 0]

# new_list = []
# for i in  positive:
#     new_list.append(i)
# for j in  positive_2:
#     new_list.append(j)
# for k in  positive_3:
#     new_list.append(k)

# print(new_list)

positive = [  num for row in matrix for num in row if num > 0]
print(positive)