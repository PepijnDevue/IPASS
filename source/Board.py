# imports
from Piece import Piece
from constants import PLAYER_BLACK, PLAYER_WHITE

def start_boardstate():
    """
    Generate the starting game state for the game 
    in format of a 2D array containing Piece objects

    return(array[8][8]): The starting game state of the game
    """
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            if y%2 == x%2:
                if y < 3:
                    board[y].append(Piece(PLAYER_WHITE))
                elif y > 4:
                    board[y].append(Piece(PLAYER_BLACK))
                else:
                    board[y].append(None)
            else:
                board[y].append(None)

    return board

class Board:
    """
    A board represents a game state at any given time

    board(array): 2D array representing all positions on the board
    """
    positions = start_boardstate()
    
    selected = ()
    highlighted = []