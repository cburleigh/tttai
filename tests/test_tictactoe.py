import numpy as np
import tictactoe
import unittest

class TestTicTacToeBoard(unittest.TestCase):     

    def test_board_starts_empty(self):
        board = tictactoe.TicTacToeBoard()
        self.assertTrue(np.equal(board.get_board(), np.zeros((3,3))).all())
        
    def test_win(self):
        board = tictactoe.TicTacToeBoard()
        firstplayer = board.current_player()
        gamemoves = [(0,0), (1,0), (0,1), (1,1), (0,2)]
        for move in gamemoves:
            board.move(move)
        self.assertEqual(board.get_winner(), firstplayer)
        
    def test_repeat_move(self):
        board = tictactoe.TicTacToeBoard()
        board.move((0,0))
        with self.assertRaises(ValueError):
            board.move((0,0))
    
    def test_out_of_bounds(self):
        board = tictactoe.TicTacToeBoard()      
        with self.assertRaises(IndexError):
            board.move((0,3))
    
    def test_game_over(self):
        board = tictactoe.TicTacToeBoard()
        gamemoves = [(0,0), (1,0), (0,1), (1,1), (0,2), (1,2)]
        with self.assertRaises(tictactoe.GameOver):
            for move in gamemoves:
                board.move(move)
    
    def test_draw(self):
        board = tictactoe.TicTacToeBoard()
        drawcode = 0
        gamemoves = [(1,1), (2,1), (2,0), (0,2), (2,2), (0,0), (0,1), (1,0), (1,2)]
        for move in gamemoves:
            board.move(move)
        self.assertEqual(board.get_winner(), drawcode)
        
    def test_twoline_win(self):
        board = tictactoe.TicTacToeBoard()
        firstplayer = board.current_player()
        gamemoves = [(0,0), (1,0), (1,1), (2,0), (0,2), (2,1), (1,2), (0,1), (2,2)]
        for move in gamemoves:
            board.move(move)
        self.assertEqual(board.get_winner(), firstplayer)
        
    def test_game_in_progress(self):
        board = tictactoe.TicTacToeBoard()
        unresolved_code = -1
        firstplayer = board.current_player()
        gamemoves = [(0,0), (1,0), (1,1), (2,0)]
        for move in gamemoves:
            board.move(move)
        self.assertEqual(board.get_winner(), unresolved_code)
        
    def test_history(self):
        board = tictactoe.TicTacToeBoard()
        gamemoves1 = [(1,1), (2,1), (2,0), (0,2)]
        gamemoves2 = [(2,2), (0,0), (0,1), (1,0), (1,2)]
        for move in gamemoves1:
            board.move(move)
        self.assertEqual(board.get_history(), gamemoves1)
        for move in gamemoves2:
            board.move(move)
        self.assertEqual(board.get_history(), gamemoves1+gamemoves2)
        
if __name__ == '__main__':
    unittest.main()

