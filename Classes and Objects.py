# Almost everything in Python is an object, with its properties and methods.
# A class is like an object constructor...
class Myclass:
    x = 5

p1 = Myclass() # p1 is an Object
print(p1.x)

# let's learn more about class and object by built-in funciton...
# __int__() and __str__()
# __int__() is only executed when class is initiated...
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person("Aman", 21)  
print(p2.name)
print(p2.age)   

#__str__()
class Per:
    def __init__(own, name, age):
        own.name = name 
        own.age =  age

    def __str__(own):
        return f"{own.name}({own.age})"

p3 = Per("Aashi", 19)
print(p3)     

# Objects can also contain Methods. Let's see how:
class Pers:
    def __init__(hex,name, age):
        hex.name = name 
        hex.age = age

    def mymethod(hex):
        print("Hey, My Name is " + hex.name)

p4 = Pers("Aman", 21)            
p4.mymethod()