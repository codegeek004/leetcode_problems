class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverse = 0
        while(x>0):
            #returns the last digit of the number
            digit = x%10
            #for example if the reverse is 121 so here reverse is 0 by definition so 0*10 + digit is 1. It will left shift from the x//10 and it will be until it reaches 0.
            reverse = reverse*10 + digit
            x = x//10
        if temp == reverse:
            return True
        else:
            return False
