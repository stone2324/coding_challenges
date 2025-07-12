# start: 2:54pm 12/7/2025
# end: 3:24pm 12/7/2025
# In mathematics, an nth root of a number x, where n is usually assumed to be a positive integer
# , is a number r which, when raised to the power n, yields x:

# r^n=x,

# Given number n, such that n > 1, find if its 2nd root,
# 4th root and 8th root are all integers (fractional part is 0),
#  return true if it exists, false if not.

# # 2nd root of 256 is 16
# # 4th root of 256 is 4
# # 8th root of 256 is 2
# perfect_roots(256) # returns True


def perfect_roots(n):
    second_root = n ** (1 / 2) #power by half, making it square root
    fourth_root = n ** (1 / 4) #power by quarter , making it forth root
    eighth_root = n ** (1 / 8) #power by eighth, making it eight root

    if second_root == int(second_root) and fourth_root == int(fourth_root) and eighth_root == int(eighth_root):
        return True

    return False

def tests():
    assert perfect_roots(256) == True
    assert perfect_roots(6561) == True
    assert perfect_roots(101) == False
    assert perfect_roots(50) == False
    print("All tests passed")

if __name__ == "__main__":
    tests()