class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum = 0
        #float('-inf') sets the value to the smallest number. If we initialize it with zero then it will give output as 0 even if the output should be negative in case of negative valued arrays
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
        