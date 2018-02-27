class Solution:
    def exist(self, board, word):
        dis=[1,-1,-1,1]
        vlen=len(board)
        wlen=len(board[0])