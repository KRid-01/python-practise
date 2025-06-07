def count_vowels(text):
    vowel_count = 0
    text = text.lower()
    
    for i in text:
        if i in "aeiou":
            vowel_count += 1
    return vowel_count

print(count_vowels())