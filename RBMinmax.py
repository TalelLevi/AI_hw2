from Minimax import Minimax
from time import time

import logging

lg = logging.getLogger("help me")


class RBMinmax:

    def __init__(self, alpha_beta_pruning=False, ordered_alpha_beta=False):
        self.ordered_alpha_beta = ordered_alpha_beta
        self.alpha_beta_pruning = alpha_beta_pruning

    def estimate_next_iteration(self, number_of_leaves, last_iteration_time):
        return last_iteration_time * 3 * number_of_leaves

    def solve(self, time_limit, problem):
        start_time = time()
        depth = 1
        last_iteration_minimax_val = {move: 0 for move in problem.get_viable_moves()}
        algo = Minimax(None, self.alpha_beta_pruning, self.ordered_alpha_beta, last_iteration_minimax_val)
        move, _, leaves = algo.solve_problem(problem=problem, depth=depth, playing_agent=1)
        last_iteration_time = time() - start_time
        next_iteration_max_time = self.estimate_next_iteration(leaves, last_iteration_time)
        time_until_now = time() - start_time
        while time_until_now + next_iteration_max_time < time_limit:
            depth += 1
            lg.error(f"depth is {depth} current best move {move}")
            iteration_start_time = time()
            move, _, leaves = algo.solve_problem(problem=problem, depth=depth, playing_agent=1)
            last_iteration_time = time() - iteration_start_time
            next_iteration_max_time = self.estimate_next_iteration(leaves, last_iteration_time)
            time_until_now = time() - start_time
        return move
