print("Enter two numbers and I will divide them and tell you the quotient")

num1 = input("Enter your first number:\n")
num2 = input("Enter your second number:\n")

#Floor division (No remainder given)
quotient = int(num1) // int(num2)
print("The quotient of " + num1 + " divided by " + num2 + " is " + str(quotient))
