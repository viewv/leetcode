class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for x in nums:
            xor ^= x
        xor = xor & ~(xor - 1)
        a, b = 0, 0
        for x in nums:
            if (x & xor):
                a ^= x
            else:
                b ^= x
        return [a, b]
