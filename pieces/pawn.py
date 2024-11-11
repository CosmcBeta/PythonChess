import pygame

from pieces.piece import Piece, Team, FIRST, LAST

class Pawn(Piece):
    def __init__(self, team, location) -> None:
        super().__init__(team, location)
        self.first_move = True
        
        png = "assets/black_pawn.png" if team == Team.BLACK else "assets/white_pawn.png"
        texture = pygame.image.load(png).convert()
        self.texture = pygame.transform.scale(texture, (80, 80))

    def generate_moves(self):
        moves = [[0 for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        if rank == FIRST or rank == LAST:
            return

        dir = -1 if self.team == Team.WHITE else 1

        moves[rank + dir][file] = 1

        if self.first_move:
            moves[rank + (dir * 2)][file] = 1

        moves[rank][file] = 0
        return moves