#user input string
#if length of that input is greater than 3 characters then add ing as suffix else print the same input

a =str(input("enter the name:"))
if len(a)>=3:
    print(a+'ing')
else:
    print(a)
    