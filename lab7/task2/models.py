class Animal:
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind

    def speak(self):
        return "..."

    def info(self):
        return self.name + " is " + str(self.age)

    def __str__(self):
        return self.kind + ": " + self.name


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Dog")

    def speak(self):
        return "Woof"


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cat")

    def speak(self):
        return "Meow"