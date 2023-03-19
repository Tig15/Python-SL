# Set is an unordered, unchangeable, and unindexed. 
# Set cannot allow duplicates.
# Set cannot be accesed but it can be looped and search the following items.
today = {"wednesday", "twentysix", "october"}
print(today)

for time in today:
    print(time)

print("october" in today) 

# Set cannot be changed but we can use this method too...
green = {"apple", "lemon", "watermelon", "peer"}
blue = list(green)
blue.append("blueberry")
green = set(blue)
print(green)

# add() method
z = {"false", "true","negative"}
z.add("positive")
print(z)

# We can use update() to add other set or any iterable object to current set...
present_set = {"twentysix", "october", "wednesday"}
past_set = {"twentyfive", "tuesday"}
present_set.update(past_set)
print(present_set)

future_list = ["twentyseven", "thursday"]
present_set.update(future_list)
print(present_set)

# For deleting set we use:
# remove() and discard()
# pop() and del and clear()

# union() - which add both the set...
# intersection_update() - which only pick the common from both set...
# symmetric_difference_update() - it will keep the item not in both set...

initial = {"two", "six", "ten", "twenty", "twentytwo"}
final = {"two", "five", "nine", "twenty", "twentytwo"}

# median = initial.union(final)
# median = initial.intersection_update(final)
median = initial.symmetric_difference_update(final)
print(median)