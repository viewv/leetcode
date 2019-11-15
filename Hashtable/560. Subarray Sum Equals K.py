class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        waitnum = {0: 1}
        tempsum = 0
        ans = 0
        for i, c in enumerate(nums):
            tempsum += c
            if tempsum in waitnum:
                waitnum[tempsum] += 1
            else:
                waitnum[tempsum] = 1
            if tempsum - k in waitnum:
                ans += waitnum[tempsum - k]
        return ans
