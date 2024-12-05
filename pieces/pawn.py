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
        if self.team == Team.WHITE:
            dir = -1
            target_rank = 3
            opponent_start_rank = rank - 2
        else:
            dir = 1
            target_rank = 4
            opponent_start_rank = rank + 2

        dir_rank = rank + dir

        # Forwards
        if board[dir_rank][file] is None:
            moves[dir_rank][file] = Move.NORMAL

        if self.first_move and board[rank + (dir * 2)][file] is None:
            moves[rank + (dir * 2)][file] = Move.PAWN_DOUBLE

        # Diagonals
        for offset in [-1, 1]:
            adjacent_file = file + offset
            if FIRST <= adjacent_file <= LAST and board[dir_rank][adjacent_file] is not None and board[dir_rank][adjacent_file].team != self.team:
                moves[dir_rank][adjacent_file] = Move.NORMAL

        # En Passant
        if previous_move == Move.PAWN_DOUBLE:
            # Check if the pawn is on the correct rank for en passant
            if rank == target_rank:
                for offset in [-1, 1]:  # Check both left and right
                    adjacent_file = file + offset
                    # Check for boundry and the piece being moved to that location
                    if FIRST <= adjacent_file <= LAST and board[rank][adjacent_file] != previous_board[rank][adjacent_file]:
                        piece_to_check = previous_board[opponent_start_rank][adjacent_file]
                        # Make sure this is the piece that En Passanted
                        if piece_to_check is not None and piece_to_check.type == Type.PAWN:
                            moves[rank + dir][adjacent_file] = Move.EN_PASSANT

        return moves