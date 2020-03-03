class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 虽然感觉不是这么个玩法但是是对的
        return sorted(nums)[-1*k]
