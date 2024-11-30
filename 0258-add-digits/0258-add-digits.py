
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # value = 0
        # while(num!=0):
        #     digit=num%10
        #     value = digit+value
        #     num = num//10
        # value1 = 0
        # print(value)
        # if value>9:
        #     value1=value%10+value//10
        #     print(value1)
        #     return value1
        # return value
        while(num>9):
            num=num%10+num//10
        return num
            
        