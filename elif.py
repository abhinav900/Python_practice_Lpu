#print if and else in one line 

#print("A") if a>b else print("b")



#question
'''marks    grade
100-90        A
90 -80        B
80-70         C
0-70          D '''

marks =int(input("enter your marks:"))  # both the condition are satisfied we use "And"
                                       # if any condition is satisfied we use "or"
if marks >90 and marks <=100:
    print("your grade is A")
elif marks >80 and marks <=90:
    print("your grade is B")
elif marks>70 and marks <=80:
    print("your grade is C")

elif marks >0 and marks <=70:
    print("your grade is D")
else:
    marks>100
    print("not a valid number")

