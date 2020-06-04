class Heuristic:
    def estimate(self, problem, playing_agent):  # TODO fix heuristic func
        if playing_agent:
            possible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
        else:
            possible_forks = problem.get_nr_of_neighbor_unvisited_cell(2)
        route_length = problem.get_length_of_route()
        dist_from_rival = problem.get_dist_from_rival()
        return 6 * route_length + 3 * possible_forks + dist_from_rival
