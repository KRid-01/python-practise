x = int(input("Enter the number: "))
def is_palindrome(x):
    original = x
    palindrome = 0      
    while x != 0:
        last_digit = x % 10
        palindrome = palindrome * 10 + last_digit
        x//=10
    # return palindrome
    if original == palindrome:
        return original == palindrome
    return False

print(is_palindrome(x))  