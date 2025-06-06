n = int(input("How many numbers you want to enter: "))
numbers_or = []
for i in range(n):
    number = int(input())
    numbers_or.append(number)

odd_numbers = [x for x in numbers_or if x %2 != 0]
print(odd_numbers)

# numbers_or = [int(input()) for _ in range(int(input("How many numbers? ")))]
# odd_numbers = [x for x in numbers_or if x % 2 != 0]
# print(odd_numbers)