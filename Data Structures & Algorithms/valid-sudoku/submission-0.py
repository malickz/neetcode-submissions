from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rcl = defaultdict(set)
        ccl = defaultdict(set)
        bcl = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".":
                    continue
                box_id = (r//3) * 3 + (c//3)
                if val in rcl[r] or val in ccl[c] or val in bcl[box_id]:
                    return False
                rcl[r].add(val)
                ccl[c].add(val)
                bcl[box_id].add(val)
        return True