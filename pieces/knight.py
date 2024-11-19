import pygame

from pieces.piece import Piece, Team, FIRST, LAST


class Knight(Piece):
    def __init__(self, team, type, location) -> None:
        super().__init__(team, type, location)

    def generate_moves(self, board):
        moves = [[0 for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        possible_moves = 8
        possible_moves_rank = [-2, -2, 2, 2, -1, -1, 1, 1]
        possible_moves_file = [-1, 1, -1, 1, -2, 2, -2, 2]

        for i in range(possible_moves):
            rank_pos = rank + possible_moves_rank[i]
            file_pos = file + possible_moves_file[i]
            if rank_pos > LAST or rank_pos < FIRST or file_pos > LAST or file_pos < FIRST:
                continue
            
            if board[rank_pos][file_pos] is None:
                moves[rank_pos][file_pos] = 1
            elif board[rank_pos][file_pos].team != self.team:
                moves[rank_pos][file_pos] = 1

        return moves