num=int(input("ENTER THE NUMBER "))
cube=0
sum=0
while(num!=0):
    digit=num%10
    cube=(digit**3)
    sum=sum+cube
    num=num//10
print("sum of the cubes of the digits are",sum)
