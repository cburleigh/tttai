import tictactoe
import randomai

def random_versus_random():
    game = tictactoe.TicTacToeBoard()
    player1 = randomai.RandomMoves(1)
    player2 = randomai.RandomMoves(2)
    players = [player1, player2]
    winner = 0
    loser = 0
    while game.check_wins() == 0:
        try:
            player = game.current_player()
            move = players[player-1].move(game.get_board())
            game.move(move)
        except randomai.NoMoveError:
            loser = player
            break
    if game.check_wins() > 0:
        winner = game.check_wins()  
        loser = (winner)%2+1
    return (winner, loser)
    
def main():
    stats = [0,0,0]
    for x in range(100000):
        result = random_versus_random()
        stats[int(result[0])] += 1
    print(f"draws: {str(stats[0])} win1: {str(stats[1])} win2: {str(stats[2])}")

if __name__ == "__main__":
    main()