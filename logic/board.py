import pygame

from pieces.piece import Team
from pieces.king import King
from pieces.queen import Queen
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.pawn import Pawn

SCREEN_SIZE = 640, 640
SQUARE_SIZE = 80

GRAY = 140, 140, 140, 160

class Board:
    def __init__(self) -> None:
        self.create_board()


    # (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0)
    # (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)
    # (0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2)
    # (0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3)
    # (0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4)
    # (0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5)
    # (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)
    # (0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7)
    def create_board(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
    
        self.board[0] = [
            Rook(Team.BLACK, (0, 0)), Knight(Team.BLACK, (1, 0)), Bishop(Team.BLACK, (2, 0)), Queen(Team.BLACK, (3, 0)),
            King(Team.BLACK, (4, 0)), Bishop(Team.BLACK, (5, 0)), Knight(Team.BLACK, (6, 0)), Rook(Team.BLACK, (7, 0))
        ]
        self.board[1] = [Pawn(Team.BLACK, (i, 1)) for i in range(8)]
        
        self.board[7] = [
            Rook(Team.WHITE, (0, 7)), Knight(Team.WHITE, (1, 7)), Bishop(Team.WHITE, (2, 7)), Queen(Team.WHITE, (3, 7)),
            King(Team.WHITE, (4, 7)), Bishop(Team.WHITE, (5, 7)), Knight(Team.WHITE, (6, 7)), Rook(Team.WHITE, (7, 7))
        ]
        self.board[6] = [Pawn(Team.WHITE, (i, 6)) for i in range(8)]


    def draw_pieces(self):
        display = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
        display.fill((0,0,0,0))
        
        for row in self.board:
            for piece in row:
                if piece is None:
                    continue
                display.blit(piece.texture, piece.get_location())

        
        return display
    
    # Display moves for current selected piece
    def select_piece(self, pos):
        display = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
        display.fill((0,0,0,0))

        rank = pos[1]
        file = pos[0]

        #self.selected_piece_pos = pos
        if self.board[rank][file] is None:
            return

        moves = self.board[rank][file].generate_moves()
        if moves is None:
            return
        
        for y, column in enumerate(moves):
            for x, move in enumerate(column):
                if move == 0:
                    continue
                pygame.draw.circle(display, GRAY, (x*SQUARE_SIZE + 40, y*SQUARE_SIZE + 40), 40)

        return display