from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix) - 1, -1, -1):
            # print(len(matrix))
            # search = False
            if matrix[i][0] > target:
                continue

            left, right = 0, len(matrix[i]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


sol = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(sol.searchMatrix(matrix, target))

# print("test")
