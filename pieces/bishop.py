import pygame
from pieces.piece import Piece, Team

class Bishop(Piece):
    def __init__(self, team, location) -> None:
        super().__init__(team, location)
        
        png = "assets/black_bishop.png" if team == Team.BLACK else "assets/white_bishop.png"
        texture = pygame.image.load(png).convert()
        self.texture = pygame.transform.scale(texture, (80, 80))

    def generate_moves(self):
        pass