class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = []
        # i=1

        full_list = [i for i in range(1, len(nums)+1)]
        return list(set(full_list) - set(nums))