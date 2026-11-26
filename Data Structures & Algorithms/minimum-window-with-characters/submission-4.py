import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for i in range(len(t)):
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1

        freq_s = {}

        i = 0
        formed = 0
        min_len = math.inf
        left = 0
        right = 0
        for j in range(len(s)):
            freq_s[s[j]] = freq_s.get(s[j], 0) + 1

            if s[j] in freq_t and freq_s[s[j]] == freq_t[s[j]]:
                formed += 1
            
            while formed == len(freq_t) and i <= j:
                leftChar = s[i]
                freq_s[leftChar] -= 1

                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    left = i
                    right = j

                if leftChar in freq_t and freq_s[leftChar] < freq_t[leftChar]:
                    formed -= 1

                i += 1

        return s[left:right + 1] if min_len != math.inf else ""
