class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # temp = []
        # for i in range(0, len(nums)):
        #     for j in range(1, len(nums)):
        #         for k in range(2, len(nums)):

        #             if i!=j and j!=k and i!=k and nums[i] + nums[j] + nums[k] == 0:
        #                     temp1 = []
        #                     temp1.append(nums[i])
        #                     temp1.append(nums[j])
        #                     temp1.append(nums[k])
        #                     temp1.sort()
        #                     if temp1 not in temp:
        #                         temp.append(temp1)
        # return temp

        Set1=set()
        
        nums.sort()
        
        n=len(nums)
        for i in range(n):
            j=i+1
            k=n-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    Set1.add((nums[i],nums[j],nums[k]))
                    k=k-1
                    j=j+1
                        
                elif sum>0:
                    k=k-1
                    
                else:
                    j=j+1
                    
        return [list(i) for i in Set1]