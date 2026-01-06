# https://leetcode.com/problems/sum-of-two-integers/description/


def getSum(a: int, b: int) -> int:
    carry = 0

    while b != 0:
        # On calculating using and operator a carry will be resulted
        carry = a & b

        # Using xor operator result is calculated without carry
        a = a ^ b

        # shifting the carry makes it valid and ready for xor again, until it reaches 0
        b = carry << 1

    return a

print(getSum(a=-1, b=1))
print(getSum(a=1, b=2))
print(getSum(a=2, b=3))
print(getSum(a=100, b=99))
print(getSum(a=999999999, b=9999))
