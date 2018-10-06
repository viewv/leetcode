class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if not letters:
            return ''
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
