class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        set1 = set()
        for num in arr:
            if num*2 in set1 or (num%2==0 and num/2 in set1):
                return True
            set1.add(num)
        return False