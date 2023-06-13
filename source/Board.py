# imports
from Piece import Piece
import pyglet
from constants import PLAYER_BLACK, PLAYER_WHITE, SQUARE_SIZE, BLACK, WHITE, PIECE, HIGHLIGHT, SELECT, BROWN, YELLOW

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
    def __init__(self) -> None:
        self.positions = start_boardstate()


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


    def draw(self):
        """
        Draw the background and contents of the board
        """
        for x in range(8):
            for y in range(8):
                if y%2 == x%2:
                    pyglet.shapes.Rectangle(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, BROWN).draw()
                else:
                    pyglet.shapes.Rectangle(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, YELLOW).draw()
                self.drawPiece(x, y)


    def drawSelected(self, x:int, y:int):
        """
        Highlight a given square, indicating selected square

        Args:
            x (int): X coordinate, 0-7
            y (int): Y coordinate, 0-7
        """
        pyglet.shapes.Rectangle(x=x*SQUARE_SIZE, y=y*SQUARE_SIZE, width=SQUARE_SIZE, height=SQUARE_SIZE, color=SELECT).draw()


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
            

    def getMoves(self, x:int, y:int, player:str):
        #TODO: fill in the king moves and the multi-captures(recursion)
        current_piece = self.positions[y][x]
        moves = []
        captures = []

        # None selected, movable pieces
        if(current_piece == None or current_piece.player != player):
            return moves, False
        
        # piece moves
        elif(current_piece.type == PIECE):
            if current_piece.player == PLAYER_WHITE:
                # move left-up
                if (self.withinBoard(x-1, y+1) and self.positions[y+1][x-1] == None):
                    moves.append([x-1, y+1])
                # move right-up
                if (self.withinBoard(x+1, y+1) and self.positions[y+1][x+1] == None):
                    moves.append([x+1, y+1])
                # (multi)capture left-up
                if (self.withinBoard(x-2, y+2) and self.positions[y+1][x-1] != None and self.positions[y+1][x-1].player == PLAYER_BLACK and self.positions[y+2][x-2] == None):
                    captures.append([x-2, y+2])
                # (multi)capture right-up
                if (self.withinBoard(x+2, y+2) and self.positions[y+1][x+1] != None and self.positions[y+1][x+1].player == PLAYER_BLACK and self.positions[y+2][x+2] == None):
                    captures.append([x+2, y+2])
                # (multi)capture left-down
                if (self.withinBoard(x-2, y-2) and self.positions[y-1][x-1] != None and self.positions[y-1][x-1].player == PLAYER_BLACK and self.positions[y-2][x-2] == None):
                    captures.append([x-2, y-2])
                # (multi)capture right-down
                if (self.withinBoard(x+2, y-2) and self.positions[y-1][x+1] != None and self.positions[y-1][x+1].player == PLAYER_BLACK and self.positions[y-2][x+2] == None):
                    captures.append([x+2, y-2])
            else:
                # move left-down
                if (self.withinBoard(x-1, y-1) and self.positions[y-1][x-1] == None):
                    moves.append([x-1, y-1])
                # move right-down
                if (self.withinBoard(x+1, y-1) and self.positions[y-1][x+1] == None):
                    moves.append([x+1, y-1])
                # (multi)capture left-up
                if (self.withinBoard(x-2, y+2) and self.positions[y+1][x-1] != None and self.positions[y+1][x-1].player == PLAYER_WHITE and self.positions[y+2][x-2] == None):
                    captures.append([x-2, y+2])
                # (multi)capture right-up
                if (self.withinBoard(x+2, y+2) and self.positions[y+1][x+1] != None and self.positions[y+1][x+1].player == PLAYER_WHITE and self.positions[y+2][x+2] == None):
                    captures.append([x+2, y+2])
                # (multi)capture left-down
                if (self.withinBoard(x-2, y-2) and self.positions[y-1][x-1] != None and self.positions[y-1][x-1].player == PLAYER_WHITE and self.positions[y-2][x-2] == None):
                    captures.append([x-2, y-2])
                # (multi)capture right-down
                if (self.withinBoard(x+2, y-2) and self.positions[y-1][x+1] != None and self.positions[y-1][x+1].player == PLAYER_WHITE and self.positions[y-2][x+2] == None):
                    captures.append([x+2, y-2])

        # king moves   
        elif(current_piece.player == PLAYER_WHITE):
            pass
        
        else:
            pass
        
        # you have to capture if you can
        if len(captures) != 0:
            return captures, True
        return moves, False
    

    def possibleMoves(self, x:int, y:int, player:str):
        """
        Get all possible/legal moves a piece can make
        Will only return the capturing moves if the piece can capture
        Will return nothing if the piece cant capture but another piece can

        Args:
            x (int): The x coordinate of the piece
            y (int): The y coordinate of the piece
            player (str): The current player

        Returns:
            list: The x and y coordinates of all moves the player can make
        """
        moves, capturing = self.getMoves(x, y, player)

        # you have to capture if you can
        if capturing:
            return moves
        
        # you cant move piece a when you can capture piece b
        canMove = True
        for piece in self.getPieces(player):
            if piece != [x, y] and self.getMoves(piece[0], piece[1], player)[1] == True:
                canMove = False
        if canMove:
            return moves
        else:
            return []
        

    def showHighlights(self, selected:list, player:str):
        """
        show all possible inputs a player can make

        Args:
            selected (list): (x, y) coordinates of the selected square
            player (str): Either B or W
        """
        positions = self.possibleMoves(selected[0], selected[1], player)
        for pos in positions:
            pyglet.shapes.Rectangle(x=pos[0]*SQUARE_SIZE, 
                                    y=pos[1]*SQUARE_SIZE, 
                                    width=SQUARE_SIZE, 
                                    height=SQUARE_SIZE, 
                                    color=HIGHLIGHT).draw()
            

    def handleTurn(self, x:int, y:int, selected:list, current_player:str):
        """
        Handle a turn being played, could be a move, a capture or a multi-capture

        Args:
            x (int): The x position of the target square
            y (int): The y position of the target square
            selected (list): The x and y coordinates of the moving piece
            current_player (str): The current player

        Returns:
            list: The new selected square
            list: Empty list representing the highlighted squares
            str: The next player
            bool: Whether or not the game is still going
        """
        # make the move
        self.move(selected[0], selected[1], x, y)

        # prepare next turn
        playing = True
        if current_player == PLAYER_WHITE:
            # check if white has won
            if len(self.getPieces(PLAYER_BLACK)) == 0:
                playing = False

            current_player = PLAYER_BLACK
            selected = [0, 7]
        else:
            # check if black has won
            if len(self.getPieces(PLAYER_WHITE)) == 0:
                playing = False
            current_player = PLAYER_WHITE
            selected = [7, 0]

        return selected, [],  current_player, playing  


    def selectNew(self, x:int, y:int, current_player:str):
        """
        Select a new square

        Args:
            x (int): The x position of the newly selected square
            y (int): The y position of the newly selected square
            current_player (str): The current player

        Returns:
            list: The x and y position of the newly selected square
            list: The positions of the newly highlighted squares
        """
        selected = [x, y]
        highlighted = self.possibleMoves(x, y, current_player)
        return selected, highlighted

    def move(self, xOld:int, yOld:int, xNew:int, yNew:int):
        """
        Make a move (capture or normal move)

        Args:
            xOld (int): Old x position
            yOld (int): Old y position
            xNew (int): New x position
            yNew (int): New y position
        """
        self.positions[yNew][xNew] = self.positions[yOld][xOld]
        self.positions[yOld][xOld] = None
        
        # single capture
        if abs(xOld-xNew) == 2:
            self.positions[(yNew+yOld)//2][(xNew+xOld)//2] = None
