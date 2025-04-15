from abc import ABC, abstractmethod
import pygame

from logic.constants import Team, Type, Move, SQUARE_SIZE, PNGS

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