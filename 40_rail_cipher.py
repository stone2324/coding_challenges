#start: 8:25pm 23/7/2025
#end:9:00pm 25/7/2025
#  Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails". First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.

# For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

# W       E       C       R       L       T       E
#   E   R   D   S   O   E   E   F   E   A   O   C  
#     A       I       V       D       E       N    
# The encoded string would be:

# WECRLTEERDSOEEFEAOCAIVDEN
# Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.

# Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns the DECODED string.

# For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an empty string.

# Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests that include punctuation. Don't filter out punctuation as they are a part of the string.

def encode_rail_fence_cipher(string_to_encode, rails_amount):
    if not string_to_encode or rails_amount < 2:
        return ""

    
    rail_lines = ['' for _ in range(rails_amount)]
    rail = 0
    direction = 1  # 1 for down, -1 for up

    for char in string_to_encode:
        rail_lines[rail] += char
        rail += direction

        if rail == 0 or rail == rails_amount - 1:
            direction *= -1
    output = "".join(rail_lines)
    return output

def decode_rail_fence_cipher(string_to_decode, rails):
    if not string_to_decode or rails < 2:
        return ""

    pattern = []
    rail = 0
    direction = 1

    for i in string_to_decode:
        pattern.append(rail)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    #create empty lists for each rail
    rail_lists = [[] for _ in range(rails)]
    rail_lengths = [0] * rails

    #count how many leters go to each rail
    for rail_index in pattern:
        rail_lengths[rail_index] += 1

    
    idx = 0
    for rail_idx in range(rails):
        for _ in range(rail_lengths[rail_idx]):
            rail_lists[rail_idx].append(string_to_decode[idx])
            idx += 1

    
    rail_positions = [0] * rails
    result = ""

    for rail_index in pattern:
        result += rail_lists[rail_index][rail_positions[rail_index]]
        rail_positions[rail_index] += 1

    return result

def tests():
    assert encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3) == "WECRLTEERDSOEEFEAOCAIVDEN"
    assert decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3) == "WEAREDISCOVEREDFLEEATONCE"

    assert encode_rail_fence_cipher("HELLO", 2) == "HLOEL"
    assert decode_rail_fence_cipher("HLOEL", 2) == "HELLO"

    assert encode_rail_fence_cipher("Hello, World!", 4) == "H !e,Wdloollr"
    assert decode_rail_fence_cipher("H !e,Wdloollr", 4) == "Hello, World!"

    assert encode_rail_fence_cipher("", 3) == ""
    assert decode_rail_fence_cipher("", 3) == ""
    print("All tests passed!")

if __name__ == "__main__":
    tests()
