# imports
from constants import PIECE

class Piece:
    """
    A piece represents a checkers piece or king

    type(char): P if piece, K if king
    player(char): W if white, B if black
    """
    type = PIECE
    def __init__(self, player):
        self.player = player