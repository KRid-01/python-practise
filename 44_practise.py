def count_chars(text):

    characters = {}
    for i in text :
        if i not in characters:
            characters[i] = 1
        else:
            characters[i] += 1
    return characters

print(count_chars("hello"))