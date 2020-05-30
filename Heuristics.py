
class MinmaxHeuristic:
    def estimate(self, problem):
        route_length = problem.get_length_of_route()
        possible_forks = problem.get_nr_of_unvisited_cell()
        dist_from_rival = problem.get_dist_from_rival()
        return 6*route_length + 3*possible_forks + dist_from_rival