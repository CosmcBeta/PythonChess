import pygame

from pieces.piece import Piece, Team, FIRST, LAST


class Pawn(Piece):
    def __init__(self, team, type, location) -> None:
        super().__init__(team, type, location)
        self.first_move = True

    def generate_moves(self, board):
        moves = [[0 for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        if rank == FIRST or rank == LAST:
            return

        dir = -1 if self.team == Team.WHITE else 1

        # Forwards
        if board[rank + dir][file] is None:
            moves[rank + dir][file] = 1

        if self.first_move and board[rank + (dir * 2)][file] is None:
            moves[rank + (dir * 2)][file] = 1

        # Diagonals
        if file + 1 <= LAST and board[rank + dir][file + 1] is not None and board[rank + dir][file + 1].team != self.team:
            moves[rank + dir][file + 1] = 1

        if file - 1 >= FIRST and board[rank + dir][file - 1] is not None and board[rank + dir][file - 1].team != self.team:
            moves[rank + dir][file - 1] = 1

        # En Passant


        return moves