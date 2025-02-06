class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x =[]
        n = len(nums)
        k = k%n
        count = k

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        
        # for i in range(len(nums)-1, -1, -1):          
        #     print('i', i)
        #     if len(nums) <= 1:
        #         return nums[i]
        #     if count > 0:
        #         x.append(nums[i])
        #         count = count -1
        #         nums.pop(i)
        # x.sort()
       
        # for j in range(0, len(nums)):
        #     if j < len(x):
        #         print("nums[j]", x[j])
        #         nums.insert(j, x[j])
        #         j+=1
        
        



            








        