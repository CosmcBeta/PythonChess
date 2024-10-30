import sys
import pygame

from screens.settings import Settings

"""
main menu
will include buttons for :
exit game
start game
enter settings
"""


# Class for main menu
class Menu:
    # Init
    def __init__(self, screen) -> None:
        self.screen = screen
        self.start = False
        self.settings = False
        self.settings_obj = Settings(screen, self)

    # Updates then renders
    def update(self):
        self.check_input()
        self.draw_menu()

    # Main render function
    def draw_menu(self):
        self.screen.fill("yellow")
        pygame.draw.circle(self.screen, "black", (50,50), 40)
        pygame.display.flip()

    # Checks for events/input from user
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
                # Exits the program
                if event.key == pygame.K_ESCAPE:
                    pygame.quit() 
                    sys.exit()
                # Starts game
                if event.key == pygame.K_p:
                    self.start = True
                # Opens settings
                if event.key == pygame.K_s:
                    self.settings = True