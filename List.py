# List are ordered, changeable and allows duplicate value
mixt1 = ["Kuroko", "Kagami", "Kise", "Kageyama", "Kuroda"]
print(mixt1)

# Index number - Item in list always start from 0
mixt2 = ["Akashi", "Midorima", "Takeshima", "Fukuda"]
print(mixt2[2])

print(mixt2[-1]) # Negative index, list starts from end

# Specifying the Range
side = ["Yes", "No", "True", "False", "Right", "Wrong", "Positive", "Negative"]
print(side[2:5])

print(side[3:]) # Leaving out the end value
print(side[:6]) # Leaving out the start value

if "Right" in side:
    print("Yes,'Right' is in the side list!")

# To change the specific item in list by index number...
vollyteam = ["Shoyo", "Kageyama", "Atsumu", "Akaashi"]
vollyteam[3] = "Oikawa"
print(vollyteam)

# insert() function, insert a new list item without replacing any other items...
footteam = ["Aoi", "Tachibana", "Togashi"]
footteam.insert(2,"Yuma")
print(footteam)

# append() function, this add the item at the end of list...
basketteam = ["Kuroko", "Akaashi", "Kise"]
basketteam.append("Aomine")
print(basketteam)

# extend() function, use to make two list, a single long list
add = ["red", "blue", 'green']
sub = ["cyan", "yellow", "magenta"]

add.extend(sub)
print(add)

# remove() - removes the specified item
# pop() - removes the specified item by index
# del - same as pop, but can aslo delete the list completely
# clear() - can empty the list, but list will be there, only all item will remove
color = ["red", "green", "yellow", "orange"]
color.remove("orange")
print(color)

shape = ["tri", "size", "circ", "rect"]
shape.pop(1)
print(shape)

Upper = ["A", "B", "C", "D", "X", "Y", "Z"]
Upper.clear()
print(Upper)

# for loop in the list
floop = ["Rate", "Gate", "Fate", "Mate"]
for x in floop:
    print(x)

# loop using in the list with help of range() and len()...
"""num = ["Three", "Five", "Seven", "Twenty"]
for a in range(len(num)):
    print(a)"""

# while loop in the list
"""wloop = ["set", "list", "tuple", "dictionary"]
i = 0
while i<len(wloop):
    print(num[i])
    i += 1"""

# sort() method
marks = [34,78,64,89,63,24]
marks.sort()
print(marks)

eng_marks = [12,23,22,43,13]
eng_marks.sort(reverse = True)
print(eng_marks)

# How to copy list in another list
first_list = ["A", "S", "M", "U"]
second_list = first_list.copy()
print(second_list)

# List Comprehension