class Solution:
    def isPowerOfFour(self, num):
        return bool(num == (num & -num) and num.bit_length() % 2)
