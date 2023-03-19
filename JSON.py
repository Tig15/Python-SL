# Python has a built-in package called json, which can be used to work with JSON data.
# If you have JSON string, you can parse it by json.loads() methods
# Let's convert JSON to Python
import json
My_Data = '{ "name" : "Aman Srivastava", "age" : 20, "height" : 170, "profession" : "student"}'

y = json.loads(My_Data)

print(y["height"])

# Let's convert Python to JSON
import json
Player = {
    "name" : "Akaashi Seijuro",
    "move" : "Emperor Eye",
    "position" : "Point Guard"
}

z = json.dumps(Player)
print(z)


my_name = input("Enter Your Name: ")
print("My Name is " + my_name)