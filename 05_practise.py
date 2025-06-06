number = int(input("Enter the number: "))
number_str = str(number)
result = 0

for i in number_str:
    result += int(i)

print (result)

# number = int(input("Enter the number: "))
# result = 0

# for digit in str(number):
#     result += int(digit)

# print(result)
