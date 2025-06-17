# start: 7:45 17/6/2025
# end: 
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


def move_zero(array):
    zeros_in_array = 0
    for index, item in enumerate(array): #count and remove zeros
        if item == 0:
            zeros_in_array += 1
            array.pop(index)
    array[len(array) : len(array) + zeros_in_array] = [0] * zeros_in_array #add zeros to the back 
    return array #return the output

def tests():
    assert move_zero([0,1,0,2,0,3,0,4,0,5]) == [1,2,3,4,5,0,0,0,0,0] #basic test
    assert move_zero([1,2,3,0,4,5,0,6,7,0,8,9,10,0]) == [1,2,3,4,5,6,7,8,9,10,0,0,0,0] #check if it can handle number 10 (it has 0 in it)
    assert move_zero([0]) == [0] #test for single digit
    assert move_zero([1]) == [1] #test for single digit
    assert move_zero([]) == [] #test for blank space

    assert move_zero([0,1,0,2,0,3,0,4,0,5]) != [1,2,3,4,5] #check if it adds 0
    assert move_zero([1,2,3,0,4,5,0,6,7,0,8,9,10,0]) != [10,9,8,7,6,5,4,3,2,1,0,0,0,0] #check if the order is the same
    assert move_zero([0]) != [0,0] #check if it adds an extra 0
    assert move_zero([]) != [0]

def main():
    tests()

if __name__ == "__main__":
    main()
    