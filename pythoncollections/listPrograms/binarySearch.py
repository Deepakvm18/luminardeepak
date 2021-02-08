arr=[10,12,12,13,19,18,29,20]
element=int(input("ENTER THE ELEMENT YOU WANT TO SEARCH"))
arr.sort()
low=0
flag=0
upp=len(arr)-1

while(low<upp):
    mid = (low + upp) // 2
    if(element>arr[mid]):
        low=mid+1
    elif(element<arr[mid]):
        upp=mid-1
    elif(element==arr[mid]):
        flag=1
        break
if flag==0:
    print("element not found")
else:
    print("elemnt found")
