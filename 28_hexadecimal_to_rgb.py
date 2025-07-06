# start: 2:00pm 6/7/2025
# end:
# When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component values for a color. Implement a function that meets these requirements:

# Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")
# Returns a Map<String, int> with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255
# Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")

# Example:
# "#FF9933" --> {r: 255, g: 153, b: 51}

def hex_string_to_RGB(hex_string):
    hex_string = hex_string.replace("#","").lower()
    hex_to_decimal = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,'5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }
    rgb = {
        'r':0,
        'g':0,
        'b':0}
    for index, item in enumerate(["r","g","b"]):
        section_of_hex = hex_string[index*2 : index * 2 + 2]
        converted = hex_to_decimal[section_of_hex[0]] * 16 + hex_to_decimal[section_of_hex[1]]
        rgb[item] = converted
    return rgb
    
def tests():
    assert hex_string_to_RGB("#FF9933") == {'r': 255, 'g': 153, 'b': 51}
    assert(hex_string_to_RGB("#beaded") == {'r':190, 'g':173, 'b':237})
    assert(hex_string_to_RGB("#000000") == {'r':0, 'g':0, 'b':0})
    assert(hex_string_to_RGB("#111111") == {'r':17, 'g':17, 'b':17})
    assert(hex_string_to_RGB("#Fa3456") == {'r':250, 'g':52, 'b':86})
    print("All tests passed")
    
if __name__ == "__main__":
    tests()