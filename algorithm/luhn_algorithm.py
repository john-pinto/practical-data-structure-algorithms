"""
Wikepedia link for the algorithm: https://en.wikipedia.org/wiki/Luhn_algorithm#cite_note-6

Planning and refactoring:
    1. Creating a function that verifies a given string of digits.
    2. The last digit, this digit is for digit validation.
    3. Initially reverse the digits, double the every second digit starting from the second digit because the first is check digit.
    4. Getting the sum of all the numbers and modifying the doubled numbers by increment of initial digit (eg. 14 -> 1 + 14 = 15)
    6. Now taking the total and applying mod 10 should give 0 as result, if not then the digits are wrong.
    7. Including lookup table for quick reference for the doubling digits and increment that are more than 9.
"""

LOOKUPS = (
    # This stay the same, multipy of 1
    dict(zip("0123456789", (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))),
    # These are doubled and reduced to single digit. eg. 10 -> 1 + 0 = 1
    dict(zip("0123456789", (0, 2, 4, 6, 8, 1, 3, 5, 7, 9))),
)


def luhn_algo_verify_digit(digits):
    total = 0
    for i, d in enumerate(reversed(digits)):
        # # Without a Lookup table
        # x = int(d) * (1 + i % 2)
        # total += x // 10 + x
        total += LOOKUPS[i % 2][d]
    return total % 10 == 0


def functional_luhn(digits):
    return sum(LOOKUPS[i % 2][d] for i, d in enumerate(reversed(digits))) % 10 == 0


if __name__ == "__main__":
    assert luhn_algo_verify_digit("17893729974")
    assert not luhn_algo_verify_digit("17893729976")
    assert functional_luhn("17893729974")
    assert not functional_luhn("17893729976")
    print("Success")
