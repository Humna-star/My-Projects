from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

class Monkey(Animal):
    def move(self):
        print("I can swing from trees")

class Fish(Animal):
    def move(self):
        print("I can swim")

class Bird(Animal):
    def move(self):
        print("I can fly")

class Elephant(Animal):
    def move(self):
        print("I can stomp")

class Kangaroo(Animal):
    def move(self):
        print("I can jump")

class zebra(Animal):
    def move(self):
        print("I can gallop")

class fox(Animal):
    def move(self):
        print("I can sneak")

class rabbit(Animal):
    def move(self):
        print("I can hop")

class turtle(Animal):
    def move(self):
        print("I can crawl slowly")

class bear(Animal):
    def move(self):
        print("I can lumber")

class rhinoceros(Animal):
    def move(self):
        print("I can charge")

class hippopotamus(Animal):
    def move(self):
        print("I can wade in water")

class crocodile(Animal):
    def move(self):
        print("I can swim and crawl")

H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()

M = Monkey()
M.move()

F = Fish()
F.move()

B = Bird()
B.move()

E = Elephant()
E.move()

K = Kangaroo()
K.move()

Z = zebra()
Z.move()

F = fox()
F.move()

R = rabbit()
R.move()

T = turtle()
T.move()

B = bear()
B.move()

R = rhinoceros()
R.move()

H = hippopotamus()
H.move()