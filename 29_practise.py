def are_anagrams (str1, str2):

    str1_clean = sorted(str1.replace(" ", "").lower())
    str2_clean = sorted(str2.replace(" ", "").lower())

    return str1_clean == str2_clean
    

print(are_anagrams("Listen", "Silent"))
print(are_anagrams("Hello", "World"))
print(are_anagrams("Listen", "Silentt"))