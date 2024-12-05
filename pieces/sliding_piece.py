from pieces.piece import Piece, Team, Type, Move, FIRST, LAST

# Directions for adders
DIRECTIONS = [
    (-1, 0), # Up
    (0, -1), # Left
    (1, 0), # Down
    (0, 1), # Right
    (-1, -1), # Up Left
    (-1, 1), # Up Right
    (1, -1), # Down Left
    (1, 1) # Down Right
]


# Queen, Rook, Bishop pieces
class Sliding(Piece):
    def __init__(self, team: Team, type: Type, location: tuple) -> None:
        super().__init__(team, type, location)

        # Move directions needed for each piece
        if self.type == Type.ROOK:
            self.directions = DIRECTIONS[:4]
        elif self.type == Type.BISHOP:
            self.directions = DIRECTIONS[-4:]
        elif self.type == Type.QUEEN:
            self.directions = DIRECTIONS
        else:
            self.directions = [(0, 0)]

    # Queen, Rook, Bishop move generation
    def generate_moves(self, board: list[list], previous_board: list[list], previous_move: Move) -> list[list]:
        moves = [[Move.NONE for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        # Dictionary of positions; {direction: (rank, file)}
        positions = {dir: (rank, file) for dir in self.directions}

        # Loops until all directions are complete
        while True:
            # Loops over each position
            for dir, (r, f) in positions.items():                
                # Set to -1 when complete
                if r == -1 or f == -1:
                    continue

                r += dir[0]
                f += dir[1]

                if r < FIRST or r > LAST or f < FIRST or f > LAST:
                    positions[dir] = (-1, -1)
                    continue

                if board[r][f] is None:
                    moves[r][f] = Move.NORMAL
                    positions[dir] = (r, f)
                elif board[r][f].team != self.team:
                    moves[r][f] = Move.NORMAL
                    positions[dir] = (-1, -1)
                else:
                    positions[dir] = (-1, -1)
            
            # All directions are complete
            if all(pos == (-1, -1) for pos in positions.values()):
                break

        return moves