print("Enter two numbers and I will divide them and tell you the remainder")

num1 = input("Enter your first number:\n")
num2 = input("Enter your second number:\n")

remainder = int(num1) % int(num2)
print("The remainder of " + num1 + " divided by " + num2 + " is " + str(remainder))
