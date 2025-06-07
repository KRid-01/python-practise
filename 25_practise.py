def count_words(text):
    word_count = 0 
    words = text.split()

    word_dict = {}

    for word in words:
        word_dict.update(word, word_count)

    return word_dict

print(count_words("krishna is a good boy"))