num=int(input("ENTER YOUR NUMBER  "))
while(num!=0):
    digit=num%10
    print(digit, end="")
    num=num//10
