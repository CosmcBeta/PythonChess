from abc import ABC, abstractmethod
from enum import Enum
import pygame


# Team
class Team(Enum):
    WHITE = 0
    BLACK = 1


# Piece Type
class Type(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5


class Move(Enum):
    NONE = 0    
    NORMAL = 1
    LEFT_CASTLE = 2
    RIGHT_CASTLE = 3
    EN_PASSANT = 4
    PAWN_DOUBLE = 5


# Constants
SQUARE_SIZE = 80
FIRST = 0
LAST = 7

# Images for pieces
PNGS = {
    Type.PAWN: ["assets/white_pawn.png", "assets/black_pawn.png"],
    Type.KNIGHT: ["assets/white_knight.png", "assets/black_knight.png"],
    Type.BISHOP: ["assets/white_bishop.png", "assets/black_bishop.png"],
    Type.ROOK: ["assets/white_rook.png", "assets/black_rook.png"],
    Type.QUEEN: ["assets/white_queen.png", "assets/black_queen.png"],
    Type.KING: ["assets/white_king.png", "assets/black_king.png"]
}


# Abstract Class for a piece
class Piece(ABC):
    def __init__(self, team: Team, type: Type, location: tuple) -> None:
        self.team = team
        self.type = type
        self.location = location
        self.first_move = True
        
        # Sets texture based on piece type
        png = PNGS[self.type][self.team.value]
        texture = pygame.image.load(png).convert()
        self.texture = pygame.transform.scale(texture, (80, 80))

    # Custom deep copy method to exclude 'texture'
    def __deepcopy__(self, memo):
        # Create a new instance of the piece without copying the 'texture' attribute
        copied_obj = self.__class__(self.team, self.type, self.location)
        
        # Prevent recursion: register the copied object in the memo dictionary
        memo[id(self)] = copied_obj
        
        # Copy simple attributes
        copied_obj.first_move = self.first_move
        return copied_obj

    # Returns location of the piece on the screen scale
    def get_location(self) -> tuple:
        return self.location[0] * SQUARE_SIZE, self.location[1] * SQUARE_SIZE

    # Returns str of piece
    def __str__(self) -> str:
        return f'Team: {self.team}, Type: {self.type}, Pos: {self.location}'
    
    # Returns repr of piece
    def __repr__(self) -> str:
        return f'Team: {self.team}, Type: {self.type}, Pos: {self.location}'
 
    # Abstract method for move generation
    @abstractmethod
    def generate_moves(self, board: list[list], previous_board: list[list], previous_move: Move) -> list[list]:
        pass