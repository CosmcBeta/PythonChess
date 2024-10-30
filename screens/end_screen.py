import sys
import pygame

"""
end screen
display who won
buttons for:
play again
main meu
"""


# Game over screen
class EndScreen:
    # Init
    def __init__(self, screen) -> None:
        self.screen = screen
        self.restart = False
        self.exit_end_screen = False
    
    # Updates then renders
    def update(self):
        self.check_input()
        self.draw_end_screen()

    # Main render function
    def draw_end_screen(self):
        self.screen.fill("blue")
        pygame.draw.circle(self.screen, "white", (50,50), 40)
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
                # Restart the game
                if event.key == pygame.K_r:
                    self.exit_end_screen = True
                    self.restart = True
                # Opens menu
                if event.key == pygame.K_m:
                    self.exit_end_screen = True