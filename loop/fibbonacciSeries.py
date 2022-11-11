num=int(input("Enter number:"))
n,m=0,1
sum=0
for i in range(0,num):
    print(sum)
    n=m
    m=sum
    sum=n+m
