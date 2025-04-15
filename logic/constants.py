from enum import Enum

# Screen and square sizes
SCREEN_SIZE = 640, 640
SQUARE_SIZE = 80
OUTLINE_SIZE = 8
OUTLINE_SQUARE_SIZE = SQUARE_SIZE + OUTLINE_SIZE

# Pieces

# Team
class Team(Enum):
    WHITE = 0
    BLACK = 1

# Piece Type
class Type(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5

# Move Type
class Move(Enum):
    NONE = 0    
    NORMAL = 1
    LEFT_CASTLE = 2
    RIGHT_CASTLE = 3
    EN_PASSANT = 4
    PAWN_DOUBLE = 5

FIRST = 0
LAST = 7

# Images for pieces
PNGS = {
    Type.PAWN: ["assets/white_pawn.png", "assets/black_pawn.png"],
    Type.KNIGHT: ["assets/white_knight.png", "assets/black_knight.png"],
    Type.BISHOP: ["assets/white_bishop.png", "assets/black_bishop.png"],
    Type.ROOK: ["assets/white_rook.png", "assets/black_rook.png"],
    Type.QUEEN: ["assets/white_queen.png", "assets/black_queen.png"],
    Type.KING: ["assets/white_king.png", "assets/black_king.png"]
}

# Colors
GRAY = 140, 140, 140, 160
LIGHT_BROWN = 236, 236, 208, 255
DARK_BROWN = 181, 136, 95, 255
# redHighlight(243, 60, 66, 255),
# 	yellowHighlight(246, 246, 129, 255),
# 	textHighlight(143, 107, 74, 255),