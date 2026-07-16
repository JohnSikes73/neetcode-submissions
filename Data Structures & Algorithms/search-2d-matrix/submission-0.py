class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)

        def matrix_map(k):
            i = k // m
            j = k - (i * m)
            return matrix[i][j]

        left = 0
        right = m*n - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_elt = matrix_map(mid)
            if target == mid_elt:
                return True
            elif target < mid_elt:
                right = mid - 1
            else:
                left = mid + 1
            
        return False