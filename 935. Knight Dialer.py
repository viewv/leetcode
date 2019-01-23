class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        MOD = 10**9 + 7
        NEIGHBORS_MAP = {
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (3, 9, 0),
            5: tuple(),  # 5 has no neighbors
            6: (1, 7, 0),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4),
            0: (4, 6),
        }
        dp = [1 for x in range(0, 10)]
        for _ in range(N - 1):
            temp = [0 for x in range(0, 10)]
            for n, count in enumerate(dp):
                for nxt in NEIGHBORS_MAP[n]:
                    temp[nxt] += count
            dp = [i % MOD for i in temp]
        return sum(dp) % MOD
