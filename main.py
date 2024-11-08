import pygame

from screens.menu import Menu
from screens.game import Game
from screens.end_screen import EndScreen


# Main function
def main():
    # Init pygame and setup variables and screen
    pygame.init()
    window_size = 640, 640
    max_frame_rate = 60
    screen = pygame.display.set_mode(window_size)
    end_screen = EndScreen(screen) # Here to make sure no errors

    # Main loop for gameplay
    while True:
        # Create objects
        game = Game(screen)
        menu = Menu(screen)

        # Menu updating
        while not menu.start and not end_screen.restart:
            if menu.settings:
                menu.settings_obj.update()
            else:
                menu.update()

        # Create clock
        clock = pygame.time.Clock()

        # Game loop
        while not game.game_over:
            if game.pause:
                game.pause_obj.update()
            else:
                game.update()
            
            # Update display and tick the clock
            pygame.display.update()
            clock.tick(max_frame_rate)
        
        # Create end screen object
        end_screen = EndScreen(screen)

        # Game over screen loop
        while not end_screen.exit_end_screen:
            end_screen.update()



if __name__ == '__main__':
    main()