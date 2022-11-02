'''company will give bonus base on following criteria

 time spent in company            Bonus
  .greater than 10 years            10%
  .more  than 6 years and 
  less than 10                       8%
  .less than 6%                      5%
  
  ask the salary and time spent from the user print the net bonus amount accordingly'''
  #solution


salary =int(input("original salary is:"))

years =int(input("work in years is:"))

if years>10:
    bonus= 10/100*salary
    print("the net bonus is",salary+bonus)
elif  years>6 and years<10:
    bonus =8/100*salary
    print("the net bonus",salary +bonus)
else:
    years>0 and years <6
    bonus =5/100*salary
    print("net bonus is",salary+bonus)


