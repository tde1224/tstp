"""
Program that takes user input and displays information about me based on dictionary of attributes
"""

my_attributes = {"Height": "5'11", "favorite color": "blue", "dog's name": "Pig"}

user_input = input("What would you like to know about me? Valid options are a. Height, b. favorite color, and C. dog's name\n:")

if user_input == "Height":
    print(my_attributes["Height"])
if user_input == "favorite color":
    print(my_attributes["favorite color"])
if user_input == "dog's name":
    print(my_attributes["dog's name"])


                
