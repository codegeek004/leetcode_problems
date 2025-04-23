class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            print(nums[i])
            if target == nums[i]:
                print('if mua gaya')
                output = index(i)
                break
            else:
                output = -1
            i += 1
        print(output)
        return output

        