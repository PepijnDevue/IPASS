# imports
from game import start_boardstate

class Board:
    """
    A board represents a game state at any given time

    board(array): 2D array representing all positions on the board
    """
    positions = start_boardstate()
    
    selected = (1,0)
    highlighted = [(2,0), (5,4)]