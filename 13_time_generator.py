# start: 6:36am 17/6/2025
# end : 7:05am 17/6/2025
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.


def convert_seconds(seconds):
    hours = int((seconds - (seconds % 3600)) / 3600)
    minutes = int((seconds - (seconds % 60)) / 60) % 60
    seconds = seconds % 60
    if hours < 10:
        hours = "0" + str(hours)
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    return str(hours) + ":" + str(minutes) + ":" + str(seconds)


def assertion_test():
    assert convert_seconds(0) == "00:00:00"
    assert convert_seconds(59) == "00:00:59"
    assert convert_seconds(60) == "00:01:00"
    assert convert_seconds(3599) == "00:59:59"
    assert convert_seconds(3600) == "01:00:00"
    assert convert_seconds(359999) == "99:59:59"


def main():
    assertion_test()


if __name__ == "__main__":
    main()
