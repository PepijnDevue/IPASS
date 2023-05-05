class Square:
    """
    A square represents a given position on the checkers board

    selected(bool): Whether or not the player has selected the piece for moving
    highlight(bool): Whether or not a selected piece can be moved to this square
    contains(var): None if the square is empty, otherwise a Piece object
    """
    selected = False
    highlight = False
    def __init__(self, contains):
        self.contains = contains