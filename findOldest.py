# Take input of age from 3 people 
# Determine the oldest  and youngest

ram = int(input("age of ram is :"))

shayam =int(input("age of shayam is:"))

khali =int(input("the age of khali is:"))

if ram >shayam and ram <khali:
    print("ram is oldest",ram)
elif shayam >ram and shayam<khali:
    print("shayam is older",shayam)
else:
    khali >ram and khali <shayam
    print("khali is youngest",khali)
