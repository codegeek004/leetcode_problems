class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) + 1
        list1 = sorted(nums)
        print(list1)
        for i in range(length):
            if i not in list1:
                return i


        