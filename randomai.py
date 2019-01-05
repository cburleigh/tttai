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
        
    def find_valid_moves(self, board):
        valid_moves = board == 0
        num_moves = np.sum(board)
        result_boards = np.tile(board, (num_moves, 1, 1))
        move_indices = (np.arange(num_moves), np.where(valid_moves))
        result_boards[move_indices] = player
        return result_boards
        
    def move(self, board):
        pass
        
        