# It is block of a code which only runs when it called...
def my_function():
    print("Welcome to My Function Area")

my_function()  

# What if we want multiple name of people in a group
def my_group(name, age):
    print(name, age)

my_group("Aman", 20)
my_group("Ayush", 21)
my_group("Bharat", 21)

# prefix of arguments (*) - args
# prefix of keyword arguments (**) - kwargs

# Recursion means that a function call itself
# In this example, tri_recursion() is function that we have defined to call itself. We use the k variable as the data, which decrements(-1) every time we recurse.

def tri_recursion(k):
    if (k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

tri_recursion(15)