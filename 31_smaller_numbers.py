# start: 9:07am 10/7/2025
# end: 9:20am 10/7/2025
# This is a hard version of How many are smaller than me?. If you have troubles solving this one, have a look at the easier kata first.

# Write

# function smaller(arr)
# that given an array arr, you have to return the amount of numbers that are smaller than arr[i] to the right.

# For example:

# smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
# smaller([1, 2, 0]) === [1, 1, 0]
# Note
# Your solution will be tested against inputs with up to 120_000 elements

def smaller(array):
    output = [0 for i in array]
    for index,item in enumerate(array):
        for digit in array[index+1:]:
            if item > digit:
                output[index] += 1
    return output

def tests():
    assert smaller([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
    assert smaller([1, 2, 3]) == [0, 0, 0]
    assert smaller([1, 2, 0]) == [1, 1, 0]
    assert smaller([1, 2, 1]) == [0, 1, 0]
    assert smaller([1, 1, -1, 0, 0]) == [3, 3, 0, 0, 0]
    assert smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]) == [4, 1, 5, 5, 0, 0, 0, 0, 0]
    assert smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]) == [5, 2, 6, 6, 1, 1, 0, 0, 0, 0]
    print("All tests passed")

if __name__ == "__main__":
    tests()