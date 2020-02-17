#read user input
str_num = input("Enter a number and I'll let you know if it's less than 10\
 or greater than or equal to 10\n")

#Convert string to int
int_num = int(str_num)

if int_num >= 10:
    print(str(int_num) + " is greater than or equal to 10")
else:
    print(str(int_num) + " is less than 10")
