x=int(input("enter ist number:"))
y=int(input("enter 2nd number:"))

def findHCF(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    return hcf
print("the hcf of two giv3n number is", findHCF(x,y))