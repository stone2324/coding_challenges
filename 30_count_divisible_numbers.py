# start 11:15am 8/7/2025
# end: 11:39am 8/7/2025
# Complete the function that takes 3 numbers x, y and k (where x ≤ y),
# and returns the number of integers within the range [x..y] (both ends included) that are divisible by k.

# More scientifically: { i : x ≤ i ≤ y, i mod k = 0 }

# Example
# Given x = 6, y = 11, k = 2 the function should return 3,
#  because there are three numbers divisible by 2 between 6 and 11: 6, 8, 10

# Note: The test cases are very large. You will need a O(log n) solution or better to pass. (A constant time solution is possible.)
import random
from functools import partial
from utils import assert_all_equal, benchmark_functions, print_output


def divisible_count_v1(lower_num, higher_num, k):
    count = 0
    for i in range( lower_num, higher_num + 1, 1 ):  # goes up by one, checking if each number is valid
        if i % k == 0:
            count += 1
    return count


def divisible_count_v2(lower_num, higher_num, divisor):
    # creates a list of valid digits and counts the lenght
    divisible_number_list = [number for number in range(lower_num, higher_num + 1, 1) if number % divisor == 0]
    count = len(divisible_number_list)
    return count


def divisible_count_v3(lower_num, higher_num, divisor):
    # let's say lower is 1, higher is 4, and divisor is 2
    # I could list out [2,4] and see that there are 2 numbers..

    # another way is to find out how many valid numbers from 0 - higher and 0 - lower
    # then find the difference between both numbers

    divisible_up_to_higher = higher_num // divisor
    divisible_up_to_lower = (lower_num - 1) // divisor
    return divisible_up_to_higher - divisible_up_to_lower


def assertion_tests():
    assert divisible_count_v1(6, 11, 2) == 3
    assert divisible_count_v2(6, 11, 2) == 3
    assert divisible_count_v3(6, 11, 2) == 3

    assert divisible_count_v1(100, 100, 10) == 1
    assert divisible_count_v2(100, 100, 10) == 1
    assert divisible_count_v3(100, 100, 10) == 1

    assert divisible_count_v1(101, 101, 10) == 0
    assert divisible_count_v2(101, 101, 10) == 0
    assert divisible_count_v3(101, 101, 10) == 0
    print("All tests passed!")


def performance_tests():
    lower = random.randint(1, 100)
    higher = random.randint(101, 500)
    divisor = random.randint(1, 20)
    runs = 50000

    functions_to_run = [
        ("divisible_count_v1", partial(divisible_count_v1, lower, higher, divisor)),
        ("divisible_count_v2", partial(divisible_count_v2, lower, higher, divisor)),
        ("divisible_count_v3", partial(divisible_count_v3, lower, higher, divisor)),
    ]
    print(f'''The inputs are:
Lower: {lower}, Higher: {higher}, Divisor: {divisor}
''')
    print_output(functions_to_run)
    print()
    assert_all_equal(functions_to_run)
    benchmark_functions(functions_to_run, runs)


def main():
    assertion_tests()
    performance_tests()


if __name__ == "__main__":
    main()
