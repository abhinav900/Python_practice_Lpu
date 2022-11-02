from re import X


#x=int(input("number is:"))
#if x%2==0 and x%3==0:
 
#   print("true")
#else:
#    print("false")



a =int(input("first side is:"))
b=int(input("second side is:"))
c=int(input("third side is:"))
if a+b>c and b+c>a and c+a>b:
    print("triangle possible")
else:
    print("triangle is not possible")
