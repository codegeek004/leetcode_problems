class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            x = i
            y = nums.count(x)
            if y<2:
                return x


        