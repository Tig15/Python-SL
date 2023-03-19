# Python has different data types built in by default, in these categories:

# 1. Text Type = str(string)
myName = "Aman"
print(myName)

# 2. Numeric Type = int(integer), float, complex
myAge = 21 #integer
print(myAge)

myPercentage = 81.19 #float
print(myPercentage)

comp = 1 + 2j #complex
print(comp)

# Numeric Type Conversion
x = 3
y = 2.36
z = 3j

a = float(x) # int to float
b = int(y) # float to int
c = complex(x) # int to complex

print(a)
print(b)
print(c)

# Type function to determine which datatype that variable is...
print(type(x))
print(type(y))
print(type(z))

# 3. Sequence Type = list, tuple, range
# 4. Mapping Type = dict
# 5. Set Type = set, frozenset
# 6. Boolean Type = bool
# 7. Binary Type = bytes, bytearray, memoryview
# 8. None Type = nonetype