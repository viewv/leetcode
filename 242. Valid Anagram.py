class Solution(object):
    def isAnagram(self, s, t):
	    return set(s) == set(t) and sum(map(hash, s)) == sum(map(hash, t))
