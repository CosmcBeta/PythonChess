from abc import ABC, abstractmethod
from enum import Enum
import pygame


SQUARE_SIZE = 80
FIRST = 0
LAST = 7



class Team(Enum):
    WHITE = 0
    BLACK = 1



class Piece(ABC):
    def __init__(self, team, location) -> None:
        self.team = team
        self.location = location # For calculating moves
        
        texture = pygame.image.load("assets/white_pawn.png").convert()
        self.texture = pygame.transform.scale(texture, (80, 80))

    def get_location(self):
        return self.location[0] * SQUARE_SIZE, self.location[1] * SQUARE_SIZE

    def __str__(self) -> str:
        return f'Team: {self.team}, Pos: {self.location}'
    
    def __repr__(self) -> str:
        return f'Team: {self.team}, Pos: {self.location}'
 
    @abstractmethod
    def generate_moves(self):
        pass