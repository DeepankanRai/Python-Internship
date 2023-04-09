low=int(input("enter low limit:"))
high=int(input("enter high limit:"))

for num in range (low,high+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        dig=temp%10
        sum+=dig**order
        temp//=10
    if num==sum:
        print(num)
