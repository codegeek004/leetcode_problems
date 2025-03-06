class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        mx=0
        for i in s:
            if i-1 not in s:
                length=1
                while i+length in s:
                    length+=1
                mx=max(mx,length)
        return mx