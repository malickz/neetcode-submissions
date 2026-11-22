from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_count = 0
        for i in nums:
            next_ele = i
            count = 0
            while next_ele in set_nums and i - 1 not in set_nums:
                count += 1
                next_ele = next_ele + 1
                max_count = max(count, max_count)

        return max_count