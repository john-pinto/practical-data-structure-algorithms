# https://leetcode.com/problems/number-of-1-bits/description


def hammingWeight(n: int) -> int:
    result = 0

    # Numbers of bits in int
    for i in range(32):
        # Shifting to right and using the last bit with
        # and operator to check whther it is 1 or 0
        if (n >> i) & 1:
            result += 1

    return result


print(hammingWeight(n=11))
print(hammingWeight(n=128))
print(hammingWeight(n=2147483645))
