# start: 8:14pm 22/6/2025
# end: 9:03pm 22/6/2025
# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

def snail(snail_map):
    result = []

    
    while snail_map:
        # take the first row from the top and add to result
        result += snail_map.pop(0)

        # take the last item from the remaining rows (moving down the right side)
        for row in snail_map:
            if row:  # ensure the row isn't empty
                result.append(row.pop())

        # take the last row from the bottom , and read backwards
        if snail_map:
            last_row = snail_map.pop()
            last_row.reverse()  # reverse in place
            result += last_row

        # take the first item from the remaining rows (moving up the left side)
        for row in reversed(snail_map):
            if row:  # ensure the row isn't empty
                result.append(row.pop(0))

    return result

def tests():

    array = [[1,2,3],
            [8,9,4],
            [7,6,5]]
    assert snail(array) == [1,2,3,4,5,6,7,8,9]

    
    array = [[42]]
    assert snail(array) == [42]

    
    array = [[1, 2],
            [4, 3]]
    assert snail(array) == [1, 2, 3, 4]

    
    array = [[ 1, 2, 3, 4],
            [12,13,14, 5],
            [11,16,15, 6],
            [10, 9, 8, 7]]
    assert snail(array) == list(range(1, 17))

    
    assert snail([]) == []

    
    assert snail([[], [], []]) == []

if __name__ == "__main__":
    tests()
    