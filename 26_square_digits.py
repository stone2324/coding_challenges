# start: 3:02 4/7/2025
# end: 3:05 4/7/2025
#  Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

def square_digits(number):
    number_as_string = str(number)
    output = ""
    for digit in number_as_string:
        output += str(int(digit) * int(digit))
    return int(output)

def tests():
    assert square_digits(1) == 1
    assert square_digits(12) == 14
    assert square_digits(12345) == 1491625
    assert square_digits(0) == 0
if __name__ == "__main__":
    tests()
    
    