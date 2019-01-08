import numpy as np
import tttai
import tictactoe
import unittest

class TestAIMethods(unittest.TestCase):     

    def test_flip_board(self):
        game = tictactoe.TicTacToeBoard()
        gamemoves = [(0,0), (1,0), (0,1), (1,1), (0,2)]
        for move in gamemoves:
            game.move(move)
        board = game.get_board()
        flipped_board = tttai.flip_board(board)
        self.assertTrue(np.array_equal(np.where(board==1), np.where(flipped_board==2)))
        self.assertTrue(np.array_equal(np.where(board==2), np.where(flipped_board==1)))
        self.assertTrue(np.array_equal(np.where(board==0), np.where(flipped_board==0)))
        
    def test_find_last_move(self):
        game = tictactoe.TicTacToeBoard()
        ai = tttai.TabularMoves(1)
        gamemoves = [(1,1), (2,1), (2,0), (0,2), (2,2), (0,0), (0,1), (1,0)]
        last_space = (1,2)
        for move in gamemoves:
            game.move(move)
        board = game.get_board()
        ai_boards = ai.find_result_boards(board)
        game.move(last_space)
        board = game.get_board()
        self.assertTrue(np.array_equal(ai_boards[0], board))
    
    def test_find_multiple_moves(self):
        board = np.array([[1,0,0],[0,2,0],[0,0,1]])
        ai = tttai.TabularMoves(2)
        boards = np.tile(board, (6, 1, 1))
        available_spaces = [[0,1], [0,2], [1,0], [1,2], [2,0], [2,1]]
        formatted_spaces = (range(len(available_spaces)), [x[0] for x in available_spaces], [x[1] for x in available_spaces])
        boards[formatted_spaces] = 2
        self.assertTrue(np.array_equal(ai.find_result_boards(board), boards))
        
if __name__ == '__main__':
    unittest.main()

