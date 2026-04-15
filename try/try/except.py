# Write a code snippet that has a list of 3 colors. Ask the user to input an index (a number). Use a try...except block to:

# Print the color at that index if it exists.
# Catch an IndexError and print "That index is out of range!" if the user enters a number like 5.
# Catch a ValueError and print "Please enter a valid whole number!" if the user enters a word instead of a number.
colors = ["red", "blue", "green"]
try:
    num=int(input("Enter a number 0-2: "))
    print({colors[num]})
except SyntaxError:
    print(" there is syntax error")
except IndexError:
    print("Enter number between 0 to 2")
except ValueError:
    print("Enter number between 0 to 2")