text = "hello world"

char_frequency = {char: text.count(char) for char in set(text) if char != " "}
print(char_frequency)