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
		
	def current_player(self):
		return self.turn
	
	def get_board(self):
		return self.board.copy()
	
	def move(self, pos):
		if(self.over):
			raise GameOver('game is over')
		if(self.board[pos] == 0):
			self.board[pos] = self.turn
			self.turn = next(self.turns)
			if self.check_wins() != 0:
				self.over = True
		else:
			raise ValueError('tile ' + str(pos) + ' is already occupied')
			
	def check_wins(self):
		lines = []
		for row in range(3):
			lines.append(self.board[row, :])
		for col in range(3):
			lines.append(self.board[:, col])
		lines.append(self.board.diagonal())
		lines.append(np.fliplr(self.board).diagonal())
		complete_lines = []
		for line in lines:
			if (line[0] != 0) and (line == line[0]).all():
				complete_lines.append(line[0])
		if len(complete_lines) == 0:
			if(0 in self.board):
				return 0
			else:
				return -1
		elif len(complete_lines) == 1:
			return complete_lines[0]
		else:
			raise RunTimeError('invalid game state')