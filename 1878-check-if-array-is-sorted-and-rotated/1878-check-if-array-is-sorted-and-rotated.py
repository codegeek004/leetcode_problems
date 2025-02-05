class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if nums==sorted(nums): #Already sorted and non-rotated
            return True
        counter = 0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if counter==1 or nums[i]>nums[0]:
                    return False
                counter = 1
            elif counter==1:
                if nums[i]>nums[0]:
                    return False
        return True

                    
        