a=int(input("enter a number"))

if a%2==0:
    print(a,"even number");

else:
    print(a,"odd number");


num=int(input("enter your number"))

if num>=60:
    print("1st")
elif num>=50:
    print("2nd")
elif num>=40:
    print("3rd")
else:
    print("fail")




# simple calculator

n1=int(input("enter number1"))
n2=int(input("enter number2"))
x=int(input("enter a numner for 1 add , 2 sub ,3 mul , 4 div"))

if x==1:
    print(n1+n2)
elif x==2:
    print(n1-n2)
elif x==3:
    print(n1*n2)
else:
    print(n1/n2)