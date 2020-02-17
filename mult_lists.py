"""
Multiply two lists together and append the results to a third list.
"""

nums_1 = [8, 19, 148, 4]
nums_2 = [9, 1, 33, 83]
nums_3 = list()

for num1 in nums_1:
    for num2 in nums_2:
        result = num1 * num2
        nums_3.append(result)

for num3 in nums_3:
    print(num3)
