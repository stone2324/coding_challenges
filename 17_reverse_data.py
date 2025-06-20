# start: 7:47am 21/6/2025
# end   8:14am 21/6/2025
# A stream of data is received and needs to be reversed.

# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)
# should become:

# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)
# The total number of bits will always be a multiple of 8.

# The data is given in an array as such:

# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]


def reverse_data(bit_stream):
    result = []

    for i in range(len(bit_stream) - 8, -1, -8):
        result += bit_stream[i : i + 8]
    return result

def tests():
        # One byte (no changes)
    assert reverse_data([1,0,1,0,1,0,1,0]) == [1,0,1,0,1,0,1,0]

    #Two bytes
    assert reverse_data([1,1,1,1,0,0,0,0, 0,1,0,1,1,0,1,0]) == [0,1,0,1,1,0,1,0, 1,1,1,1,0,0,0,0]

    #Empty list
    assert reverse_data([]) == []

    input = [
        1,1,1,1,1,1,1,1,  # byte 1
        0,0,0,0,0,0,0,0,  # byte 2
        1,0,1,0,1,0,1,0,  # byte 3
    ]
    expected_output = [
        1,0,1,0,1,0,1,0,
        0,0,0,0,0,0,0,0,
        1,1,1,1,1,1,1,1,
    ]
    assert reverse_data(input) == expected_output
if __name__ == "__main__":
    tests()