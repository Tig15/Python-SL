# It is a small anonymous function. It can take any number of arguments but can only have one expression.
# syntax = lambda argument : expression

# Add 10 to argument a, and return the result
x = lambda a : a + 10
print(x(5))

# Multiple argument a with argument b and return the result
z = lambda p,q : p*q
print(z(18,18))

# Lambda inside Function
def myfunc(n):
    return lambda y : y*n

mytripler = myfunc(3)
print(mytripler(33))