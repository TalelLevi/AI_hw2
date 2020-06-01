from Player import Player
from RBMinmax import RBMinmax


class OrderedAlphaBetaPlayer(Player):
    def __init__(self):
        super(Player, self).__init__()
        self.curr_path = 0

    def make_move(self, time_limit):
        calc_move_algo = RBMinmax(alpha_beta_pruning=True, ordered_alpha_beta=True)
        move = calc_move_algo.solve(time_limit=time_limit, problem=self)
        self.execute_move(self.player1, move)
        return move

    def get_length_of_route(self):
        return self.curr_path

    def get_dist_from_rival(self):  # TODO remove this and replace with two functions get loc and rival loc.
        return abs(self.loc[0] - self.rival_loc[0]) + abs(self.loc[1] + self.rival_loc[1])
