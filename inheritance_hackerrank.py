class Person:
    def __init__(self, firstname, lastname, person_id):
        self.firstname = firstname
        self.lastname = lastname
        self.person_id = person_id

    def display_person(self):
        print("Name:", self.lastname + " " + self.firstname)
        print("ID:", self.person_id)


class Student(Person):
    def __init__(self, firstname, lastname, person_id, scores):
        super().__init__(firstname, lastname, person_id)
        self.scores = scores

    def calculate_grade(self):
        a = sum(self.scores) / len(self.scores)
        if 90 <= a <= 100:
            return 'O'
        elif 80 <= a < 90:
            return 'E'
        elif 70 <= a < 80:
            return 'A'
        elif 55 < a < 70:
            return 'P'
        elif a < 40:
            return 'T'


line = input().split()
first_name = line[0]
last_name = line[1]
student_id = line[2]
obtained_scores = list(map(int, input().split()))
student = Student(first_name, last_name, student_id, obtained_scores)
student.display_person()
print("Grade:", student.calculate_grade())
