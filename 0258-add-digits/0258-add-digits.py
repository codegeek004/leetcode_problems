
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while(num>9):
            num=num%10+num//10
        return num
            
        