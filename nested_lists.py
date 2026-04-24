if __name__ == '__main__':
    students = []
    second_lowest_grade = float('inf')
    lowest_grade = float('inf')
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        if score < lowest_grade:
            second_lowest_grade = lowest_grade
            lowest_grade = score
        elif score < second_lowest_grade and score != lowest_grade:
            second_lowest_grade = score
       
    students.sort(key=lambda x: x[0])  # Sort alphabetically
  
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    for student in second_lowest_students:
        print(student)
