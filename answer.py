"""
Write a program that asks a user a question and saves their answer to a file.
"""


x = input("Do you like pizza?\n")
with open("answer.txt", "w") as f:
    f.write(x)
