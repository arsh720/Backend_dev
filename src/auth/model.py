class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        import math
        #length at a point is 4*m+n
        m=len(matrix)
        n=len(matrix[0])
        right =m*n -1
        left=0
        mid=(left+right)//2
        if target>matrix[m-1][n-1] or target<matrix[0][0]:
            return False
        
        def bin(matrix,target,left,right):
            mid=(left+right)//2
            row=mid//n
            col=mid%n
            if matrix[row][col]== target:
                return True
            if matrix[row][col] > target:
                right=mid-1
                return bin(matrix,target,left,right)
            if matrix[row][col]<target:
                left=mid+1
                return bin(matrix,target,left,right)
            return False
        bin(matrix,target,left,right)


        
        
        
        

        