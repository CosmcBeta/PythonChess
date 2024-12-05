from pieces.piece import Piece, Team, Type, Move, FIRST, LAST


# Pawn piece
class Pawn(Piece):
    def __init__(self, team: Team, type: Type, location: tuple) -> None:
        super().__init__(team, type, location)

    # Pawn move generation
    def generate_moves(self, board: list[list], previous_board: list[list], previous_move: Move) -> list[list]:
        moves = [[Move.NONE for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        # Final square
        if rank == FIRST or rank == LAST:
            return

        # Direction of moves
        dir = -1 if self.team == Team.WHITE else 1

        # Forwards
        if board[rank + dir][file] is None:
            moves[rank + dir][file] = Move.NORMAL

        if self.first_move and board[rank + (dir * 2)][file] is None:
            moves[rank + (dir * 2)][file] = Move.PAWN_DOUBLE

        # Diagonals
        if file + 1 <= LAST and board[rank + dir][file + 1] is not None and board[rank + dir][file + 1].team != self.team:
            moves[rank + dir][file + 1] = Move.NORMAL

        if file - 1 >= FIRST and board[rank + dir][file - 1] is not None and board[rank + dir][file - 1].team != self.team:
            moves[rank + dir][file - 1] = Move.NORMAL

        # En Passant        
        if previous_move == Move.PAWN_DOUBLE: # Previous move was a double pawn move
            # White En Passant
            if self.team == Team.WHITE: # Team
                if rank == 3: # Pawn is in the right row
                    if file + 1 <= LAST: # Right boundry
                        if board[rank][file + 1] != previous_board[rank][file + 1]: # Check if the piece next to it is the same before and after the previous move
                            if previous_board[rank - 2][file + 1] is not None and previous_board[rank - 2][file + 1].type == Type.PAWN: # Makes sure it was this pawn that moved double
                                moves[rank - 1][file + 1] = Move.EN_PASSANT
                    if file - 1 >= FIRST: # Left boundry
                        if board[rank][file - 1] != previous_board[rank][file - 1]:
                            if previous_board[rank - 2][file - 1] is not None and previous_board[rank - 2][file - 1].type == Type.PAWN:
                                moves[rank - 1][file - 1] = Move.EN_PASSANT
            # Black En Passant
            if self.team == Team.BLACK:
                if rank == 4:
                    if file + 1 <= LAST: # Right boundry
                        if board[rank][file + 1] != previous_board[rank][file + 1]: # Check if the piece next to it is the same before and after the previous move
                            if previous_board[rank + 2][file + 1] is not None and previous_board[rank + 2][file + 1].type == Type.PAWN: # Makes sure it was this pawn that moved double
                                moves[rank + 1][file + 1] = Move.EN_PASSANT
                    if file - 1 >= FIRST: # Left boundry
                        if board[rank][file - 1] != previous_board[rank][file - 1]:
                            if previous_board[rank + 2][file - 1] is not None and previous_board[rank + 2][file - 1].type == Type.PAWN:
                                moves[rank + 1][file - 1] = Move.EN_PASSANT


        return moves