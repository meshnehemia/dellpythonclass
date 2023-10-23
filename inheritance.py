class Animal:
    def speak(self):
        print("Animal is speaking")


class Dog(Animal):
    def bark(self):
        print("the dog is barking")

class Cat(Animal):
    def moow(self):
        print("cat is meowing")


d = Dog()
d.speak()
