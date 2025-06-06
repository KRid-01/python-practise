text = "List Comprehension is Powerful".lower()

vowel = [x for x in text if x not in "aeiou " ]
print(vowel)