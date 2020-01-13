class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        l = len(str(low))
        r = len(str(high))
        ans = []
        for x in range(l, r + 1):
            t = 9 - x
            for i in range(0, t + 1):
                temp = nums[i: i + x]
                temp = int(''.join(temp))
                if temp > high:
                    break
                elif temp < low:
                    continue
                else:
                    ans.append(temp)
        return sorted(ans)
