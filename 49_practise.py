scores = {
    "Alice": 82,
    "Bob": 67,
    "Charlie": 91,
    "David": 73,
    "Eva": 88
}

above_75 = {students: scores[students] for students in scores if scores[students] > 75}
print(above_75)