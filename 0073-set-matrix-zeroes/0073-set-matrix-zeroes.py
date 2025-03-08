class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rowset = set()
        colset = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowset.add(i)
                    colset.add(j)
        
        for row in rowset:
            for j in range(cols):
                matrix[row][j] = 0
        for col in colset:
            for i in range(rows):
                matrix[i][col] = 0