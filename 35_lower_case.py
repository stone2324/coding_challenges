# The borrowers are tiny tiny fictional people. As tiny tiny people they have to be sure they aren't spotted, or more importantly, stepped on.

# As a result, the borrowers talk very very quietly. They find that capitals and punctuation of any sort lead them to raise their voices and put them in danger.

# The young borrowers have begged their parents to stop using caps and punctuation.

# Change the input text s to new borrower speak. Help save the next generation!

def borrower(string):
    lower_string = string.lower()
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in punctuation:
        lower_string = lower_string.replace(char, '')
    
    return lower_string

def tests():
    assert borrower("Hello, World!") == "hello world"
    assert borrower("The Borrowers are tiny tiny people.") == "the borrowers are tiny tiny people"
    assert borrower("No Punctuation Here") == "no punctuation here"
    assert borrower("Caps and Punctuation!") == "caps and punctuation"
    assert borrower("Tiny People, Big Dreams.") == "tiny people big dreams"
    print("All tests passed")

if __name__ == "__main__":
    tests()