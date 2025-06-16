# start : 8:35am 15/6/2025
# end : 9:14am 15/6/2025
# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of 'abad' is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.


def find_highscore_word(input_word):
    #establish variables
    word_list = []
    score_list = []
    current_score = 0
    current_word = ""
    high_score = 0
    high_score_word = ""
    for letter in input_word + " ":
        if letter == " ":
            #add word and scores to lists when seperated by space
            word_list.append(current_word)
            score_list.append(current_score)
            #reset word and score to avoid mis-scoring
            current_word = ""
            current_score = 0
        else:
            #build word letter by letter
            current_word += letter
            for score_allocate, char in enumerate(" abcdefghijklmnopqrstuvwxyz"): #allocate score by position in alphabet
                if char == letter:
                    current_score += score_allocate #add letter score to the score 
                    break

    for word_num, word_score in enumerate(score_list): #find the highest scoring word in the score list
        if word_score > high_score:
            high_score = word_score
            high_score_word = word_list[word_num]
    return high_score_word

def assertion_tests():
    assert find_highscore_word('a aa') == 'aa' #test for larger length of same letter
    assert find_highscore_word('abc def') == 'def' #test for larger value
    assert find_highscore_word('bat tab') == 'bat' #test for same value but different position
    assert find_highscore_word('thank you for the food') == 'thank' #test for larger conbinations
    assert find_highscore_word('a b c d e f g h i j k l m n o p q r s t u v w y y z') == 'z' #test all letters

def main():
    assertion_tests()

if __name__ == '__main__':
    main()