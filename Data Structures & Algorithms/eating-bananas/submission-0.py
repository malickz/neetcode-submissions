class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slow = 1
        fastest = max(piles)
        
        while slow <= fastest:
            mid = (slow + fastest) // 2
            
            hours = 0
            
            for pile in piles:
                hours += math.ceil(pile/mid)
            
            if hours <= h:
                fastest = mid - 1 # Speed works; try a slower speed
            else:
                slow = mid + 1
            
        return slow