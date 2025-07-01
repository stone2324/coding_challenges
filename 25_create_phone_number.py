# start: 4:25pm 2/7/2025
# end: 4:40 2/7/2025
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!

def create_phone_number(arr):
    arr = [str(i) for i in arr]
    return "(" + "".join(arr[:3]) + ") " + "".join(arr[3:6]) + "-" + "".join(arr[6:])

def tests():
    assert create_phone_number([1,2,3,4,5,6,7,8,9,0]) == "(123) 456-7890"
    assert create_phone_number([9,8,7,6,5,4,3,2,1,0]) == "(987) 654-3210"
    assert create_phone_number([0,1,2,3,4,5,6,7,8,9]) == "(012) 345-6789"
    assert create_phone_number([5,5,5,1,2,3,4,5,6,7]) == "(555) 123-4567"
    print("All tests passed!")

if __name__ == "__main__":
    tests()
