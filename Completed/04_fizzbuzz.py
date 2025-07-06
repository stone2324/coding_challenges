#------------------------------
# Problem statement
#------------------------------

# Write a function that prints the numbers from 1 to 100, but with the following rules:

# For numbers that are multiples of 3, print "Fizz" instead of the number.

# For numbers that are multiples of 5, print "Buzz" instead of the number.

# For numbers that are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

# For all other numbers, print the number itself.

#------------------------------
# Function Signature
#------------------------------

# def fizz_buzz() -> None:
#     pass

def fizz_buzz():
    for number in range(1,100):
        if number % 3 == 0:
            if number % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizz_buzz()

