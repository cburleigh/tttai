import timing
import tictactoe

def main():
	print("running 100k games")
	for x in range(100000):
		playdraw()
	
def playdraw():
	board = tictactoe.TicTacToeBoard()
	gamemoves = [(1,1), (2,1), (2,0), (0,2), (2,2), (0,0), (0,1), (1,0), (1,2)]
	for move in gamemoves:
			board.move(move)

if __name__ == "__main__":
    main()