# https://leetcode.com/problems/counting-bits/description


def countBits(n: int):
    # Creating an array of 0's
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        # Using even and odd method
        # First the i number is right shifted which makes is half the number
        # For e.g. 4 becomes 2, 7 becomes 3
        # Taking the result of the half and add 1 if it is odd and 0 if it is even
        # For e.g. 2 have single 1's, so 4 will have the same and
        #          3 have double 1's, so 7 will have double 1's plus single 1's, which is triple 1's.
        result[i] = result[i >> 1] + (i & 1)

    return result


print(countBits(n=2))
print(countBits(n=4))
print(countBits(n=7))
print(countBits(n=10))
print(countBits(n=20))
