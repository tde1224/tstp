#read user input
str_num = input("Enter a number and I'll let you know if it's less than or equal to 10\
 or greater than 10 but less than 25, or if the number is greater than 25\n")

#Convert string to int
int_num = int(str_num)

if int_num >= 10 and int_num <= 25:
    print(str(int_num) + " is greater than or equal to 10 but less than or equal to 25")
if int_num < 10:
    print(str(int_num) + " is less than 10")
if int_num > 25:
    print(str(int_num) + " is greater than 25")
