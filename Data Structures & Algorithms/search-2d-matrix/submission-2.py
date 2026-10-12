def searchRow(matrix, target):
    L=0
    R=len(matrix)-1

    while L <= R:
        mid = (L+R)//2
        if mid==R and R==L:
            return mid
        
        if target > matrix[mid][0]:
            L=mid+1
        elif target < matrix[mid][0]:
            R=mid-1
        else:
            return mid
    return -1

def binarySearch(row, target):
    L=0
    R=len(row)-1

    while L <= R:
        mid = (L+R)//2
        if target > row[mid]:
            L=mid+1
        elif target < row[mid]:
            R=mid-1
        else:
            return mid
    return -1

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = searchRow(matrix, target)
        
        m = len(matrix)-1
        
        if (M-1) > m or (M-1) < 0:
            L = -1
        else:
            L = binarySearch(matrix[M-1], target)
            
        if M > m or M < 0:
            mid = -1
        else:
            mid = binarySearch(matrix[M], target)
        
        if (M+1) > m or (M+1) < 0:
            R = -1
        else:
            R = binarySearch(matrix[M+1], target)

        if L != -1:
            return True
        elif mid != -1:
            return True
        elif R != -1:
            return True
        else:
            return False


















        