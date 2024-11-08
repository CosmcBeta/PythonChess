import pygame

from pieces.piece import Piece, Team

class Knight(Piece):
    def __init__(self, team, location) -> None:
        super().__init__(team, location)
        
        png = "assets/black_knight.png" if team == Team.BLACK else "assets/white_knight.png"
        texture = pygame.image.load(png).convert()
        self.texture = pygame.transform.scale(texture, (80, 80))

    def generate_moves(self):
        pass