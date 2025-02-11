class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # count=0
        # print(len(nums))
        # for i in range(len(nums)):
        #     subarray_sum = 0
        #     for j in range(i, len(nums)):
        #         #brute force (time limit exceeded)
        #         # subarray_sum = sum(nums[i:j+1])
        #         # subarray_sum += nums[j]
        #         if subarray_sum == k:
        #             count+=1
        # return count


        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return(count)


        