# start: 3:05 29/6/2025
# end: 3:25 29/6/2025
# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.


def increment_string(s):
    digits = "0123456789"
    split_index = len(s)

    for i in range(len(s) - 1, -1, -1):  # Loop backward using a for loop
        if s[i] in digits:
            split_index = i
        else:
            break
    text_part = s[:split_index]
    number_part = s[split_index:]
    if number_part == "":
        return s + "1"
    number_value = int(number_part)
    incremented = str(number_value + 1)
    while len(incremented) < len(number_part):
        incremented = "0" + incremented
    return text_part + incremented

def tests():
    assert increment_string("foo") == "foo1"
    assert increment_string("bar007") == "bar008"
    assert increment_string("item099") == "item100"
    assert increment_string("") == "1"

if __name__ == "__main__":
    tests()
