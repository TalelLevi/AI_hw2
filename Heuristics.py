
class Heuristic:
    def estimate(self, problem, playing_agent):
        up_left = 0
        up_right = 0
        down_left = 0
        down_right = 0

        right = 0
        left = 0
        up = 0
        down = 0
        # create a box around the current state of 5X5,
        # split it into 4 small boxes of 2x2 and 4 2x1 vectors between each 2x2 block.
        # count the number of visited cells in each block
        for i in range(-2, 3):
            for j in range(-2, 3):
                cell = (problem.loc[0] + i, problem.loc[1] + j)
                if not problem.in_board(cell) or problem.board[cell] == -1:
                    if i < 0 and j < 0:
                        down_left += 1
                    elif i < 0 and j > 0:
                        down_right += 1
                    elif i > 0 and j < 0:
                        up_left += 1
                    elif i > 0 and j > 0:
                        up_right += 1
                    elif i == 0:
                        if j == -1 or j == -2:
                            left += 1
                        elif j == 1 or j == 2:
                            right += 1
                    elif j == 0:
                        if i == -1 or j == -2:
                            down += 1
                        elif i == 1 or i == 2:
                            up += 1

        # calculate for each combination of 3 blocks vs 1 block. we are trying to get as close as possible to 3 fully
        # visited blocks to 1 unvisited block. return the max of those possibilities  ( to negate direction )

        return max(abs(up_left + left + down_left + up_right + up - down - right - down_right),
                   abs(up_left + left + down_left + down_right + down - up - right - up_right),
                   abs(down_left + up_right + down_right + down + right - up - left - up_left),
                   abs(up_left + up_right + down_right + up + right - down - left - down_left))


def dfsl_aux(problem):
    visited = set()
    escaped = set()
    dfsl2(problem, problem.loc, visited, escaped)
    return visited, escaped


def dfsl2(problem, cell, visited=None, escaped=None):
    visited.add(cell)
    if abs(problem.loc[0] - cell[0]) > 4 or abs(problem.loc[1] - cell[1]) > 4:
        escaped.add(cell)

    considered_cells = [(move[0] + cell[0], move[1] + cell[1]) for move in problem.get_viable_moves()]
    legal_cells = [cell for cell in considered_cells if problem.in_board(cell)
                   and cell not in visited
                   and problem.board[cell] == 0]

    for curr_cell in legal_cells:
        dfsl2(problem, curr_cell, visited, escaped)


class Heuristic2:
    war_radius = 7
    min_value_offset = 35

    def estimate(self, problem, playing_agent):
        dist_from_rival = problem.get_dist_from_rival()
        if dist_from_rival <= self.war_radius:
            return 100 + problem.get_nr_of_neighbor_unvisited_cell(1)

        visited, escaped = dfsl_aux(problem)
        if len(escaped) == 0:
            return -self.min_value_offset + len(visited)
        count = 0
        for i in range(-4, 5):
            for j in range(-4, 5):
                cell = (problem.loc[0] + i, problem.loc[1] + j)
                if problem.in_board(cell):
                    if problem.board[cell] == -1:
                        count += 2
                    elif problem.board[cell] == 0:
                        count -= 1
                else:
                    count += 1
        return count + self.min_value_offset + len(visited)


def dfsl(problem, cell, visited=None):
    if visited is None:
        visited = set()
    visited.add(cell)

    considered_cells = [(move[0] + cell[0], move[1] + cell[1]) for move in problem.get_viable_moves()]
    legal_cells = [cell for cell in considered_cells if problem.in_board(cell)
                   and cell not in visited
                   and problem.board[cell] == 0]

    for curr_cell in legal_cells:
        # check if we escaped the "box"
        if abs(problem.loc[0] - curr_cell[0]) > 4 or abs(problem.loc[1] - curr_cell[1]) > 4:
            return True
        elif dfsl(problem, curr_cell, visited):
            return True
    return False


class Heuristic3:
    war_radius = 7
    min_value_offset = 35

    def estimate(self, problem, playing_agent):
        dist_from_rival = problem.get_dist_from_rival()
        posible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
        dist_from_mid = problem.dist_from_mid(1)
        max_dist = len(problem.board) + len(problem.board[0])
        return round((-dist_from_rival/max_dist)* 3) + round((+dist_from_mid/max_dist) * 3) + posible_forks


def backtrack_out(problem, cell):
    player = problem.board[cell]
    problem.board[cell] = 0
    ret_val = inner_backtrack(problem, cell)
    problem.board[cell] = player
    return ret_val


def inner_backtrack(problem, cell):
    if not problem.in_board(cell):
        return False
    elif not problem.board[cell] == 0:
        return False
    elif abs(problem.loc[0] - cell[0]) > 3 or abs(problem.loc[1] - cell[1]) > 3:
        return True

    problem.board[cell] = 3
    ret_value = inner_backtrack(problem, (cell[0] + 1, cell[1])) or \
                inner_backtrack(problem, (cell[0] - 1, cell[1])) or \
                inner_backtrack(problem, (cell[0], cell[1] + 1)) or \
                inner_backtrack(problem, (cell[0], cell[1] - 1))

    problem.board[cell] = 0
    return ret_value
