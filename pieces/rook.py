import pygame

from pieces.piece import Piece, Team

class Rook(Piece):
    def __init__(self, team, location) -> None:
        super().__init__(team, location)
        
        png = "assets/black_rook.png" if team == Team.BLACK else "assets/white_rook.png"
        texture = pygame.image.load(png).convert()
        self.texture = pygame.transform.scale(texture, (80, 80))

    def generate_moves(self):
        moves = [[0 for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        for i in range(8):
            moves[i][file] = 1
            moves[rank][i] = 1

        moves[rank][file] = 0
        return moves