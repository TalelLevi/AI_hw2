from MapsGenerator import ai_board
import numpy as np
from MinimaxPlayer import MinimaxPlayer as Player1
from AlphaBetaPlayer import AlphaBetaPlayer as Player2
from OrderedAlphaBetaPlayer import OrderedAlphaBetaPlayer as Player3
from ContestPlayer import ContestPlayer as Player4
import matplotlib.pyplot as plt

minimax_times = []
minimax_depths = []
alphabeta_times = []
alphabeta_depths = []
ordered_times = []
ordered_depths = []
contest_time = []
contest_depth = []

for t in np.linspace(0.1, 3, 50):
    # player1 = Player1()
    # player2 = Player2()
    player3 = Player3()
    player4 = Player4()
    # player1.set_game_params(ai_board.copy())
    # player2.set_game_params(ai_board.copy())
    player3.set_game_params(ai_board.copy())
    # d1 = player1.make_move(t)
    # d2 = player2.make_move(t)
    d3 = player3.make_move(t)
    d4 = player3.make_move(t)
    # minimax_times.append(t)
    # alphabeta_times.append(t)
    ordered_times.append(t)
    contest_time.append(t)
    # minimax_depths.append(d1)
    # alphabeta_depths.append(d2)
    ordered_depths.append(d3)
    contest_depth.append(d4)

# plt.scatter(minimax_times, minimax_depths, c='r')
# plt.show()
# plt.scatter(alphabeta_times, alphabeta_depths, c='y')
# plt.show()
plt.scatter(ordered_times, ordered_depths, c='g')
plt.show()
plt.scatter(contest_time, contest_depth, c='r')
plt.show()