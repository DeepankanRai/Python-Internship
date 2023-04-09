def fact(n):
    if n==1:
        return 1
    else:
        return(n* fact(n-1))
    
n=int(input("Enter a number:"))

if n<=0:
    print("Factorial does not exit")
else:
    print("Factorial of a given number is", fact(n))