class Heuristic:
    def estimate(self, problem, playing_agent):
        # if problem.get_dist_from_rival() <= 15:
        #     # check if path exists if yes do something.
        #     return 18 + problem.get_nr_of_neighbor_unvisited_cell(1)
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
        if not backtrack_out(problem, problem.loc, 20):
            return -100
        return max(abs(up_left + left + down_left + up_right + up - down - right - down_right),
                   abs(up_left + left + down_left + down_right + down - up - right - up_right),
                   abs(down_left + up_right + down_right + down + right - up - left - up_left),
                   abs(up_left + up_right + down_right + up + right - down - left - down_left))


def backtrack_out(problem, cell, length):
    player = problem.board[cell]
    problem.board[cell] = 0
    ret_val = inner_backtrack(problem, cell, length)
    problem.board[cell] = player
    return ret_val

def inner_backtrack(problem, cell, length):
    if not problem.in_board(cell):
        return False
    elif not problem.board[cell] == 0:
        return False
    elif abs(problem.loc[0] - cell[0]) > 2 or abs(problem.loc[1] - cell[1]) > 2:
        return True
    problem.board[cell] = 3
    ret_value = inner_backtrack(problem, (cell[0] + 1, cell[1]), length - 1) or \
                inner_backtrack(problem, (cell[0] - 1, cell[1]), length - 1) or \
                inner_backtrack(problem, (cell[0], cell[1] + 1), length - 1) or \
                inner_backtrack(problem, (cell[0], cell[1] - 1), length - 1)
    problem.board[cell] = 0
    return ret_value


def backtrack_out2(problem, cell, length):
    player = problem.board[cell]
    problem.board[cell] = 0
    ret_val = inner_backtrack2(problem, cell, length)
    problem.board[cell] = player
    return ret_val

def inner_backtrack2(problem, cell, length):
    if not problem.in_board(cell):
        return False, length
    elif not problem.board[cell] == 0:
        return False, length
    elif abs(problem.loc[0] - cell[0]) > 2 or abs(problem.loc[1] - cell[1]) > 2:
        return True, length
    problem.board[cell] = 3
    ret_value, path_len = max(inner_backtrack2(problem, (cell[0] + 1, cell[1]), length - 1),
                              inner_backtrack2(problem, (cell[0] - 1, cell[1]), length - 1),
                              inner_backtrack2(problem, (cell[0], cell[1] + 1), length - 1),
                              inner_backtrack2(problem, (cell[0], cell[1] - 1), length - 1),
                              key=lambda tup: tup[0]*tup[1])
    problem.board[cell] = 0
    return ret_value, path_len


class Heuristic2:
    def estimate(self, problem, playing_agent):
        dist = problem.get_dist_from_rival()
        if dist <= 10:
            return 100 - dist + problem.get_nr_of_neighbor_unvisited_cell(1)

        escape_route, path_len = backtrack_out2(problem, problem.loc, 20)
        if not escape_route:
            return path_len
        count = 0
        for i in range(-4, 5):
            for j in range(-4, 5):
                cell = (problem.loc[0] + i, problem.loc[1] + j)
                if problem.in_board(cell):
                    if problem.board[cell] == -1:
                        count += 1
        return count
