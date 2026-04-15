# The Divider: Write a code snippet that asks the user for two numbers and divides them. Use a try...except block to catch the error if the user tries to divide by zero.

try:
    num1=int(input("Give num1: "))
    num2=int(input("Give num2: "))
    num3=num1/num2
    print(num3)
except ZeroDivisionError:
    print("enter value other then 0")
except ValueError:
    print("enter some value")