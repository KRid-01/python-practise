def char_frequency (text):
    text = text.lower()

    char_dict = {}

    for char in text:
        if char in " ":
            continue
        elif char  in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

print(char_frequency("Hello World"))