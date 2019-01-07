import numpy as np
import itertools

class GameOver(Exception):
    pass

class TicTacToeBoard:
    def __init__(self):
        self.board = np.zeros((3,3))
        self.turns = itertools.cycle([1,2])
        self.turn = next(self.turns)
        self.over = False
        self.winner = 0
        self.history = []
        
    def current_player(self):
        return self.turn
    
    def get_board(self):
        return self.board.copy()
    
    def move(self, pos):
        if(self.over):
            raise GameOver("game is over")
        if(self.board[pos] == 0):
            self.board[pos] = self.turn
            self.turn = next(self.turns)
            status = self.__check_wins()
            if status >= 0:
                self.over = True
                self.winner = status
            self.history.append(pos)
        else:
            raise ValueError("tile " + str(pos) + " is already occupied")
    
    def get_winner(self):
        if self.over:
            return self.winner
        else:
            return -1
            
    def get_history(self):
        return self.history
    
    def __check_wins(self):
        lines = np.vstack((self.board, self.board.transpose(), self.board.diagonal(), np.fliplr(self.board).diagonal()))
        complete_mask = np.logical_and(lines[:, 0] != 0, np.all(lines.transpose() == lines[:, 0], axis = 0))
        complete_lines = lines[:, 0][complete_mask]
        if len(complete_lines) == 0:
            if(0 in self.board):
                return -1
            else:
                return 0
        elif np.all(complete_lines == complete_lines[0]):
            return complete_lines[0]
        else:
            raise RuntimeError("invalid game state")