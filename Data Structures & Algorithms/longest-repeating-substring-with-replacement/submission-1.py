class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        freq = {}

        max_len = 0
        win_max = 0

        while j < len(s):
            freq[s[j]] = freq.get(s[j], 0) + 1
            win_max = max(win_max, freq[s[j]])

            while (j - i + 1) - win_max > k:
                freq[s[i]] = freq[s[i]] - 1
                i += 1
            max_len = max(max_len, (j - i + 1))
            j += 1
        return max_len

