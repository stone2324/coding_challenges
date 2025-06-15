# start: 6:50 16/6/2025
# end: 7:10 16/6/2025
# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
#
#   " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
#   "    Hello     World   "                  =>  "#HelloWorld"
#   ""                                        =>  false


def generate_hashtag(message):
    if len(message) > 140 or len(message) == 0:
        return False
    words = message.split(" ")
    for word in words:
        for letter in word:
            if letter == " ":
                words.remove(" ")
    output_message = "#"
    for item in words:
        output_message += item.capitalize()
    return output_message


def assertion_tests():
    assert generate_hashtag("hello there") == "#HelloThere"  # test for basic case
    assert generate_hashtag("hello     ") == "#Hello"  # test for trailing spaces
    assert generate_hashtag("     hello") == "#Hello"  # test for leading spaces
    assert generate_hashtag("hElLo ThErE") == "#HelloThere"  # test only the first letter capatilized


def main():
    assertion_tests()


if __name__ == "__main__":
    main()
