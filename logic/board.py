import pygame

from pieces.piece import Team, Type, LAST, SQUARE_SIZE
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.sliding_piece import Sliding

"""
    Board indexes
    (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0)
    (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)
    (0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2)
    (0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3)
    (0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4)
    (0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5)
    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)
    (0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7)
"""


# Size of the screen
SCREEN_SIZE = 640, 640

# Colors
GRAY = 140, 140, 140, 160


# Main class for the chess board
class Board:
    # Creates the board
    def __init__(self) -> None:
        self.fen_to_board() #"r1bk3r/p2pBpNp/n4n2/1p1NP2P/6P1/3P4/P1P1K3/q5b1")

    # Creates board from the first arg of a FEN string
    def create_board(self, board: str) -> None:
        # Inits everything as None
        self.board = [[None for _ in range(8)] for _ in range(8)]

        rank = 0
        file = 0
        just_skipped = False # Doesn't skip twice in a row

        # Iterates over every char in board
        for char in board:
            # Checks if char is a number and skips that many squares
            if char.isnumeric():
                file += int(char)

                # Checks for end of rank and moves to the next
                if file > LAST:
                    file = 0
                    rank += 1
                    just_skipped = True

                continue
            elif char == 'p': # Black Pawn
                self.board[rank][file] = Pawn(Team.BLACK, Type.PAWN, (file, rank))
            elif char == 'n': # Black Knight
                self.board[rank][file] = Knight(Team.BLACK, Type.KNIGHT, (file, rank))
            elif char == 'b': # Black Bishop
                self.board[rank][file] = Sliding(Team.BLACK, Type.BISHOP, (file, rank))
            elif char == 'r': # Black Rook
                self.board[rank][file] = Sliding(Team.BLACK, Type.ROOK, (file, rank))
            elif char == 'q': # Black Queen
                self.board[rank][file] = Sliding(Team.BLACK, Type.QUEEN, (file, rank))
            elif char == 'k': # Black King
                self.board[rank][file] = King(Team.BLACK, Type.KING, (file, rank))
            elif char == 'P': # White Pawn
                self.board[rank][file] = Pawn(Team.WHITE, Type.PAWN, (file, rank))
            elif char == 'N': # White Knight
                self.board[rank][file] = Knight(Team.WHITE, Type.KNIGHT, (file, rank))
            elif char == 'B': # White Bishop
                self.board[rank][file] = Sliding(Team.WHITE, Type.BISHOP, (file, rank))
            elif char == 'R': # White Rook
                self.board[rank][file] = Sliding(Team.WHITE, Type.ROOK, (file, rank))
            elif char == 'Q': # White Queen
                self.board[rank][file] = Sliding(Team.WHITE, Type.QUEEN, (file, rank))
            elif char == 'K': # White King
                self.board[rank][file] = King(Team.WHITE, Type.KING, (file, rank))
            elif char == '/': # End of rank
                # Checks if number just ended rank
                if just_skipped:
                    just_skipped = False
                    continue

                file = 0
                rank += 1
                continue

            file += 1

    # Creates board and inits variables from FEN string
    def fen_to_board(self, fen: str="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1") -> None:        
        # Sets them to none is not given
        # Board is the board string; turn is the current playes turn;
        # en_passant is the square that can be en_passanted;
        # half move is for the 50 move rule; full move is move counter, increments 1 after blacks move
        board, turn, castle, en_passant, half_move, full_move = (fen.split() + [None] * 6)[:6]

        # Board
        self.create_board(board)
        
        # Turn
        self.players_turn = Team.BLACK if turn == 'b' else Team.WHITE

        # Castling
        # WIP

        # En Passant
        # WIP

        # Half Move
        self.half_move = half_move if not None else 0

        # Full Move
        self.full_move = full_move if not None else 0
        
    # Draws the pieces from the board to the surface; returns surface
    def draw_pieces(self) -> pygame.Surface:
        display = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
        display.fill((0,0,0,0))
        
        for row in self.board:
            for piece in row:
                if piece is None:
                    continue

                display.blit(piece.texture, piece.get_location())

        return display
    
    # Display moves for current selected piece; returns surface
    def piece_moves(self, pos: tuple) -> pygame.Surface:
        display = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
        display.fill((0,0,0,0))

        rank = pos[1]
        file = pos[0]

        # Skips if piece is None
        if self.board[rank][file] is None:
            return

        # Skips if piece is opposite team
        if self.board[rank][file].team != self.players_turn:
            return

        # Generates Moves
        self.moves = self.board[rank][file].generate_moves(self.board)
        
        # Skips if no moves found
        if self.moves is None:
            return
        
        # Goes thru each move and creates gray circle for each move
        for y, column in enumerate(self.moves):
            for x, move in enumerate(column):
                if move == 0:
                    continue
                pygame.draw.circle(display, GRAY, (x*SQUARE_SIZE + 40, y*SQUARE_SIZE + 40), 40)

        return display
    
    # Returns whether the pos is in the selected pieces moves or not
    def is_move(self, pos: tuple) -> bool:
        rank = pos[1]
        file = pos[0]

        return self.moves[rank][file] == 1
    
    # Moves a piece to new location
    def move_piece(self, new_pos: tuple, previous_pos: tuple) -> None:
        new_rank = new_pos[1]
        new_file = new_pos[0]

        previous_rank = previous_pos[1]
        previous_file = previous_pos[0]

        # Move piece
        self.board[new_rank][new_file] = self.board[previous_rank][previous_file]
        self.board[new_rank][new_file].location = new_pos

        # If pawn no longer first move
        if isinstance(self.board[new_rank][new_file], Pawn):
            self.board[new_rank][new_file].first_move = False
        
        # Sets old position to None
        self.board[previous_rank][previous_file] = None
        
        # Increments full move after each black move
        if self.players_turn == Team.BLACK:
            self.full_move += 1