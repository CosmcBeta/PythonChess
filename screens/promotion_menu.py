import sys
import pygame

from logic.constants import SCREEN_SIZE, SQUARE_SIZE, OUTLINE_SIZE, OUTLINE_SQUARE_SIZE, PNGS, Type, Team, LIGHT_BROWN


# Class for piece select menu
class Promotion_Menu:
    # Init
    def __init__(self, screen, game) -> None:
        self.screen = screen
        self.game = game
        self.team = game.board.players_turn
        self.selections = [Type.KNIGHT, Type.BISHOP, Type.ROOK, Type.QUEEN]
        self.create_squares()

    # Creates the squares
    def create_squares(self) -> None:
        x = SCREEN_SIZE[1] / 2 - SQUARE_SIZE * 2 # Starting x value
        y = SCREEN_SIZE[0] / 2 - SQUARE_SIZE / 2 # The height
       
        # The center square
        self.selection_squares = [(x + (i * SQUARE_SIZE) + (OUTLINE_SIZE * (i - 1.5)), y, SQUARE_SIZE, SQUARE_SIZE) for i in range(4)]
        # The outline square, also the square for selection
        self.outline_squares = [(x + (i * SQUARE_SIZE) + (OUTLINE_SIZE * (i - 2)), y - OUTLINE_SIZE / 2, OUTLINE_SQUARE_SIZE, OUTLINE_SQUARE_SIZE) for i in range(4)]

        # Locations for the textures
        self.locations = [(x + (i * SQUARE_SIZE) + (OUTLINE_SIZE * (i - 1.5)), y) for i in range(4)]
        self.create_textures()

    # Creates the textures for the pieces to make the selections
    def create_textures(self):
        self.textures = []
        for piece in self.selections:
            png = PNGS[piece][self.team.value]
            texture = pygame.image.load(png).convert()
            self.textures.append(pygame.transform.scale(texture, (80, 80)))

    # Updates then renders
    def update(self):
        self.team = Team.WHITE if self.game.board.players_turn == Team.BLACK else Team.BLACK
        self.create_textures()
        self.draw_selection()
        self.check_input()

    # Main draw function
    def draw_selection(self):
        # For making the background of pngs transparent
        display = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
        display.fill((0,0,0,0))

        # Displays the menu
        for i in range(4):
            pygame.draw.rect(self.screen, 'black', self.outline_squares[i])
            pygame.draw.rect(self.screen, LIGHT_BROWN, self.selection_squares[i])
            display.blit(self.textures[i], self.locations[i])
        
        self.screen.blit(display, display.get_rect())

        pygame.display.flip()

    # Checks for events/inputs from user
    def check_input(self):
        events = pygame.event.get()
        # Loops over events
        for event in events:
            # Clicked the exit button for app
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse movement
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos_x, pos_y = pos
                for index, rect in enumerate(self.outline_squares):
                    x, y, w, h = rect

                    # Checks if mouse is in this rect
                    if x < pos_x < x + w and y < pos_y < y + h:
                        type = self.selections[index] # Gets new piece
                        self.game.board.set_piece(self.game.pawn_pos, type, self.team) # Sets new piece
                        self.game.promotion_menu = False # Exits menu