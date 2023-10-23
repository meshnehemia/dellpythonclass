class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print(self.name, "is studying ")


p = Person("meshack", 34, "male")

p.details()


