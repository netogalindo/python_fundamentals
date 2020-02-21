from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = []): # This is bad!
        self.name = name
        self.grades = grades # self.grades is the tag for the grades of every object now

    def take_exam(self, result: int):
        self.grades.append(result)


neto = Student("Neto")
arthur = Student("Arthur")
neto.take_exam(90)
print(neto.grades)
print(arthur.grades)
