class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum = 0
        maxsum = float('-inf')
        for i in range(len(nums)):
            cursum += nums[i]
            if cursum > maxsum:
                maxsum = cursum
            if cursum < 0:
                cursum = 0
        # if len(nums) == 1:
        #     return nums[0]

        return maxsum
        