numbers = int(input("How many numbers you want in the List?: "))
my_list = []

for items in range (numbers):
    items = int(input("Enter the number: "))
    my_list.append(items)

print(my_list)

greatest = max(my_list)

while greatest in my_list:
    my_list.remove(greatest)

s_greatest = max(my_list)
print(s_greatest)