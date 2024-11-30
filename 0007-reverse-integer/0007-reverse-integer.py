class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = x
        negative = x<0
        int_min = -2**31
        int_max = 2**31 - 1
        reverse = 0
        x = abs(x)
        while(x!=0):

            digit=x%10
            reverse=reverse*10+digit
            x=x//10
            if(reverse>int_max or reverse<int_min):
                return 0
        if negative:
            return -reverse
        return reverse
     