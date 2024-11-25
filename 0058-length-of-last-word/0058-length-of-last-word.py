class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = s.strip()
        num1 = s.split()
        length = num1[-1]
        return len(length)
        