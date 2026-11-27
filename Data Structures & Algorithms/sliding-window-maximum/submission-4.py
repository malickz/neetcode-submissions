class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        stack = []
        for i in range(0, k):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)

        res.append(nums[stack[0]])
        
        for j in range(k, len(nums)):
            if stack[0] < j - k + 1: # if its outside the start of window
                stack.pop(0)
            while stack and nums[stack[-1]] < nums[j]:
                stack.pop()
            stack.append(j)
            
            res.append(nums[stack[0]])
        print(stack)
        return res