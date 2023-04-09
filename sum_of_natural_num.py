def Sum(n):
    if n<=1:
        return n
    else:
        return(n)+Sum(n-1)
    
n=int(input("ENter a number here:"))

if n<=0:
    print("Enter a positive number:")
else:
    print("The sum is:",Sum(n))