from Player import Player
from RBMinmax import RBMinmax
from Heuristics import Heuristic


class AlphaBetaPlayer(Player):
    def __init__(self):
        super(AlphaBetaPlayer, self).__init__()

    def make_move(self, time_limit):
        calc_move_algo = RBMinmax(Heuristic, alpha_beta_pruning=True)
        move = calc_move_algo.solve(time_limit=time_limit, problem=self)
        self.execute_move(self.player1, move)
        return move
