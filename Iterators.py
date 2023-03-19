# It is an Object ccntains a countable number of values.
# The method we use in this are : __iter__() and __next__()
color = ("red", "green", "blue", "black")
myit = iter(color[3]) 

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class Mynumbers:
    def __iter__(self):
        self.a += 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = Mynumbers()
myit2 = iter(myclass)

for y in myit2:
    print(y)


# Stop  after 20 Iteration...
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myit3 = iter(myclass)

for x in myit3:
    print(x)
