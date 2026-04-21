class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                pres = board[r][c]
                if pres == ".":
                    continue
                
                if(pres in rows[r] or pres in cols[c] or pres in squares[(r//3,c//3)]):
                    return False
                cols[c].add(pres)
                rows[r].add(pres)
                squares[(r//3, c//3)].add(pres)
        return True