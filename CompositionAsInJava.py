class Planet:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class Person:
    def __init__(self, name: str, age: int, planet: Planet):
        self.name = name
        self.age = age
        self.planet = planet

    def __repr__(self):
        return f"{self.name} is {self.age} years old and is from {self.planet}"


earth = Planet("Earth")

neto = Person("Neto", 35, earth)

print(neto.planet)

print(neto)
