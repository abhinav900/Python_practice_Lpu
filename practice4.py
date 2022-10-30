''' A company decided to give bonus of rs 1000 to employee if his service is more than 5 years ask her their salary and year 
of service and print the net bonus '''

x =float(input("person current salary:"))

y =float(input("spend time in company in year:"))

if y>5:
    print("the net bonus is:",x+1000)

else:
    print("no bonus received")