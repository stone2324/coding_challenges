# start: 9:14am 15/7/2025
# end: 9:26am 15/7/2025
# Reverse Number is a number which is the same when reversed.

# For example, the first 20 Reverse Numbers are:

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101
# TASK:

# You need to return the nth reverse number. (Assume that reverse numbers start from 0 as shown in the example.)
# NOTES:



def reverse_number(number):
    count = 0
    current = 0
    while count < number:
        if str(current) == str(current)[::-1]:
            count += 1
        current += 1
    
    return current - 1

def tests():
    assert reverse_number(1) == 0
    assert reverse_number(2) == 1
    assert reverse_number(10) == 9
    assert reverse_number(100) == 909
    print("All tests passed")

if __name__ == "__main__":
    tests()
    