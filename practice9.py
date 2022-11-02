from ast import operator


first=input("enter first number:")
second=input("enter second number:")
operator=input("operator(+,-,*,/)")

first=int(first)
second=int(second)

if operator =="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator =="*":
    print(first*second)
else:
    operator =="/"
    print(first/second)