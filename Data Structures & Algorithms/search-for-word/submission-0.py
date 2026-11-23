class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]

        def back(i, x, y):
            if i == len(word):
                return True
            if not (0 <= x < rows and 0 <= y < cols) or board[x][y] != word[i]:
                return False
            tmp, board[x][y] = board[x][y], "#"   # mark visited
            found = any(back(i + 1, x + dx, y + dy) for dx, dy in dirs)
            board[x][y] = tmp                      # un-mark (backtrack)
            return found

        return any(back(0, r, c) for r in range(rows) for c in range(cols))
        