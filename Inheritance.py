# Let's create parent class...
class Person:
    def __init__(tax, fname, lname):
        tax.fname = fname
        tax.lname = lname

    def myself(tax):
        print(tax.fname, tax.lname)

p1 = Person("Aman", "Srivastava")
p1.myself()

# Let's create child class...
class Student(Person):
    def __init__(tax, fname, lname):
        super().__init__(fname, lname)
    #pass - This use to say that child class is containing the same methods and properties as parents.

x = Student("Hinata", "Shoyo")  
x.myself()  