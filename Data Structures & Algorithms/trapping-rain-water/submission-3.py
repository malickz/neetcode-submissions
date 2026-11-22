class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        max_water = 0
        leftmax = [0] * n # prefix left max
        rightmax = [0] * n # suffix right max

        leftmax[0] = height[0] # nothing on left of 0
        for i in range(1, n):
            leftmax[i] = max(leftmax[i - 1], height[i]) # am i the max so far or have we seen on left and updated the index before me
        rightmax[n - 1] = height[n - 1]# nothing on right of n - 1
        for i in range(n - 2, -1, -1):
            rightmax[i] = max(height[i], rightmax[i + 1])# am i the max so far or have we seen on irght and updated the index after me

        for i in range(len(height)):
            max_water += min(leftmax[i], rightmax[i]) - height[i]

        return max_water
