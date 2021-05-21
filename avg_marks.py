if __name__ == '__main__':
    n = int(input("enter number of students:"))
    student_marks = {}
    for i in range(n):
        name, *line = input("enter name and obtained marks:").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("enter name of student:")
    if query_name in student_marks:
        avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
        print(format(avg_score, '.2f'))
