

def utility(problem):
    rival_possible_move = problem.get_nr_of_neighbor_unvisited_cell(2)
    our_possible_move = problem.get_nr_of_neighbor_unvisited_cell(1)
    if rival_possible_move == 0 and our_possible_move > 0:
        return float("inf")
    elif our_possible_move == 0 and rival_possible_move > 0:
        return float("-inf")
    else:
        return 0


def estimate(problem):
    player1 = 1
    route_length = problem.get_length_of_route()
    possible_forks = problem.get_nr_of_neighbor_unvisited_cell(player1)
    dist_from_rival = problem.get_dist_from_rival()
    return 6*route_length + 3*possible_forks + dist_from_rival


def heuristic(problem):
    return estimate(problem)


class Minimax:
    my_agent = 1

    def __init__(self, heuristic_function, alpha_beta_pruning=False, ordered_alpha_beta=False):
        self.num_of_leaves_expanded = 0
        self.ordered_alpha_beta = ordered_alpha_beta
        self.alpha_beta_pruning = alpha_beta_pruning
        # self.heuristic_function_type = heuristic_function_type
        self.heuristic_function = heuristic_function
        pass

    def solve_problem(self, problem, depth, playing_agent):
        """

        :param problem:
        :param depth: if depth is a number then the function will act as depth restricted minmax otherwise if depth is
                        None then the function will act as a standard minmax
        :param playing_agent:
        :return:
        """
        if problem.is_goal(playing_agent):
            self.num_of_leaves_expanded += 1
            return None, utility(problem), self.num_of_leaves_expanded
        if depth == 0:
            self.num_of_leaves_expanded += 1
            return None, heuristic(problem), self.num_of_leaves_expanded
        best_move = (0, 0)
        legal_moves = problem.legal_moves(playing_agent)
        if self.ordered_alpha_beta:
            legal_moves.sort()       #TODO sort the sons by heuristic func
        if playing_agent == self.my_agent:
            current_best_minmax_value = float("-inf")
            for move in legal_moves: #TODO add support for alpha beta pruning
                problem.execute_move(playing_agent, move)
                _, minmax_val, leaves = self.solve_problem(problem, depth - 1, 1 - playing_agent) #TODO depth - 1 or None
                if minmax_val > current_best_minmax_value:
                    current_best_minmax_value = minmax_val
                    best_move = move
                problem.undo_move(playing_agent, move)
            return best_move, current_best_minmax_value, leaves
        else:
            current_best_minmax_value = float("inf")
            for move in legal_moves:
                problem.execute_move(playing_agent, move)
                _, minmax_val, leaves = self.solve_problem(problem, depth - 1, 1 - playing_agent)
                if minmax_val < current_best_minmax_value:
                    current_best_minmax_value = minmax_val
                    best_move = move
                problem.undo_move(playing_agent, move)
            return best_move, current_best_minmax_value, leaves
