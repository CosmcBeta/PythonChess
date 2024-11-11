import pygame

from pieces.piece import Piece, Team, FIRST, LAST

class Queen(Piece):
    def __init__(self, team, location) -> None:
        super().__init__(team, location)

        png = "assets/black_queen.png" if team == Team.BLACK else "assets/white_queen.png"
        texture = pygame.image.load(png).convert()
        self.texture = pygame.transform.scale(texture, (80, 80))

    def generate_moves(self):
        moves = [[0 for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        # Horrizontal and vertical moves
        for i in range(8):
            moves[i][file] = 1
            moves[rank][i] = 1

        # Diagonal moves
        # Finds starting rank and file for top left diagonal moves
        temp = rank - file
        top_rank = temp if temp > FIRST else FIRST
        top_file = FIRST if temp > FIRST else abs(temp)

        # Finds starting rank and file for bottom left diagonal moves
        temp = rank + file
        bottom_rank = temp if temp < LAST else LAST
        bottom_file = FIRST if temp < LAST else temp - LAST

        # Finds the moves for the diagonals
        top = bottom = True
        while True:
            if top:
                moves[top_rank][top_file] = 1
                top_rank += 1
                top_file += 1
            if bottom:
                moves[bottom_rank][bottom_file] = 1
                bottom_rank -= 1
                bottom_file += 1

            if top_rank > LAST or top_file > LAST:
                top = False

            if bottom_rank < FIRST or bottom_file > LAST:
                bottom = False

            if not top and not bottom:
                break

        moves[rank][file] = 0
        return moves