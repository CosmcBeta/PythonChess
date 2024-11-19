import sys
import pygame

from screens.pause import Pause
from logic.board import Board


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

                piece_moved = False
                if self.piece_selected:
                    piece_moved = self.board.piece_selected(pos) # Bool if the piece moves or just selects a different square; true if moves, false if stays

                if piece_moved:
                    self.moves = None
                    self.board.move_piece(pos, self.previous_pos)
                else:
                    self.moves = self.board.piece_moves(pos)
                
                self.piece_selected = True if self.moves is not None else False
                self.previous_pos = pos