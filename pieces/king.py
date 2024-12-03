from pieces.piece import Piece, Team, Type, Move, FIRST, LAST


# King piece
class King(Piece):
    def __init__(self, team: Team, type: Type, location: tuple) -> None:
        super().__init__(team, type, location)

    # King move generation
    def generate_moves(self, board: list[list]) -> list[list]:
        moves = [[0 for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        # Normal moves
        for i in range(max(0, rank - 1), min(8, rank + 2)):
            for j in range(max(0, file - 1), min(8, file + 2)):
                if board[i][j] is None:
                    moves[i][j] = 1
                elif board[i][j].team != self.team:
                    moves[i][j] = 1

        # Castling
        if self.first_move:
            if self.check_castle(rank, FIRST, board, [1, 2, 3]):
                 moves[rank][FIRST + 2] = Move.LEFT_CASTLE

            if self.check_castle(rank, LAST, board, [-1, -2]):
                 moves[rank][LAST - 1] = Move.RIGHT_CASTLE

        moves[rank][file] = 0
        return moves

    # Checks if it's possible to castle
    def check_castle(self, rank: int, file: int, board: list[list], empty_spaces: list) -> bool:
        rook = board[rank][file]
        return rook is not None and rook.type == Type.ROOK and rook.first_move and rook.team == self.team and all(board[rank][file + i] is None for i in empty_spaces)