# Problem:
# Given a list of integers, write a Python function to remove all duplicates.
# Return the list in the same order as the first appearance.

from functools import partial
import random

from utils import assert_all_equal, benchmark_functions, print_output


def remove_duplicates_slow_1(arr):
    output_arr = []
    for input_item in arr:
        is_found = False
        for output_item in output_arr:
            if input_item == output_item:
                is_found = True
                break
        if is_found == False:
            output_arr.append(input_item)
    return output_arr


def remove_duplicates_slow_2(arr):
    output_arr = []
    for input_item in arr:
        if input_item not in output_arr:
            output_arr.append(input_item)
    return output_arr


def remove_duplicates_fast(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def main():

    random.seed(42)
    arr = [random.randint(1, 25) for _ in range(10_000)]

    n_runs = 5_000

    funcs = [
        ("remove_duplicates_slow_1", partial(remove_duplicates_slow_1, arr)),
        ("remove_duplicates_slow_2", partial(remove_duplicates_slow_2, arr)),
        ("remove_duplicates_fast", partial(remove_duplicates_fast, arr)),
    ]

    print_output(funcs)
    assert_all_equal(funcs)
    benchmark_functions(funcs, n_runs)


if __name__ == "__main__":
    main()
