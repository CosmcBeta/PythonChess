from pieces.piece import Piece
from logic.constants import Team, Type, Move, FIRST, LAST

# Knight piece
class Knight(Piece):
    def __init__(self, team: Team, type: Type, location: tuple) -> None:
        super().__init__(team, type, location)

    # Knight move generation
    def generate_moves(self, board: list[list], previous_board: list[list], previous_move: Move) -> list[list]:
        moves = [[Move.NONE for _ in range(8)] for _ in range(8)]

        rank = self.location[1] # Row
        file = self.location[0] # Column

        # All possible move adders
        possible_moves = 8
        possible_moves_rank = [-2, -2, 2, 2, -1, -1, 1, 1]
        possible_moves_file = [-1, 1, -1, 1, -2, 2, -2, 2]

        for i in range(possible_moves):
            rank_pos = rank + possible_moves_rank[i]
            file_pos = file + possible_moves_file[i]

            if rank_pos > LAST or rank_pos < FIRST or file_pos > LAST or file_pos < FIRST:
                continue
            
            if board[rank_pos][file_pos] is None:
                moves[rank_pos][file_pos] = Move.NORMAL
            elif board[rank_pos][file_pos].team != self.team:
                moves[rank_pos][file_pos] = Move.NORMAL

        return moves