# PythonChess
A 2 player game of chess created with python and pygame

## Need to do:
- Create methods for en passant and castling (only for FEN sring)
- Create endings
- Check/Checkmate
- Create moves for when in check
- Create actual menus
- Change controls from keyboard to mouse

Castling: requires history of involved rook and king. Can be accomplished via a hasMovedBefore flag.

En Passant: Knowledge of the last move taken. Can be accommodated by retaining a lastMove data structure, or retaining the previous board state.

Fifty move rule: requires history of when the last capture or pawn move. Can be accomplished via a lastPawnMoveOrCapture counter

Threefold repetition: requires all previous board states since the last castle, pawn move or capture. A list of hashes of previous states may be an option. (Thanks dfeuer)