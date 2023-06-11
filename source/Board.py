# imports
from Piece import Piece
import pyglet
from constants import PLAYER_BLACK, PLAYER_WHITE, SQUARE_SIZE, BLACK, WHITE, PIECE, KING

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
            # If the position is a black square, check if and which piece should be placed there
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

    def drawPiece(self, x, y):
        """
        Draw the contents of a square on the board

        Args:
            x (int): The x coordinate of the board 0-7
            y (int): The y coordinate of the board 0-7
        """
        piece = self.positions[y][x]
        if piece == None:
            return
        if piece.player == PLAYER_BLACK:
            pyglet.shapes.Circle(x=x*SQUARE_SIZE+SQUARE_SIZE//2, y=y*SQUARE_SIZE+SQUARE_SIZE//2, radius=SQUARE_SIZE//3, color=BLACK).draw()
        elif piece.player == PLAYER_WHITE:
            pyglet.shapes.Circle(x=x*SQUARE_SIZE+SQUARE_SIZE//2, y=y*SQUARE_SIZE+SQUARE_SIZE//2, radius=SQUARE_SIZE//3, color=WHITE).draw()

    def printPos(self, x, y):
        """
        Print the contents of a square in the cli

        Args:
            x (int): The x coordinate of the board 0-7
            y (int): The y coordinate of the board 0-7
        """
        piece = self.positions[y][x]
        if piece == None:
            print(None, x, y)
        elif piece.type == PIECE:
            if piece.player == PLAYER_WHITE:
                print("White piece", x, y)
            else:
                print("Black piece", x, y)
        else:
            if piece.player == PLAYER_WHITE:
                print("White king", x, y)
            else:
                print("Black king", x, y)

    def showHighlights(self, selected, board):
        if(selected == None or board.positions[selected[1]][selected[0]] == None):
            print("None")
        else:
            print("Not None")