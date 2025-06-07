
def count_words(text):
    import string
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    words = text.split()

    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict

print(count_words("krishna is a good boy! "))