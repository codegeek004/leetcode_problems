class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        mismatch = []
        for i in range(len(heights)):
            for j in range(len(expected)):
                if i==j:
                    if heights[i] != expected[j]:
                        x = heights[i]
                        mismatch.append(x)
        print(mismatch)
        return len(mismatch)
                        
        
                
        