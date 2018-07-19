num = [2, 3, 1, 1, 4]

def maxforword(a, nums):
    step = nums[a]
    return max(nums[a + 1:a+step])


def jump(nums):
    x = 0
    count = 0
    Length = len(nums)
    while x + maxforword(x, nums) <= Length:
        for y in range(x + 1, x + nums[x]):
            if y == maxforword(x, nums):
                x = y
                break
        count += 1
    return count


print(jump(num))
