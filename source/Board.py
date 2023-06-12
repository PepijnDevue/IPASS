# imports
from Piece import Piece
import pyglet
from constants import PLAYER_BLACK, PLAYER_WHITE, SQUARE_SIZE, BLACK, WHITE, PIECE, KING, HIGHLIGHT, SELECT

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
        Highlight a given square, indicating possible move

        Args:
            x (int): X coordinate, 0-7
            y (int): Y coordinate, 0-7
        """
        pyglet.shapes.Rectangle(x=x*SQUARE_SIZE, y=y*SQUARE_SIZE, width=SQUARE_SIZE, height=SQUARE_SIZE, color=HIGHLIGHT).draw()

    def drawSelected(self, x:int, y:int):
        """
        Highlight a given square, indicating selected square

        Args:
            x (int): X coordinate, 0-7
            y (int): Y coordinate, 0-7
        """
        pyglet.shapes.Rectangle(x=x*SQUARE_SIZE, y=y*SQUARE_SIZE, width=SQUARE_SIZE, height=SQUARE_SIZE, color=SELECT).draw()

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
            pyglet.shapes.Circle(x=x*SQUARE_SIZE+SQUARE_SIZE//2, 
                                 y=y*SQUARE_SIZE+SQUARE_SIZE//2, 
                                 radius=SQUARE_SIZE//3, color=BLACK).draw()
            
        elif piece.player == PLAYER_WHITE:
            pyglet.shapes.Circle(x=x*SQUARE_SIZE+SQUARE_SIZE//2,
                                 y=y*SQUARE_SIZE+SQUARE_SIZE//2, 
                                 radius=SQUARE_SIZE//3, color=WHITE).draw()

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
    
    def withinBoard(self, x:int, y:int):
        """
        Check whether or not the coordinates are within the playing field

        Args:
            x (int): X coordinate
            y (int): Y coordinate
        """
        return (x > -1 and x < 8 and y > -1 and y < 8)
            

    def possibleMoves(self, x:int, y:int, player:str):
        #TODO: fill in the if (use recursion for multi-captures)
        current_piece = self.positions[y][x]
        positions = []

        if(current_piece == None or current_piece.player != player):
            pieces = self.getPieces(player)
            for piece in pieces:
                leng = len(self.possibleMoves(piece[0], piece[1], player))
                if leng != 0:
                    positions.append(piece)
            return positions
        
        elif(current_piece.type == PIECE):
            if current_piece.player == PLAYER_WHITE:
                if (self.withinBoard(x-1, y+1) and self.positions[y+1][x-1] == None):
                    positions.append([x-1, y+1])
                if (self.withinBoard(x+1, y+1) and self.positions[y+1][x+1] == None):
                    positions.append([x+1, y+1])
                return positions
            else:
                if (self.withinBoard(x-1, y-1) and self.positions[y-1][x-1] == None):
                    positions.append([x-1, y-1])
                if (self.withinBoard(x+1, y-1) and self.positions[y-1][x+1] == None):
                    positions.append([x+1, y-1])
                return positions
            
        elif(current_piece.player == PLAYER_WHITE):
            return positions
        
        else:
            return positions

    def showHighlights(self, selected:list, player:str):
        """
        show all possible inputs a player can make

        Args:
            selected (list): (x, y) coordinates of the selected square
            player (str): Either B or W
        """
        positions = self.possibleMoves(selected[0], selected[1], player)
        for pos in positions:
            self.drawHighlight(pos[0], pos[1])
