from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = dict.fromkeys(words, 0)
        for x in words:
            d[x] -= 1
        l = list(d.items())
        l = sorted(l, key=lambda x: (x[1], x[0]))
        l = [x[0] for x in l[:k]]
        return l


sol = Solution()
word = ["i", "love", "leetcode", "i", "love", "coding"]

l = sol.topKFrequent(word, 2)
print(l)
