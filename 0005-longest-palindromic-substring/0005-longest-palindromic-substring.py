class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp =''
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                pal = s[i:j]
                if pal==pal[::-1]:
                    if(len(pal)>len(temp)):
                        temp = pal
        return temp
            
                    
                    
                    
                
                    

                