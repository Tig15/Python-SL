# A Variable is only available from inside the region it is created, is called Scope.
# Local Scope
def myfunc():
    x = 300
    print(x)

myfunc()   

# Global Scope
x = 43
def myday():
    global x # Global Keyword is use to make variable global for function.
    x = 27

myday()

print(x)