import pygame

from pieces.piece import Piece, Type, FIRST, LAST


DIRECTIONS = [
    (-1, 0), # Up
    (0, -1), # Left
    (1, 0), # Down
    (0, 1), # Right
    (-1, -1), # Up Left
    (-1, 1), # Up Right
    (1, -1), # Down Left
    (1, 1) # Down Right
]


class Sliding(Piece):
    def __init__(self, team, type, location) -> None:
        super().__init__(team, type, location)

        if self.type == Type.ROOK:
            self.directions = DIRECTIONS[:4]
        elif self.type == Type.BISHOP:
            self.directions = DIRECTIONS[-4:]
        elif self.type == Type.QUEEN:
            self.directions = DIRECTIONS
        else:
            self.directions = [(0, 0)]

    def generate_moves(self, board):
        moves = [[0 for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        positions = {dir: (rank, file) for dir in self.directions}

        while True:
            for dir, (r, f) in positions.items():                
                if r == -1 or f == -1:
                    continue

                r += dir[0]
                f += dir[1]

                if r < FIRST or r > LAST or f < FIRST or f > LAST:
                    positions[dir] = (-1, -1)
                    continue

                if board[r][f] is None:
                    moves[r][f] = 1
                    positions[dir] = (r, f)
                elif board[r][f].team != self.team:
                    moves[r][f] = 1
                    positions[dir] = (-1, -1)
                else:
                    positions[dir] = (-1, -1)
            
            if all(pos == (-1, -1) for pos in positions.values()):
                break

        return moves