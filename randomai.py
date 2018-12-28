import random

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
    