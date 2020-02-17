"""
Converts input string to float and prints the result.
:param string: str.
:return: num
"""

def string_to_float(string):
    try:
        num = float(string)
        return(num)
    except(ValueError):
        print("Invalid input")
