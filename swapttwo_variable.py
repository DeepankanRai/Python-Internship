#using 3rd variable
x=8
y=6

temp=x
x=y
y=temp

print("the value of x is",x)
print("the values of y is", y)

#without using 3rd variable

x=4
y=9
x,y=y,x

print("the value of x is",x)
print("the value of y is",y)