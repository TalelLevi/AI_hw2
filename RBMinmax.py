from Minimax import Minimax
import time as time


class RBMinmax:

    def __init__(self, alpha_beta_pruning=False, ordered_alpha_beta=False):
        self.ordered_alpha_beta = ordered_alpha_beta
        self.alpha_beta_pruning = alpha_beta_pruning
        pass

    def estimate_next_iteration(self, number_of_leaves, last_iteration_time):
        return last_iteration_time * 3 * number_of_leaves

    def solve(self, time_limit, problem):
        ID_start_time = time.time()
        depth = 1
        algo = Minimax(None, self.alpha_beta_pruning, self.ordered_alpha_beta)
        move, _, leaves = algo.solve_problem(problem=problem, depth=depth, playing_agent=1)
        last_iteration_time = time.time() - ID_start_time
        next_iteration_max_time = self.estimate_next_iteration(leaves, last_iteration_time)
        time_until_now = time.time() - ID_start_time
        while time_until_now + next_iteration_max_time < time_limit:
            depth += 1
            iteration_start_time = time.time()
            move, _, leaves = algo.solve_problem(problem=problem, depth=depth, playing_agent=1)
            last_iteration_time = time.time() - iteration_start_time
            next_iteration_max_time = self.estimate_next_iteration(leaves, last_iteration_time)
            time_until_now = time.time() - ID_start_time
        return move
