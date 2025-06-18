# start: 6:47am 19/6/2025
# end: 7:10am 19/6/2025
# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"
#
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(number):
    number_as_string = str(number) #make it a string to easily get digits
    addends = [] #create list to store all expanded numbers
    for index, digit in enumerate(number_as_string,1): #loop through all digits
        if digit != "0": #ignore 0
            addends.append(digit + "0" * (len(number_as_string) - index)) #join the digit with trailing '0's
    output = " + ".join(addends) #join all items of the expanded nunmbers with a plus sign
    return output


def assertion_tests():
    assert expanded_form(12) == "10 + 2"
    assert expanded_form(34) == "30 + 4" # do basic tests
    assert expanded_form(123456) == "100000 + 20000 + 3000 + 400 + 50 + 6" # test for larger number
    assert expanded_form(10203) == "10000 + 200 + 3" #test for numbers with 0
    
    # test for false cases
    assert expanded_form(12) != "1 + 2"
    assert expanded_form(34) != "300 + 4"
    assert expanded_form(123456) != "10 + 2 + 3 + 4 + 5 + 6"
    assert expanded_form(10203) != "10000 + 0000 + 200 + 00 + 3"

def main():
    assertion_tests()

if __name__ == "__main__":
    main()