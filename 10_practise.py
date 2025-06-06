def students():
    student_info = []
    number = int(input("Enter the number of students: "))
    
    for i in range (number):
        name = input("Enter the name: ")
        score = float(input("Enter the score: "))
        student_info.append([name,score])
    student_info.sort(key=lambda x: (x[1],x[0]))

    scores = [x[1] for x in student_info]

    unique_scores = sorted(set(scores))

    if len(unique_scores) < 2:
        return "There is no second lowest score"
    second_lowest = unique_scores[1]

    result = [x[0] for x in student_info if x[1] == second_lowest]
    for names in result:
        print (names)

students()