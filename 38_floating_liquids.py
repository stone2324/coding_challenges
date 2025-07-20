# start: 8:56am 21/7/2025
# end: 9:24am 21/7/2025
#  Don't Drink the Water

# Given a two-dimensional array representation of a glass of mixed liquids, sort the array such that the liquids appear in the glass based on their density. (Lower density floats to the top) The width of the glass will not change from top to bottom.

# ======================
# |   Density Chart    |
# ======================
# | Honey   | H | 1.36 |
# | Water   | W | 1.00 |
# | Alcohol | A | 0.87 |
# | Oil     | O | 0.80 |
# ----------------------

# {                             {
#   { 'H', 'H', 'W', 'O' },        { 'O','O','O','O' },
#   { 'W', 'W', 'O', 'W' },  =>    { 'W','W','W','W' },
#   { 'H', 'H', 'O', 'O' }         { 'H','H','H','H' }
# }                             }

# The glass representation may be larger or smaller. If a liquid doesn't fill a row, it floats to the top and to the left.


def separate_liquids(glass):
    # oil floats at the top, then alchohol, water, and honey
    float_map = {"O": 1, "A": 2, "W": 3, "H": 4, 1: "O", 2: "A", 3: "W", 4: "H"}

    rows = len(glass)
    row_length = len(glass[0]) if rows > 0 else 0
    all_liquids = []
    for row in glass:
        for item in row:
            all_liquids.append(float_map[item])
    # Sort in density order
    all_liquids.sort()
    output = []
    for row_num in range(rows):
        output.append(
            [
                float_map[density_num]
                for density_num in all_liquids[
                    row_num * row_length : (row_num + 1) * row_length
                ]
            ]
        )
    return output


def tests():
    assert separate_liquids(
        [["H", "H", "W", "O"], ["W", "W", "O", "W"], ["H", "H", "O", "O"]]
    ) == [["O", "O", "O", "O"], ["W", "W", "W", "W"], ["H", "H", "H", "H"]]

    assert separate_liquids([["H", "W"], ["A", "O"]]) == [["O", "A"], ["W", "H"]]

    assert separate_liquids([["H"]]) == [["H"]]

    assert separate_liquids([]) == []

    print("All tests passed")


if __name__ == "__main__":
    tests()
