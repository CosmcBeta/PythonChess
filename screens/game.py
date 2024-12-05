import sys
import pygame

from screens.pause import Pause
from logic.board import Board
from pieces.piece import Team, Move, FIRST, LAST

# Constants
SQUARE_SIZE = 80

LIGHT_BROWN = 236, 236, 208, 255
DARK_BROWN = 181, 136, 95, 255
# redHighlight(243, 60, 66, 255),
# 	yellowHighlight(246, 246, 129, 255),
# 	textHighlight(143, 107, 74, 255),


"""
Main game loop
will render the main game

"""


# Class for main game loop
class Game:
    # Init
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.game_over = False
        self.pause = False
        self.moves = None
        self.piece_selected = False
        self.previous_pos = (0, 0)
        self.pause_obj = Pause(screen, self)
        self.board = Board()
        #self.players_turn = self.board.players_turn
        self.create_background_board()

    # Updates then renders
    def update(self) -> None:
        self.draw_game()
        self.check_input()

    # Main render function
    def draw_game(self):
        self.screen.blit(self.background_board, self.background_board.get_rect())
        pieces = self.board.draw_pieces()
        self.screen.blit(pieces, pieces.get_rect())
        if self.moves is not None:
            self.screen.blit(self.moves, self.moves.get_rect())
        pygame.display.flip()
    
    # Draws the background board
    def create_background_board(self):
        self.background_board = pygame.Surface((SQUARE_SIZE * 8, SQUARE_SIZE * 8))
        self.background_board.fill(DARK_BROWN)
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(self.background_board, LIGHT_BROWN, (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Checks for events/updates from user
    def check_input(self):
        events = pygame.event.get()
        # Loops over events
        for event in events:
            # Clicked the exit button for app
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Pressed a key
            if event.type == pygame.KEYDOWN:
                # Opens pause menu
                if event.key == pygame.K_ESCAPE:
                    self.pause = True
                # Ends the game
                if event.key == pygame.K_o:
                    self.game_over = True

            # Mouse movement
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                pos = pos[0] // 80, pos[1] // 80

                # If mouse is at the very edge of screen
                if pos[0] == 8:
                    pos = 7, pos[1]

                if pos[1] == 8:
                    pos = pos[0], 7
                
                # Determines whether piece is moving or selecting a different piece
                move = Move.NONE
                if self.piece_selected:
                    move = self.board.move_type(pos)

                # Moves the piece selected
                if move != Move.NONE:
                    self.moves = None
                    self.board.move_piece(pos, self.previous_pos, move)
                    if move == Move.RIGHT_CASTLE or move == Move.LEFT_CASTLE:
                        rank = pos[1]
                        if move == Move.LEFT_CASTLE:
                            rook_pos = (FIRST, rank)
                            new_pos = (FIRST + 3, rank)
                        if move == Move.RIGHT_CASTLE:
                            rook_pos = (LAST, rank)
                            new_pos = (LAST - 2, rank)
                        self.board.move_piece(new_pos, rook_pos, move)
                    
                    if move == Move.EN_PASSANT:
                        if self.board.players_turn == Team.WHITE:
                            self.board.remove_piece((pos[0], pos[1] + 1))
                        elif self.board.players_turn == Team.BLACK:
                            self.board.remove_piece((pos[0], pos[1] - 1))


                    self.board.players_turn = Team.BLACK if self.board.players_turn == Team.WHITE else Team.WHITE
                else: # Selects next pieces moves
                    self.moves = self.board.piece_moves(pos)
                
                # Determines if new piece is selected or not
                self.piece_selected = True if self.moves is not None else False
                self.previous_pos = pos