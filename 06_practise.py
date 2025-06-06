number = int(input("Enter the number: "))
result = 0

while number != 0 :
    last_digit = number % 10
    result += last_digit
    number //= 10

print(result)