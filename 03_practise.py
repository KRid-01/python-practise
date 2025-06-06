def add_item(item, items=None):
    if items == None:
        items = []
    items.append(item)
    return items

print(add_item("apple"))   # ?
print(add_item("banana"))  # ?
