class Person:

    def __innit__(self, n, g, a, t, w):
        self.name = n
        self.gender = g
        self.age = a
        self.tall = t
        self.weight = w

def talk(self):
    print("Hi I'm ", self.name)

def vote(self):
    if self.age < 18:
        print(" I am not eligible to vote")
    else:
        print("I am eligible to vote")

obj1 = Person("Sam", "Male", 22, 168, 50)
obj2 = Person("Jesse", "Female", 16, 179, 87)
print (obj1.name, obj2.name)
