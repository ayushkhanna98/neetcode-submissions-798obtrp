class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = self.binrySearchCol(matrix,target)
        print(row)

        return self.binarySearchRow(matrix, row, target)

    

    def binrySearchCol(self, matrix, target):
        e = len(matrix[0]) - 1
        r = len(matrix) - 1
        l = 0

        while l < r:
            mid = (l + r) // 2
            if target <= matrix[mid][e]:
                r = mid 
            else:
                l = mid + 1
        return l
    
    def binarySearchRow(self, matrix, row, target):
        r = len(matrix[row]) - 1
        l = 0
        mid = (l+r)//2
        while l<=r:
            mid = (l+r)//2

            if target < matrix[row][mid]:
                r = mid-1
            elif target > matrix[row][mid]:
                l = mid+1
            else:
                return True
        return False












        