# start: 4:05pm 14/6/2025
# end: 4:29pm 14/6/2025
# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

# In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :

#     /                             \
#     | p    p+1   p+2    p+3       |
#     |a  + b   + c    + d    +...  |  = n * k
#     \                             /

# If it is the case we will return k, if not return -1.

# Note: n and p will always be strictly positive integers.

# Examples:
# n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

# n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

# n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

# n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51


def digits_powered(number, power):
    total = 0
    for index, digit in enumerate(str(number), start=power):
        total += int(digit) ** index #raise a digit to the index of the number's power
        #for example, if the number was 1234, and the power input was 2:
        #1 would be raised to the power of 2, 2 would be raised to the power of 3 and so on
    if total % number == 0:
        return int(total / number)
    return -1


def assertion_tests():
    #test for true case
    assert digits_powered(89, 1) == 1
    assert digits_powered(46288, 3) == 51
    assert digits_powered(41, 5) == 25
    assert digits_powered(114, 3) == 9
    assert digits_powered(8, 3) == 64
    assert digits_powered(695,2) == 2

    #test for case that don't work
    assert digits_powered(92, 1) == -1
    assert digits_powered(95, 1) == -1

def main():
    assertion_tests()

if __name__ == '__main__':
    main()