from pieces.piece import Piece, Team, Type, FIRST, LAST


# Pawn piece
class Pawn(Piece):
    def __init__(self, team: Team, type: Type, location: tuple) -> None:
        super().__init__(team, type, location)
        self.first_move = True

    # Pawn move generation
    def generate_moves(self, board: list[list]) -> list[list]:
        moves = [[0 for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        # Final square
        if rank == FIRST or rank == LAST:
            return

        # Direction of moves
        dir = -1 if self.team == Team.WHITE else 1

        # Forwards
        if board[rank + dir][file] is None:
            moves[rank + dir][file] = 1

        if self.first_move and board[rank + (dir * 2)][file] is None:
            moves[rank + (dir * 2)][file] = 1

        # Diagonals
        if file + 1 <= LAST and board[rank + dir][file + 1] is not None and board[rank + dir][file + 1].team != self.team:
            moves[rank + dir][file + 1] = 1

        if file - 1 >= FIRST and board[rank + dir][file - 1] is not None and board[rank + dir][file - 1].team != self.team:
            moves[rank + dir][file - 1] = 1

        # En Passant
        # Rules:
        # describes the capture by a pawn of an enemy pawn on the same rank and an adjacent 
        # file that has just made an initial two-square advance.[2][3] This is a special case 
        # in the rules of chess. The capturing pawn moves to the square that the enemy pawn passed over, 
        # as if the enemy pawn had advanced only one square. The rule ensures that a pawn cannot use its 
        # two-square move to safely skip past an enemy pawn.

        # if self.team == Team.WHITE: # Team
        #     if rank == 2: # 3rd row, one below black pawns
        #         if file + 1 <= LAST: # boundry
        #             if board[rank][file + 1] is not None: # Piece is actually there
        #                 if board[rank][file + 1].type == Type.PAWN: # Is a pawn
        #                     if board[rank][file + 1].team != self.team: # Not on my team
        #                         if # Last move was this pawn moving 2 spaces to get here






        return moves