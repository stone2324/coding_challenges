#-------------------
# Problem Statement
#-------------------

# Write a function that checks whether a given array of integers is a palindrome.

# An array is considered a palindrome if it reads the same forwards and backwards.

#-------------------
# Function Signature
#-------------------
# def is_palindrome_array(arr: list[int]) -> bool:
#     pass

#-------------------
# Example
#-------------------

# is_palindrome_array([1, 2, 3, 2, 1])     # Output: True
# is_palindrome_array([4, 5, 6, 5, 4])     # Output: True
# is_palindrome_array([1, 2, 3, 4])        # Output: False
# is_palindrome_array([9])                # Output: True
# is_palindrome_array([])                 # Output: True (empty array is considered a palindrome)

def is_palindrome_array(input_array):
    for index in range(len(input_array)-1):
        if not input_array[index] == input_array[(index + 1) * -1]:
            return False     
    return True


test_array = [1, 2, 3, 2, 1]

print(is_palindrome_array(test_array))


