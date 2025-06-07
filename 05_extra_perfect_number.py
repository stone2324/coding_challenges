
# An extra perfect number is a positive integer whose first and last bits in binary representation are set (i.e., both are 1).

# Task
# Given a positive integer N, return all the extra perfect numbers in the range from 1 to N, inclusive.

# Notes
# The input is always a positive integer.
# The returned list/array should contain the extra perfect numbers in ascending order, from lowest to highest.
# Extra perfect numbers correspond to binary representations that start and end with 1.
# Input >> Output Examples
#   extraPerfect(3)  ==>  return {1, 3}
# Explanation:
# 1 in binary is 1 → first and last bits are set.
# 3 in binary is 11 → first and last bits are set.
#   extraPerfect(7)  ==>  return {1, 3, 5, 7}
# Explanation:
# 5 in binary is 101 → first and last bits are set.
# 7 in binary is 111 → first and last bits are set.

def extra_perfect(N):
    output = []
    for i in range(1,N+1,2):
        output.append(i)
    return output