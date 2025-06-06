number = int(input("Enter the number: ")) 
i = 0
result = 0
number_str = str(number)

while i < len(number_str):
    result += int(number_str[i])
    i += 1

print(result)