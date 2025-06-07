def filter_and_square(nums=[]):
    square = [x*x for x in nums if x % 2 == 0]
    return square

print(filter_and_square([1, 2, 3, 4, 5, 6]))