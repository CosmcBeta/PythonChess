import pygame

from pieces.piece import Team, Type
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.sliding_piece import Sliding


SCREEN_SIZE = 640, 640
SQUARE_SIZE = 80

GRAY = 140, 140, 140, 160


class Board:
    def __init__(self) -> None:
        self.create_board()

    """
    (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0)
    (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)
    (0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2)
    (0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3)
    (0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4)
    (0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5)
    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)
    (0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7)
    """
    def create_board(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
    
        self.board[0] = [
            Sliding(Team.BLACK, Type.ROOK, (0, 0)), Knight(Team.BLACK, Type.KNIGHT, (1, 0)), Sliding(Team.BLACK, Type.BISHOP, (2, 0)), Sliding(Team.BLACK, Type.QUEEN, (3, 0)),
            King(Team.BLACK, Type.KING, (4, 0)), Sliding(Team.BLACK, Type.BISHOP, (5, 0)), Knight(Team.BLACK, Type.KNIGHT, (6, 0)), Sliding(Team.BLACK, Type.ROOK, (7, 0))
        ]
        self.board[1] = [Pawn(Team.BLACK, Type.PAWN, (i, 1)) for i in range(8)]
        
        self.board[7] = [
            Sliding(Team.WHITE, Type.ROOK, (0, 7)), Knight(Team.WHITE, Type.KNIGHT, (1, 7)), Sliding(Team.WHITE, Type.BISHOP, (2, 7)), Sliding(Team.WHITE, Type.QUEEN, (3, 7)),
            King(Team.WHITE, Type.KING, (4, 7)), Sliding(Team.WHITE, Type.BISHOP, (5, 7)), Knight(Team.WHITE, Type.KNIGHT, (6, 7)), Sliding(Team.WHITE, Type.ROOK, (7, 7))
        ]
        self.board[6] = [Pawn(Team.WHITE, Type.PAWN, (i, 6)) for i in range(8)]

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
    def piece_moves(self, pos):
        display = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
        display.fill((0,0,0,0))

        rank = pos[1]
        file = pos[0]

        #self.selected_piece_pos = pos
        if self.board[rank][file] is None:
            return

        self.moves = self.board[rank][file].generate_moves(self.board)
        if self.moves is None:
            return
        
        for y, column in enumerate(self.moves):
            for x, move in enumerate(column):
                if move == 0:
                    continue
                pygame.draw.circle(display, GRAY, (x*SQUARE_SIZE + 40, y*SQUARE_SIZE + 40), 40)

        return display
    
    def piece_selected(self, pos):
        rank = pos[1]
        file = pos[0]

        return self.moves[rank][file] == 1
    
    def move_piece(self, new_pos, previous_pos):
        new_rank = new_pos[1]
        new_file = new_pos[0]

        previous_rank = previous_pos[1]
        previous_file = previous_pos[0]

        self.board[new_rank][new_file] = self.board[previous_rank][previous_file]
        self.board[new_rank][new_file].location = new_pos

        if isinstance(self.board[new_rank][new_file], Pawn):
            self.board[new_rank][new_file].first_move = False
        self.board[previous_rank][previous_file] = None