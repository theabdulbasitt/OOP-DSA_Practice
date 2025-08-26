from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def speak(self):
        pass   # must be implemented by child classes

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# a = Animal()  # ❌ ERROR: Can't instantiate abstract class
d = Dog()
d.speak()