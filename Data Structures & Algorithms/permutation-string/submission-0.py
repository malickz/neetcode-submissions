from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_len = len(s1)
        s2_len = len(s2)
        if len(s1) > len(s2):
            return False
        s1_counts = Counter(s1)
        initial_win_counts = Counter(s2[:s1_len])

        if s1_counts == initial_win_counts:
            return True
        print ("s1_counts", s1_counts)
        print("out_initial_win_counts", initial_win_counts)
        for right in range(s1_len, s2_len):
            leftChar = s2[right - s1_len]
            initial_win_counts[leftChar] -= 1
            rightChar = s2[right]
            initial_win_counts[rightChar] += 1

            if initial_win_counts[leftChar] == 0:
                del initial_win_counts[leftChar]
            print("initial_win_counts", initial_win_counts)
            if initial_win_counts == s1_counts:
                return True
            

        return False

