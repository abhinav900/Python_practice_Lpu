#first triangle

a = float(input("enter first side of triangle:"))

b = float(input("enter second side of triangle:"))

c = float(input("enter third side of triangle:"))

s = (a+b+c)/2
 
ar =(s*(s-a)*(s-b)*(s-c))**0.5

print("area of the triangle is:",ar)
