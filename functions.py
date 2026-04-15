#Write a function called multiply_all that takes a list of numbers as an argument and returns the product of all those numbers.
def multiply_all(*numbers):
    product=1
    for n in numbers:
        product=product*n
    return product
print(multiply_all(1,2,3))