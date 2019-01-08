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
        self.exploration_ratio = 0.5
    
    def find_valid_moves(self,board):
        return board == 0
        
    def find_result_boards(self, board, player):
        valid_moves = self.find_valid_moves(board)
        num_moves = np.sum(valid_moves)
        result_boards = np.tile(board, (int(num_moves), 1, 1))
        moves = np.where(valid_moves)
        move_indices = (np.arange(num_moves), moves[0], moves[1])
        result_boards[move_indices] = player
        return result_boards
    
    def convert_indices(self, states):
        return np.sum(states * self.TRI_DIGITS, (1,2))
    
    def move(self, board):
        if self.player == 2:
            board = flip_board(board)
        moves = np.where(self.find_valid_moves(board))
        result_states = self.find_result_boards(board, 1)
        indices = self.convert_indices(result_states)
        state_values = self.state_vals[indices]
        max_index = np.argmax(state_values)
        if random.random() < self.exploration_ratio:
            move_index = random.randint(0, len(moves[0])
        else:
            move_index = max_index
        return (moves[0][move_index], moves[1][move_index]
        #untested
        
def flip_board(board):
        return (board%2)+np.minimum(board, 1)