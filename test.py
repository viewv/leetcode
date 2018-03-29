class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        total_count = 1
        for i in range(len(s) - 1):
            stack = []
            stack.append(s[i])
            count = 1
            for j in s[i+1:]:
                if j in stack:
                    break
                else:
                    stack.append(j)
                    if count == 94:
                        return 95
                    else:
                        count += 1
            if total_count < count:
                total_count = count
        return total_count
