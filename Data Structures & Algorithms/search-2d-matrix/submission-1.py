class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for r in matrix:
            left = 0
            right = len(r) - 1

            if target == r[left] or target == r[right]:
                return True
            if target > r[right]:
                continue
            if target > r[left] and target < r[right]:

                while left <= right:
                    mid = left + (right - left) // 2

                    if r[mid] == target:
                        return True
                    if r[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
        return False