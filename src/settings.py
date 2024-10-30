import sys
import pygame

"""
Settings menu
change theme
sound? if we decide to include this
change background
change font? again if i decide
change piece texture
stuff like that

"""


# Class for settings menu
class Settings:
    # Init
    def __init__(self, screen, last_display) -> None:
        self.screen = screen
        self.last_display = last_display

    # Updates then renders
    def update(self):
        self.check_input()
        self.draw_settings()

    # Main draw function
    def draw_settings(self):
        self.screen.fill("green")
        pygame.draw.circle(self.screen, "blue", (50,50), 40)
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
                # Exits settins
                if event.key == pygame.K_ESCAPE:
                    self.last_display.settings = False 