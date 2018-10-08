class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        length = len(dominoes)
        Force = [0 for x in range(0, length)]
        forceRight = forceLeft = 0
        dominoes = list(dominoes)
        for x in range(0, length):
            if dominoes[x] == 'R':
                forceRight += 1
            Force[x] += forceRight
        for x in range(length - 1, -1, -1):
            if dominoes[x] == 'L':
                forceLeft += 1
            Force[x] -= forceLeft
        for x in range(0, length):
            if Force[x] > 0:
                dominoes[x] = 'R'
            elif Force[x] == 0:
                dominoes[x] = '.'
            else:
                dominoes[x] = 'L'
        return str(dominoes)
