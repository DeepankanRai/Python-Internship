def ConvertBinary(n):
    if n>1:
        ConvertBinary(n//2)
    print(n%2,end="")


n=int(input("Enter a number:"))
print("The binary of a givrn number is:",ConvertBinary(n))