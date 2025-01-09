class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:

            # if target == 0:
            #     return nums.index(i)
            if target == i:
                print('index',nums.index(i))
                return nums.index(i)
            elif target not in nums:
                nums.append(target)
                nums.sort()
                print('nums',nums)
                return nums.index(target)


        