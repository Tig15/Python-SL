# It is a collection which is ordered, changeable and no duplicate allow..
# They are written in curly bracket and key:value pair.
karasuno = {
    "player" : "Hinata Shoyo",
    "height" : 164,
    "position" : "Spiker"
}
print(karasuno)

# We can specifically any key:value pair like this
print(karasuno["position"])

# We can use list in dict too...
p2 = {
    "name" : "Kageyama Tobio",
    "height" : 183,
    "position" : ["setter","spiker","server"]
}
print(p2)
print(p2["position"])

# We can access item in dictionary by two ways...
p3 = {
    "name" : "Miya Atsumu",
    "height" : 177,
    "position" :"ideal setter"
}
z = p3["position"] # First Way
print(z)

x = p3.get("position") # Second Way
print(x)

# keys(), values()...
p4 = {
    "name" : "Oikawa",
    "height" : 176,
    "team" : "Aoba Johsei"
}

# a = p4.keys()
b = p4.values()
print(b)

p4["team"] = "MSYW Black Jackal"
print(b)

