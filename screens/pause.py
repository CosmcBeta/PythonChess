import sys
import pygame

from screens.settings import Settings

"""
Pause menu for game
runs when escape is pressed
will show 3 buttons
main menu
settings
quit
"""


# Class for pause menu
class Pause:
    # Init
    def __init__(self, screen, game) -> None:
        self.screen = screen
        self.game = game
        self.settings = False
        self.settings_obj = Settings(screen, self)

    # Updates then renders
    def update(self):
        self.draw_options()
        self.check_input()

    # Main draw function
    def draw_options(self):
        self.screen.fill("red")
        pygame.draw.circle(self.screen, "purple", (50,50), 40)
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

            # Pressed a key
            if event.type == pygame.KEYDOWN:
                # Exits pause menu
                if event.key == pygame.K_ESCAPE:
                    self.game.pause = False

                # Opens settings
                if event.key == pygame.K_s:
                    self.settings = True
                    # Settings loop
                    while self.settings:
                        self.settings_obj.update()