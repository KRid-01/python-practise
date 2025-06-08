text = "the quick brown fox jumps over the lazy dog the fox was quick"
words = text.split()

frequency_words = {word: words.count( word )for word in words}
print(frequency_words)