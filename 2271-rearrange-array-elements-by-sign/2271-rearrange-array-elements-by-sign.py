class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        negative = []
        pos = []
        temp = []
        for i in nums:
            if i<0:
                negative.append(i)
            else:
                pos.append(i)

        i1 = 0
        i2 = 0
        while( i1<len(nums)/2 and i2<len(nums)/2):
            temp.append(pos[i1])
            i1+=1
            temp.append((negative[i2]))
            i2+=1
        print(temp)

        return temp
