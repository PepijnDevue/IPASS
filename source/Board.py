# imports


def start_boardstate():
    """
    Generate the starting game state for the game 
    in format of a 2D array containing Piece objects

    return(array[8][8]): The starting game state of the game
    """
    board = []
    for y in range(8):
        for x in range(8):
            print(x, y)

    return board

class Board:
    """
    A board represents a game state at any given time

    board(array): 2D array representing all positions on the board
    """
    positions = start_boardstate()
    
    selected = ()
    highlighted = []