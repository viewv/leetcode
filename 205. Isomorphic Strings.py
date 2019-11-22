class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dstot = {}
        dttos = {}
        l = len(s)
        for x in range(l):
            if s[x] in dstot and t[x] in dttos:
                if dstot[s[x]] != t[x] or dttos[t[x]] != s[x]:
                    return False
            elif s[x] in dstot and t[x] not in dttos:
                return False
            elif s[x] not in dstot and t[x] in dttos:
                return False
            else:
                dstot[s[x]] = t[x]
                dttos[t[x]] = s[x]
        return True
