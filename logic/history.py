from pieces.piece import Move

class History:
    def __init__(self) -> None:
        self.history = []

    def add_board(self, board, move):
        self.history.append((board, move))
        self.previous_board = board
        self.previous_move = move
    
    def get_last_board(self):
        if not self.history:
            return None
        return self.previous_board
        
    def get_last_move(self):
        if not self.history:
            return Move.NONE
        return self.previous_move
    
    def print_previous(self):
        print(f'Move: {self.previous_move}')