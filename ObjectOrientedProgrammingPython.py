# student = {"name": "Neto", "grades": (70, 80, 75, 100, 90, 75)}
#
#
# def average(sequence):
#     return sum(sequence) / len(sequence)
#
#
# print(average(student["grades"]))
#
# How would it be to do this with objects?


class Student:
    def __init__(self, name, grades): # This methods with __ on each side are called magic methods sometimes
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Neto", (100, 80, 75, 100, 90, 100))
student_two = Student("Jose", (90, 90, 70, 90, 80, 80))
print(student.name)
print(student.grades)
print(student.average_grade())
# This is the same as print(Student.average_grade(student))
print(student_two.average_grade())
