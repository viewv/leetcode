class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        length = len(nums)
        coin = 0
        maxcoin = 0

        def helper(ns, l, coin):
            nonlocal maxcoin
            if l == 0:
                if coin > maxcoin:
                    maxcoin = coin
                return
            for x in range(l):
                b = ns[x]
                if x == 0:
                    a = 1
                else:
                    a = ns[x-1]
                if x == l - 1:
                    c = 1
                else:
                    c = ns[x + 1]
                coin += a * b * c
                temp = ns.pop(x)
                helper(ns, l - 1, coin)
                ns.insert(x, temp)
                coin -= a * b * c
            return
        helper(nums, length, coin)
        return maxcoin
