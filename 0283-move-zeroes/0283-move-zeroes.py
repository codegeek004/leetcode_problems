class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == 0:
                    x.append(nums[i])
                    nums.pop(i)
        for i in x:
            nums.append(i)

        