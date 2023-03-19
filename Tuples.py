# Tuples are ordered, unchangeable... They are written in round brackets
red = ("cherry", "strawberry", "raspberry")
print(red)

# A Tuple can have only one item in it, but there has to be comma after it.
one = ("date",)
print(one)

# Tuple is immutable, so the item cannot be changed directly but we have our methods...
y = ("red", "crimson", "cyan")
x = list(y)
x[2] = "firebrick"
y = tuple(x)

print(y)

a = ("cyan", "orange", "magenta")
b = list(a)
b.append("yellow")
a = tuple(b)

print(a)

# Tuple can be change with other tuple...
tup1 = ("violet", "indigo","blue", "green", "yellow", "orange")
tup2 = ("red",)
tup1 += tup2
print(tup1)

# Unpacking in a tuple...
tup = ("Shoyo", "Aoi", "Kuroko", "Kagami", "Kise")
(volley, foot, *basket) = tup
print(volley)
print(foot)
print(basket)