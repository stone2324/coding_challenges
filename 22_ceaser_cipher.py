# start: 8:10pm 26/6/2025
# end: 8:39pm 26/6/2025
#  ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
# ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.


def rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"  # repeat aplhabet twice for lowercase and uppercase so there are enough characters
    message_array = [
        letter for letter in message
    ]  # create array of message so it can be changed
    for message_index, message_letter in enumerate(
        message_array
    ):  # loop through the message
        for index, letter in enumerate(
            alphabet
        ):  # check if the letter matches the aplhabet
            if letter == message_letter:
                message_array[message_index] = alphabet[
                    index + 13
                ]  # add 13 to index fo a rot13 encription
                break  # get out of loop befor the letter gets changed again
    return "".join(message_array)


def tests():
    assert rot13("test") == "grfg"
    assert rot13("Test") == "Grfg"
    assert rot13("This is a Test for casing, numbers -> 123456789, and special characters -> +=_-!@#$%^&*()") == "Guvf vf n Grfg sbe pnfvat, ahzoref -> 123456789, naq fcrpvny punenpgref -> +=_-!@#$%^&*()"
    
if __name__ == "__main__":
    tests()
    print("All tests passed :D")

