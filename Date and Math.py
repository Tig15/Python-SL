# Let's use Datetime Module...
import datetime 
# x = datetime.datetime(2019, 4, 15)
x = datetime.datetime.now()

# print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.second)
print(x.microsecond)

print(x.strftime("%B")) # strftime() - It use for formatting date objects into readable strings.
print(x.strftime("%b"))
print(x.strftime("%A"))
print(x.strftime("%p"))
print(x.strftime("%Z"))

# Let's use Math Module before that let's check some built in function...
x = min(4,26,-8)
y = max(26,83, 29)
print(x)
print(y)

z = abs(-47)
print(z)

a = pow(2, 8)
print(a)

# Let's use Math Module now...
import math 
X = math.sqrt(144)
print(X)

Z = math.ceil(2.6)
Y = math.floor(3.93)
print(Z)
print(Y)

W = math.pi 
print(W)

