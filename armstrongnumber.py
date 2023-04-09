numb=int(input("Enter the number:"))

sum=0
temp=numb

while temp>0:
    dig=temp%10
    cube=dig**3
    sum=sum+cube
    temp//=10

if sum==numb:
    print("the number is armstrong")
else:
    print("the number is not armtrong")