from Player import Player
from RBMinmax import RBMinmax
from Heuristics import Heuristic2


class ContestPlayer(Player):
    def __init__(self):
        super(ContestPlayer, self).__init__()

    def make_move(self, time_limit):
        calc_move_algo = RBMinmax(Heuristic2, alpha_beta_pruning=True, ordered_alpha_beta=True)
        move = calc_move_algo.solve(time_limit=time_limit, problem=self)
        self.execute_move(self.player1, move) #TODO uncomment
        return move
