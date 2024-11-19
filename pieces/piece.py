from abc import ABC, abstractmethod
from enum import Enum
import pygame


class Team(Enum):
    WHITE = 0
    BLACK = 1


class Type(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5


SQUARE_SIZE = 80
FIRST = 0
LAST = 7

PNGS = {
    Type.PAWN: ["assets/white_pawn.png", "assets/black_pawn.png"],
    Type.KNIGHT: ["assets/white_knight.png", "assets/black_knight.png"],
    Type.BISHOP: ["assets/white_bishop.png", "assets/black_bishop.png"],
    Type.ROOK: ["assets/white_rook.png", "assets/black_rook.png"],
    Type.QUEEN: ["assets/white_queen.png", "assets/black_queen.png"],
    Type.KING: ["assets/white_king.png", "assets/black_king.png"]
}


class Piece(ABC):
    def __init__(self, team, type, location) -> None:
        self.team = team
        self.type = type
        self.location = location
        
        png = PNGS[self.type][self.team.value]
        texture = pygame.image.load(png).convert()
        self.texture = pygame.transform.scale(texture, (80, 80))

    def get_location(self):
        return self.location[0] * SQUARE_SIZE, self.location[1] * SQUARE_SIZE

    def __str__(self) -> str:
        return f'Team: {self.team}, Type: {self.type}, Pos: {self.location}'
    
    def __repr__(self) -> str:
        return f'Team: {self.team}, Type: {self.type}, Pos: {self.location}'
 
    @abstractmethod
    def generate_moves(self, board):
        pass