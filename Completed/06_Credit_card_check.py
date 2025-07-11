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
    match len(str(card_number)): #sort cards by their number length
        case 15:
            if str(card_number)[0:2] == "34" or str(card_number)[0:2] == "37": #check if number begins in 34 or 37
                return "AMEX"
        case 13:
            if str(card_number)[0] == "4": #check if number begins in 4
                return "VISA"
        case 16:
            if str(card_number)[0:2] in ["51","52","53","54","55"]: #check if number begins between 51-55
                return "Mastercard"
            if str(card_number)[0] == "4": #check if number begins with 4
                return "VISA"
            if str(card_number)[0:4] == "6011": #check if the number begins with 6011
                return "Discover"
    return "Unknown" #if the card does not match anything, return "Unknown"

def get_issuer_new(card_number):
    card_string = str(card_number)
    if card_string[0:2] in ["34","37"] and len(card_string) == 15: #check for AMEX
        return "AMEX"
    if card_string[0:4] == "6011" and len(card_string) == 16:#check for Discover
        return "Discover"
    if int(card_string[0:2]) in range(51,56) and len(card_string) == 16:#check for Mastercard
        return "Mastercard"
    if card_string[0] == "4" and len(card_string) in [13,16]:#check for VISA
        return "VISA"
    return "Unknown" #if the card does not match anything, return "Unknown"

def assertion_tests():
    
    #These assertions should be true
    get_issuer(4111111111111) == "VISA"
    get_issuer_new(4111111111111) == "VISA"
    get_issuer(378282246310005) == "AMEX"
    get_issuer_new(378282246310005) == "AMEX"
    get_issuer(6011111111111117) == "Discover"
    get_issuer_new(6011111111111117) == "Discover"
    get_issuer(5105105105105100) == "Mastercard"
    get_issuer_new(5105105105105100) == "Mastercard"
    get_issuer(9111111111111111) == "Unknown"
    get_issuer_new(9111111111111111) == "Unknown"


    # The assertions are false
    assert get_issuer(123456789012345) != "AMEX", "This should not be AMEX."
    assert get_issuer_new(123456789012345) != "AMEX", "This should not be AMEX."
    assert get_issuer(123456789012345) != "Discover", "This should not be Discover."
    assert get_issuer_new(123456789012345) != "Discover", "This should not be Discover."
    assert get_issuer(123456789012345) != "Mastercard", "This should not be Mastercard."
    assert get_issuer_new(123456789012345) != "Mastercard", "This should not be Mastercard."
    assert get_issuer(123456789012345) != "VISA", "This should not be VISA."
    assert get_issuer_new(123456789012345) != "VISA", "This should not be VISA."
    assert get_issuer(4111111111111111) != "Unknown", "This should not be Unknown."
    assert get_issuer_new(4111111111111111) != "Unknown", "This should not be Unknown."

def performance_tests():

    input = random.randint(1000000000000,9999999999999999) #generate a number that must be between 13 - 16 digits long

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


def main():
    assertion_tests()
    performance_tests()

main()

