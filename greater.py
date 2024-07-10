'''
This program is about finding greater number between two numbers entered by user
'''
a = int(input("Enter first number: "))
b = int(input("Enter seconf number: "))

if a > b:
    print("First is greater")
elif b > a:
    print("Second is greater")
else:
    print("Both are equal")


#print("First is greater" if a>b else "Second is greater" if b>a else "Both are equal")-------------------->Another way
