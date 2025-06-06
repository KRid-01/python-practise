x = int(input("Enter the number: "))

def is_prime(x):
    if x <= 1:
        return False
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
        
    return True

print(is_prime(x))

def is_prime(x):

    if x <= 1:
        return False
    
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
         
print(is_prime(x))