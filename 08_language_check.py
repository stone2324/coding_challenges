#start: 9:05am 14/6/2025
#end : 9:22am 14/6/2025

# You received a whatsup message from an unknown number. Could it be from that girl/boy with a foreign accent you met yesterday evening?

# Write a simple function to check if the string contains the word hello in different languages.

# These are the languages of the possible people you met the night before:

# hello - english
# ciao - italian
# salut - french
# hallo - german
# hola - spanish
# ahoj - czech republic
# czesc - polish
# Notes

# you can assume the input is a string.
# to keep this a beginner exercise you don't need to check if the greeting is a subset of word (Hallowen can pass the test)
# function should be case insensitive to pass the tests

def validate_hello(message):
    possible_greetings = ['hello','ciao','salut','hallo','hola','ahoj','czesc'] #list all possible languages to loop through
    for item in possible_greetings: #loop through languages
        if item in message.lower(): #check if the message contains a hello in any language
            return True #if the message has hello in, return true
    return False #otherwise, return false

def assertion_tests():
    #these should be right
    assert validate_hello('Hello there!') == True
    assert validate_hello('Ciao bella') == True
    assert validate_hello('halloween') == True
    assert validate_hello('aHoJ') == True

    #these should be false
    assert validate_hello('Good Morning!') == False
    assert validate_hello('how are you!') == False
    assert validate_hello('this is not a greeting') == False
    assert validate_hello('Caio') == False

def main():
    assertion_tests()

if __name__ == "__main__":
    main()
