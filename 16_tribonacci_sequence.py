# start :6:36am 20/6/2025
# end: 6:47am 20/6/2025
# Well met with Fibonacci bigger brother, AKA Tribonacci.

# As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

# [1, 1 ,1, 3, 5, 9, 17, 31, ...]

# But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

# Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

# Signature will always contain 3 numbers; n will always be a non-negative number and represents how much items to output; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

def tribonacci(signature, output_digits):
    if output_digits == 0:
        return [] # Return an empty list if output_digits is 0
    elif output_digits <= 3:
        return signature[0:output_digits] # Return the signature if output_digits is 1, 2, or 3
    
    tribonacci_sequence = signature # Create output list starting with the signature
    
    for i in range(3, output_digits):
        next_value = tribonacci_sequence[i-1] + tribonacci_sequence[i-2] + tribonacci_sequence[i-3] # Add the last three numbers to get the next value
        tribonacci_sequence.append(next_value) #add the next value to the sequence
    
    return tribonacci_sequence # Return the complete tribonacci sequence

def asssertion_tests():
    assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    assert tribonacci([0, 0, 1], 10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    assert tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44,81]
    assert tribonacci([1, 2, 3], 5) == [1, 2, 3, 6, 11]
    assert tribonacci([0.5, -0.5, -0.5], 6) == [0.5, -0.5, -0.5, -0.5, -1.5, -2.5]
    assert tribonacci([1, 2, 3], 0) == []
    assert tribonacci([1, 2, 3], 1) == [1]

def main():
    asssertion_tests()
    
if __name__ == "__main__":
    main()
    
