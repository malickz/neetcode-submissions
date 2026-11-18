class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = {}
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            key = tuple(counts)
            freq_dict.setdefault(key, []).append(s)
        
        return list(freq_dict.values())

