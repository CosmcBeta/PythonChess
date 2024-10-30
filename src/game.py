import sys
import pygame

from pause import Pause

"""
Main game loop
will render the main game

"""


# Class for main game loop
class Game:
    # Init
    def __init__(self, screen) -> None:
        self.screen = screen
        self.game_over = False
        self.pause = False
        self.pause_obj = Pause(screen, self)

    # Updates then renders
    def update(self) -> None:
        self.draw_game()
        self.check_input()

    # Main render function
    def draw_game(self):
        self.screen.fill("purple")
        pygame.draw.circle(self.screen, "red", (50,50), 40)
        pygame.display.flip()
    
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