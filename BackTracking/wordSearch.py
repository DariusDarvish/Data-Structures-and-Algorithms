class Solution:
    def __init__(self):
        pass

    def exist(self, board: list[list[str]], word: str) -> bool:
        rows,columns=len(board),len(board[0])
        visited=set()
        def dfs(row,column,index):
            nonlocal word
            nonlocal visited
            nonlocal board
            nonlocal rows
            nonlocal columns
            directions=[(1,0),(0,1),(0,-1),(-1,0)]
            if index==len(word)-1:
                return True
            
            visited.add((row,column))
            for direction in directions:
                new_row=row+direction[0]
                new_column=column+direction[1]
                if 0<=new_row<rows\
                and 0<=new_column<columns\
                and (new_row,new_column) not in visited\
                and board[new_row][new_column]==word[index+1]:
                    if dfs(new_row,new_column,index+1):
                        return True
            visited.remove((row,column))
            return False
        
        for row in range(rows):
            for column in range(columns):
                if board[row][column]==word[0]:
                    end_value=dfs(row,column,0)
                    if end_value:
                        return True
        return False

solutions = Solution()
print(solutions.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],word="ABCCED"))