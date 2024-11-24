class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        fibo = [0,1]
        a = 0
        b = 1
        for i in range(0, n):
            sum = a + b
            fibo.append(sum)
            a = b
            b = sum
            i+=1
        print(fibo)
        for j in range(0,n+1):
            print('j:',j)
            if j == n:
                return fibo[j] 
            
        
        return 0

        
        