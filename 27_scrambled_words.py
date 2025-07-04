# start: 8:46am 5/7/2025
# end: 9:00 5/7/2025
#  Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
    # scramble('rkqodlw', 'world') ==> True
    # scramble('cedewaraaossoqqyt', 'codewars') ==> True
    # scramble('katas', 'steak') ==> False

def is_scrambled(word1,word2):
    for letter in word2:
        if letter in word1:
            word1.replace(letter,"")
        else:
            return False
    return True
def tests():
    assert is_scrambled("abc","bac") == True
    assert is_scrambled('rkqodlw', 'world') == True
    assert is_scrambled('cedewaraaossoqqyt', 'codewars') == True
    assert is_scrambled('katas', 'steak') == False

if __name__ == "__main__":
    tests()