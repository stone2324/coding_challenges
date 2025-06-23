# start: 2:49pm 23/6/2025
# end: 3:00pm 23/6/2025
# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

#   12 ==> 21
#  513 ==> 531
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

#   9 ==> -1
# 111 ==> -1
# 531 ==> -1

def next_bigger(number):
    number_in_array = [int(item) for item in str(number)] #turn into an array
    number_in_array.sort() #sort the array from lowest to highest
    compare_output = number
    output = ""
    for digit in number_in_array: #reverse and put it into output variable
        output = str(digit) + output
    output = int(output) #turn into output to return
    if compare_output == output or len(number_in_array) == 1:
        return -1
    return output
    
def tests():
    assert next_bigger(1111) == -1
    assert next_bigger(1234) == 4321
    assert next_bigger(1121) == 2111
    assert next_bigger(1) == -1

if __name__ == "__main__":
    tests()