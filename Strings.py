# Strings in python are displayed by Single Quotation and Double Qoutation.
myName = "Aman"
print(myName)

# Multiline Strings can be displayed by three quotes

# Strings are Array in Python
my_name = "Aman Srivastava"
print(my_name[3])

# Looping through String
for x in "Aman":
    print(x)

# String Length, len() function
a = "Best Author"
print(len(a))

# Check the string by using 'in'
sentence = "I am going to be best author!"
print("best" in sentence)

# Slicing of Strings, where first character has Index-0, 
slc = "Let's Slice The String"
print(slc[4:11])
      
slcs = "Let's Slice The String"    # i. Slice from the start
print(slcs[:9])               
      
slce = "Let's Slice The String"   # ii. Slice from the end
print(slce[5:])

slcn = "Let's Slice The String"   # iii. Negative Index, means count from backwards
print(slcn[-12:-3])

# UpperCase amd LowerCase function
uc = "Let's Do Coding!"
print(uc.upper())

lc = "We are Strong!"
print(lc.lower())

# Removing Whitespace - strip() function
white = "Welcome to My Place!"
print(white.strip())

# Replace the String
rep = "Welcome to By Place"
print(rep.replace('B', 'M'))

# split() funtion returns list
z = "We are Unrivaled!"
print(z.split())

# Concatenation, which done by "+" operator
x = "Don't"
y = "Give Up"
msg = x + " " + y      # " " is used to keep space between the message
print(msg)

# format() method, which helps to combine number in the strings with placeholder {}
age = 21
Intro = 'My name is Aman Srivastava and I am {}'
print(Intro.format(age))