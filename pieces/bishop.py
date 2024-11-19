import pygame

from pieces.piece import Piece, Team, FIRST, LAST

class Bishop(Piece):
    def __init__(self, team, location) -> None:
        super().__init__(team, location)
        
        png = "assets/black_bishop.png" if team == Team.BLACK else "assets/white_bishop.png"
        texture = pygame.image.load(png).convert()
        self.texture = pygame.transform.scale(texture, (80, 80))

    def generate_moves(self, board):
        moves = [[0 for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        directions = [
            (-1, -1), # Up Left
            (-1, 1), # Up Right
            (1, -1), # Down Left
            (1, 1) # Down Right
        ]

        positions = {dir: (rank, file) for dir in directions}
        
        while True:
            for dir, (r, f) in positions.items():
                dr, df = dir

                if r == -1 or f == -1:
                    continue

                r += dr
                f += df

                if r < FIRST or r > LAST or f < FIRST or f > LAST:
                    positions[dir] = (-1, -1)
                    continue

                if board[r][f] is None:
                    moves[r][f] = 1
                    positions[dir] = (r, f)
                elif board[r][f].team != self.team:
                    moves[r][f] = 1
                    positions[dir] = (-1, -1)
                else:
                    positions[dir] = (-1, -1)
            
            if all(pos == (-1, -1) for pos in positions.values()):
                break

        return moves