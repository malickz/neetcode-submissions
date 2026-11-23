class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) and nums[i] != 1:
            i += 1
                
        j = i
        maxzeroes = 0
        while j < len(nums):
            if nums[j] != 1:
                maxzeroes = max(maxzeroes, j - i)
                while j < len(nums) and nums[j] != 1:
                    j += 1
                i = j
            else:
                j += 1
        maxzeroes = max(maxzeroes, j - i)
        
        return maxzeroes
