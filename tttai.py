import random
import numpy as np

class NoMoveError(RuntimeError):
    pass

class RandomMoves:
    def __init__(self, player):
        moves = [(0,0),(0,1),(0,2),
                    (1,0),(1,1),(1,2),
                    (2,0),(2,1),(2,2)]
        random.shuffle(moves)
        self.moves = iter(moves)
    
    def move(self, board):
        move = next(self.moves)
        try:
            while board[move] != 0:
                move = next(self.moves)
        except StopIteration:
            raise NoMoveError()
        return move

class TabularMoves:
    TRI_DIGITS = (np.ones((3,3))*3)**np.arange(9).reshape(3,3)
    
    def __init__(self, player):
        self.player = player
        self.state_vals = np.zeros(3**9)
    
    def board_to_index(self, board):
        if self.player == 2:
            board = flip_board(board)
        return np.sum(board * TRI_DIGITS)
    
    def find_valid_moves(self,board):
        return board == 0
        
    def find_result_boards(self, board):
        valid_moves = self.find_valid_moves(board)
        num_moves = np.sum(valid_moves)
        result_boards = np.tile(board, (int(num_moves), 1, 1))
        moves = np.where(valid_moves)
        move_indices = (np.arange(num_moves), moves[0], moves[1])
        result_boards[move_indices] = self.player
        return result_boards
        
    def move(self, board):
        pass
        
def flip_board(board):
        return (board%2)+np.minimum(board, 1)