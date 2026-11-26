import math
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        i, j = 0, 0
        seen = {}
        while j < len(s):
            if s[j] in seen and seen[s[j]] >= i:
                i = seen[s[j]] + 1    


            seen[s[j]] = j
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len