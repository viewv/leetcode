class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dic = {}
        countA = 0
        setA = set()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                countA += 1
                setA.add(i)
            elif secret[i] not in dic:
                dic[secret[i]] = 1
            else:
                dic[secret[i]] += 1
        countB = 0
        for i in range(len(guess)):
            if i not in setA:
                if guess[i] in dic:
                    countB += 1
                    dic[guess[i]] -= 1
                    if dic[guess[i]] == 0:
                        del dic[guess[i]]
        return str(countA)+"A"+str(countB)+"B"
