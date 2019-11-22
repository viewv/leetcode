class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n != 0:
            r = (n-1) % 26
            ans.append(chr(65 + r))
            n = (n-1) // 26
        return ''.join(ans[::-1])
