class Player:
    player1 = 1
    player2 = 2
    unvisited_cell = 0
    visited_cell = -1
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def __init__(self):
        self.loc = None
        self.rival_loc = None
        self.board = None
        self.curr_path_len = 0

    def set_game_params(self, board):
        self.board = board
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == self.player1:
                    self.loc = (i, j)
                if val == self.player2:
                    self.rival_loc = (i, j)

    def set_rival_move(self, loc):
        self.board[self.rival_loc] = self.visited_cell
        self.board[loc] = self.player2
        self.rival_loc = loc

    def execute_move(self, player, move):
        self.curr_path_len += 1
        if player == self.player1:
            new_player = self.player1
            old_location = self.loc
            new_location = (old_location[0] + move[0], old_location[1] + move[1])
            self.loc = new_location
        else:
            new_player = self.player2
            old_location = self.rival_loc
            new_location = (old_location[0] + move[0], old_location[1] + move[1])
            self.rival_loc = new_location
        self.board[old_location] = self.visited_cell
        self.board[new_location] = new_player

    def undo_move(self, player, move):
        self.curr_path_len -= 1
        if player == self.player1:
            new_player = self.player1
            old_location = self.loc
            new_location = (old_location[0] - move[0], old_location[1] - move[1])
            self.loc = new_location
        else:
            new_player = self.player2
            old_location = self.rival_loc
            new_location = (old_location[0] - move[0], old_location[1] - move[1])
            self.rival_loc = new_location
        self.board[old_location] = self.unvisited_cell
        self.board[new_location] = new_player

    def _count_neighbor_unvisited_cell(self, i, j):
        cells = 0
        for move in self.directions:
            cell = (i + move[0], j + move[1])
            if 0 <= cell[0] < len(self.board) and 0 <= cell[1] < len(self.board[0]) and self.board[cell] == 0:
                cells += 1
        return cells

    def get_nr_of_neighbor_unvisited_cell(self, player):
        if player == 1:
            return self._count_neighbor_unvisited_cell(self.loc[0], self.loc[1])
        else:
            return self._count_neighbor_unvisited_cell(self.rival_loc[0], self.rival_loc[1])

    def is_goal(self, player):
        return self.get_nr_of_neighbor_unvisited_cell(player) == 0

    def legal_moves(self, player):
        location = self.loc if player == 1 else self.rival_loc
        return [move for move in self.directions if
                0 <= location[0] + move[0] < len(self.board) and 0 <= location[1] + move[1] < len(self.board[0]) and
                self.board[location[0] + move[0]][location[1] + move[1]] == 0]

    def get_viable_moves(self):
        return self.directions

    def get_length_of_route(self):
        return self.curr_path_len

    def get_dist_from_rival(self):  # TODO remove this and replace with two functions get loc and rival loc.
        return abs(self.loc[0] - self.rival_loc[0]) + abs(self.loc[1] + self.rival_loc[1])
