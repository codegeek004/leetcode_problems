class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp = 0
        for i in nums:
            if count == 0:
                temp = i
            if i == temp:
                count+=1
            else:
                count-=1
        return temp






        