# start: 7:30am 25/6/2025
# end: 7:59am 25/6/2025
# Let us consider this example (array written in general format):

# ls = [0, 1, 3, 6, 10]

# Its following parts:

# ls = [0, 1, 3, 6, 10]
# ls = [1, 3, 6, 10]
# ls = [3, 6, 10]
# ls = [6, 10]
# ls = [10]
# ls = []
# The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

# The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of the sums of its parts as defined above.

# Other Examples:
# ls = [1, 2, 3, 4, 5, 6] 
# parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

# ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
# parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]
# Notes
# Take a look at performance: some lists have thousands of elements.
# Please ask before translating.

def part_sum(list):
    sums = [] #establish the output list
    for index in range(len(list)): #create an an ascending sum
        total = 0
        for number in list[index:]:
            total += number
        sums.append(total)
    sums.append(0)
    return sums
    
    
def tests():
    # Correct cases
    assert part_sum([1, 2, 3, 4, 5]) == [15, 14, 12, 9, 5, 0]
    assert part_sum([0, 0, 0]) == [0, 0, 0, 0]
    assert part_sum([5]) == [5, 0]
    assert part_sum([]) == [0]
    assert part_sum([10, -10, 10]) == [10, 0, 10, 0]

    # Incorrect cases 
    assert part_sum([1, 2, 3]) != [6, 3, 3, 0] #incorect sum
    assert part_sum([4, 1]) != [5, 2] #no zero
    assert part_sum([2, 2, 2]) != [6, 4, 2] #no zero

if __name__ == "__main__":
    tests()
    print("All tests passed!")