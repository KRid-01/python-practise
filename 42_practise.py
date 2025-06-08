inventory = {
    "banana": 8,
    "orange": 7,
    "grape": 12
}
inventory.update({"apples":5})
inventory["banana"] -= 3
del inventory["orange"]
print(inventory)