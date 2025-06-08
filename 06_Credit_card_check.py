# Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

# Complete the function get_issuer() that will use the values shown below to determine the card issuer for a given card number. If the number cannot be matched then the function should return the string Unknown.

# | Card Type  | Begins With          | Number Length |
# |------------|----------------------|---------------|
# | AMEX       | 34 or 37             | 15            |
# | Discover   | 6011                 | 16            |
# | Mastercard | 51, 52, 53, 54 or 55 | 16            |
# | VISA       | 4                    | 13 or 16      |
# Examples
# get_issuer(4111111111111111) == "VISA"
# get_issuer(4111111111111) == "VISA"
# get_issuer(4012888888881881) == "VISA"
# get_issuer(378282246310005) == "AMEX"
# get_issuer(6011111111111117) == "Discover"
# get_issuer(5105105105105100) == "Mastercard"
# get_issuer(5105105105105106) == "Mastercard"
# get_issuer(9111111111111111) == "Unknown"

from functools import partial
from utils import assert_all_equal, benchmark_functions, print_output
import random


def get_issuer(card_number):
    match len(str(card_number)):
        case 15:
            if str(card_number)[0:2] == "34" or str(card_number)[0:2] == "37":
                return "AMEX"
        case 13:
            if str(card_number)[0] == "4":
                return "VISA"
        case 16:
            if str(card_number)[0:2] in ["51","52","53","54","55"]:
                return "Mastercard"
            if str(card_number)[0] == "4":
                return "VISA"
            if str(card_number)[0:4] == "6011":
                return "Discover"
    return "Unknown"

def get_issuer_new(card_number):
    card_string = str(card_number)
    if card_string[0:2] in ["34","37"] and len(card_string) == 15:
        return "AMEX"
    if card_string[0:4] == "6011" and len(card_string) == 16:
        return "Discover"
    if int(card_string[0:2]) in range(51,56) and len(card_string) == 16:
        return "Mastercard"
    if card_string[0] == "4" and len(card_string) in [13,16]:
        return "VISA"
    return "Unknown"

def main():

    random.seed(42)
    input = [str(random.randint(0,9)) for _ in range(random.randint(13,16))]
    input = int("".join(input))

    n_runs = 50000

    funcs = [
        ("get_issuer", partial(get_issuer, input)),
        ("get_issuer_new", partial(get_issuer_new, input))
        ]
    print(f"The input is {input}")
    print()
    print_output(funcs)
    print()
    assert_all_equal(funcs)
    benchmark_functions(funcs, n_runs)

main()
