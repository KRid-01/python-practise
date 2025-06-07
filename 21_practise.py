def reverse_words(text):
    words = text.split()
    reversed_words = [x[::-1] for x in words]

    return " ".join(reversed_words)

print(reverse_words("hello world"))
print(reverse_words("python is fun"))