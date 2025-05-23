class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break
        if index == -1:
            nums.reverse()
        else:
            for i in range(n-1, index, -1):
                if nums[i] > nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    break
            nums[index+1:] = reversed(nums[index+1:])
        print(index)

        