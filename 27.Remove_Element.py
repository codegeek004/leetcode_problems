class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x = 0
        for y in range(len(nums)):
            if nums[y] != val:
                #add all the values which are not equal to val to the new array x.
                nums[x] = nums[y]
                
                x += 1

        return x
