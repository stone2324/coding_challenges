# Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format:

# [sign]a b/c

# where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c. Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional part must be provided absolute).

# If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.

# Division by zero should raise an error (preferably, the standard zero division error of your language).

# Value ranges
# -10 000 000 < x < 10 000 000
# -10 000 000 < y < 10 000 000
# Examples
# Input: 42/9, expected result: 4 2/3.
# Input: 6/3, expedted result: 2.
# Input: 4/6, expected result: 2/3.
# Input: 0/18891, expected result: 0.
# Input: -10/7, expected result: -1 3/7.
# Inputs 0/0 or 3/0 must raise a zero division error.
# Note
# Make sure not to modify the input of your function in-place, it is a bad practice.

def mixed_fraction(string):
    # Split numerator and denominator from input
    slash_index = string.find("/")
    numerator = int(string[:slash_index])
    denominator = int(string[slash_index + 1:])

    # Calculate whole number and remainder
    whole = abs(numerator) // abs(denominator)
    remainder = abs(numerator) % abs(denominator)

    # Determine the sign using a multiline if-statement
    sign = ""
    if numerator * denominator < 0:
        sign = "-"

    if remainder == 0:
        return sign + str(whole)
    elif whole == 0:
        return sign + f"{remainder}/{abs(denominator)}"
    else:
        return sign + f"{whole} {remainder}/{abs(denominator)}"
    
def tests():
    # Simple mixed fraction
    assert mixed_fraction("7/4") == "1 3/4"

    # Negative numerator
    assert mixed_fraction("-5/2") == "-2 1/2"

    # Proper fraction (no whole part)
    assert mixed_fraction("2/5") == "2/5"


if __name__ == "__main__":
    tests()