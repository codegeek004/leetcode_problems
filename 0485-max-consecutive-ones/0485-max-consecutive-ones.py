class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x =0
        y = 0
        for i in nums:
            if i == 1:
                x+=1
            elif i == 0:
                x=0
            if x>y:
                y=x
        return y



        

    
        