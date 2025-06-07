    #last se remove karke aage insert karna hai
    #matlab [-1] se remove karke [0] pe insert karna hai
def rotate_list(my_list, k):
    my_list = my_list[:]
    for i in range(k):
       last = my_list.pop()
       my_list.insert(0, last)
        
    return my_list

print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([10, 20, 30], 1))