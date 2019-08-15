class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenght = len(nums)
        currzero = 0
        numszero = 0
        for x in range(lenght):
            if nums[x] == 0:
                currzero = x
                numszero += 1
            elif nums[x] != 0 and numszero > 0:
                pos = currzero - numszero + 1
                nums[pos] = nums[x]
                nums[x] = 0
                currzero += 1


# def moveZeroes(nums):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     lenght = len(nums)
#     currzero = 0
#     numszero = 0
#     for x in range(lenght):
#         if nums[x] == 0:
#             currzero = x
#             numszero += 1
#         elif nums[x] != 0 and numszero > 0:
#             pos = currzero - numszero + 1
#             nums[pos] = nums[x]
#             nums[x] = 0
#             currzero += 1


# nums = [0, 7, 0, 0, 0, 1]
# moveZeroes(nums)
# print(nums)
