import abc


class Animal(abc.ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, name):
        print("Animal speak")
        pass
