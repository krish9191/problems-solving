if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    if query_name in student_marks:
        score = sum(student_marks[query_name]) / 3

        print(format(score, '.2f'))

# num = input("How many students?:  ")
# students=[]
# marks=[]
#
# for i in num:
#      name = input("input name of student :")
#      students.append(name)
#      mark = input("input mark of the student:")
#      marks.append(mark)
# for i in num:
#      print(students +, marks)