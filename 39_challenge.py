# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

# Example:
# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "M"       -> 1000
# "CD"      ->  400
# "XC"      ->   90
# "XL"      ->   40
# "I"       ->    1
# Help:
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
# Courtesy of rosettacode.org

def roman_to_int(string):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(string):
        value = roman_numerals[char]
        
        if value < prev_value:
            total -= value
        else:
            total += value
            
        prev_value = value
    
    return total

def tests():
    assert roman_to_int("MM") == 2000
    assert roman_to_int("MDCLXVI") == 1666
    assert roman_to_int("M") == 1000
    assert roman_to_int("CD") == 400
    assert roman_to_int("XC") == 90
    assert roman_to_int("XL") == 40
    assert roman_to_int("I") == 1
    print("All tests passed!")

if __name__ == "__main__":
    tests()
    