import pygame

from pieces.piece import Piece, Team

class King(Piece):
    def __init__(self, team, location) -> None:
        super().__init__(team, location)
        
        png = "assets/black_king.png" if team == Team.BLACK else "assets/white_king.png"
        texture = pygame.image.load(png).convert()
        self.texture = pygame.transform.scale(texture, (80, 80))

    def generate_moves(self, board):
        moves = [[0 for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        for i in range(max(0, rank - 1), min(8, rank + 2)):
            for j in range(max(0, file - 1), min(8, file + 2)):
                if board[i][j] is None:
                    moves[i][j] = 1
                elif board[i][j].team != self.team:
                    moves[i][j] = 1

        moves[rank][file] = 0
        return moves
