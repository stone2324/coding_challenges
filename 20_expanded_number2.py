# start: 7:00am 24/6/2025
# end: 
# You will be given a number and you will need to return it as a string in expanded form :

# expanded form illustration

# For example:

# 807.304 --> "800 + 7 + 3/10 + 4/1000"
#   1.24  --> "1 + 2/10 + 4/100"
#   7.304 --> "7 + 3/10 + 4/1000"
#   0.04  --> "4/100"

def expanded_form(number):
    number_as_string = str(number) #turn into string for better processing
    addends = [] #create a place to store addends
    decimal_place = -1 #define decimal place as -1 to show that it has not been found
    for index, digit in enumerate(number_as_string * 2): #loop twice, one for finding decimal place, one for assembling addends
        if digit == "." and decimal_place == -1: #check if digit is valid to be decimal point
            decimal_place = index + len(number_as_string) 
        if not digit in [".","0"] and index >= len(number_as_string):
            if index < decimal_place: 
                addends.append(digit + "0" * (decimal_place - index - 1)) #add numbers bigger than one
            else:
                addends.append(digit + "/1" + "0" * (index - decimal_place)) #add numbers lower than one
    output = " + ".join(addends) #join all together with plus sign
    return output
        
def tests():
    assert expanded_form(807.304) == "800 + 7 + 3/10 + 4/1000"
    assert expanded_form(1.24) == "1 + 2/10 + 4/100"
    
    assert expanded_form(807.304) == "800 + 7 + 3/10 + 4/1000"
