# imports
from Piece import Piece
import pyglet
from constants import PLAYER_BLACK, PLAYER_WHITE, SQUARE_SIZE, BLACK, WHITE, PIECE, KING, HIGHLIGHT

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

    def drawHighlight(self, x:int, y:int):
        """
        Highlight a given square

        Args:
            x (int): X coordinate, 0-7
            y (int): Y coordinate, 0-7
        """
        pyglet.shapes.Rectangle(x=x*SQUARE_SIZE, y=y*SQUARE_SIZE, width=SQUARE_SIZE, height=SQUARE_SIZE, color=HIGHLIGHT)

    def drawPiece(self, x:int, y:int):
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

    def printPos(self, x:int, y:int):
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

    def getPieces(self, player:str):
        """
        Get all positions of the pieces of a player

        Args:
            player (str): Either "B" for black or "W" for white

        Returns:
            list[list]: The list of position
        """
        positions = []
        for x in range(8):
            for y in range(8):
                if(self.positions[y][x] != None and self.positions[y][x].player == player):
                    positions.append((x, y))
        return positions

    def possibleMoves(self, x:int, y:int, player:str):
        #TODO: fill in the passes (use recursion for multi-captures)
        current = self.positions[y][x]
        positions = []
        if(current == None):
            return self.getPieces(player)
        elif(current.type == PIECE):
            if current.player == WHITE:
                pass
            else:
                pass
        elif(current.player == WHITE):
            pass
        else:
            pass

    def showHighlights(self, selected:list, player:str):
        """
        TODO: write this

        Args:
            selected (list): _description_
            player (str): _description_
        """
        positions = self.possibleMoves(selected[0], selected[1], player)
        for pos in positions:
            self.drawHighlight(pos[0], pos[1])
