# imports
from constants import START_BOARD
from game import start_boardstate

class Board:
    """
    A board represents a game state at any given time

    board(array): 2D array representing all positions on the board
    """
    board = start_boardstate()