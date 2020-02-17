"""
Write a program with an infinite loop (with the option to press q to quit) and a list of numbers
Each time through the loop ask the user to guess a number on the list and tell them
whether or not they guessed correctly.
"""

nums = [1, 5, 7, 2, 8, 99]

while True:
    guess = input("Guess a number, type q to quit\n:")
    if guess == "q":
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input")
        continue
    if guess in nums:
        print("You got it! " + str(guess) + " was in my list")
    else:
        print("Try again!")
            
    
    
