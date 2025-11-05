from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("Human: I can walk and run")

class Snake(Animal):
    def move(self):
        print("Snake: I can crawl")

class Dog(Animal):
    def move(self):
        print("Dog: I can bark")

class Lion(Animal):
    def move(self):
        print("Lion: I can roar")

R = Human()
R.move()

K = Snake()
K.move()

D = Dog()
D.move()

L = Lion()
L.move()
