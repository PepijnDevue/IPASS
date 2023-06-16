# imports
from Piece import Piece
import pyglet
import numpy as np
import copy
import random
from constants import PLAYER_BLACK, PLAYER_WHITE, SQUARE_SIZE, BLACK, WHITE, PIECE, KING, HIGHLIGHT, SELECT, BROWN, YELLOW

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

    positions(list): 2D list representing all positions on the board
    mandatoryMove(None/list): If a player is capturing multiple pieces in one turn, this variable will contain the position of the piece that is multi-capturing
    """
    def __init__(self, maxDepth) -> None:
        """
        Initiate a board object

        Args:
            maxDepth (int): The max ply for minimax
        """
        self.positions = start_boardstate()
        #TODO: bug, player cant capture more than 2 times at once
        self.mandatoryMove = None
        self.maxDepth = maxDepth


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
            if piece.type == KING:
                pyglet.shapes.Star(x=x*SQUARE_SIZE+SQUARE_SIZE//2, 
                                   y=y*SQUARE_SIZE+SQUARE_SIZE//2, 
                                   outer_radius=SQUARE_SIZE//4, 
                                   inner_radius=SQUARE_SIZE//8, 
                                   num_spikes=5, rotation=-90,
                                   color=WHITE).draw()
            
        elif piece.player == PLAYER_WHITE:
            pyglet.shapes.Circle(x=x*SQUARE_SIZE+SQUARE_SIZE//2,
                                 y=y*SQUARE_SIZE+SQUARE_SIZE//2, 
                                 radius=SQUARE_SIZE//3, color=WHITE).draw()
            if piece.type == KING:
                pyglet.shapes.Star(x=x*SQUARE_SIZE+SQUARE_SIZE//2, 
                                   y=y*SQUARE_SIZE+SQUARE_SIZE//2, 
                                   outer_radius=SQUARE_SIZE//4, 
                                   inner_radius=SQUARE_SIZE//8, 
                                   num_spikes=5, rotation=-90, 
                                   color=BLACK).draw()


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
        """
        Get all legal moves a piece can make and tell if the piece can capture or not

        Args:
            x (int): The x position of the piece
            y (int): The y position fo the piece
            player (str): The current player

        Returns:
            list: A list of coordinates the piece can move to
            bool: True if the piece is capturing
        """

        #TODO: fill in the king moves and its multi-captures
        current_piece = self.positions[y][x]
        moves = []
        captures = []

        # None selected or opposite player's piece selected
        if(current_piece == None or current_piece.player != player):
            return moves, False
        
        # In the middle of a multi-capture and this piece is not the capturing piece
        elif(self.mandatoryMove != None and self.mandatoryMove != [x, y]):
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
                # capture left-up
                if (self.withinBoard(x-2, y+2) and self.positions[y+1][x-1] != None and self.positions[y+1][x-1].player == PLAYER_BLACK and self.positions[y+2][x-2] == None):
                    captures.append([x-2, y+2])
                # capture right-up
                if (self.withinBoard(x+2, y+2) and self.positions[y+1][x+1] != None and self.positions[y+1][x+1].player == PLAYER_BLACK and self.positions[y+2][x+2] == None):
                    captures.append([x+2, y+2])
                # capture left-down
                if (self.withinBoard(x-2, y-2) and self.positions[y-1][x-1] != None and self.positions[y-1][x-1].player == PLAYER_BLACK and self.positions[y-2][x-2] == None):
                    captures.append([x-2, y-2])
                # capture right-down
                if (self.withinBoard(x+2, y-2) and self.positions[y-1][x+1] != None and self.positions[y-1][x+1].player == PLAYER_BLACK and self.positions[y-2][x+2] == None):
                    captures.append([x+2, y-2])
            else:
                # move left-down
                if (self.withinBoard(x-1, y-1) and self.positions[y-1][x-1] == None):
                    moves.append([x-1, y-1])
                # move right-down
                if (self.withinBoard(x+1, y-1) and self.positions[y-1][x+1] == None):
                    moves.append([x+1, y-1])
                # capture left-up
                if (self.withinBoard(x-2, y+2) and self.positions[y+1][x-1] != None and self.positions[y+1][x-1].player == PLAYER_WHITE and self.positions[y+2][x-2] == None):
                    captures.append([x-2, y+2])
                # capture right-up
                if (self.withinBoard(x+2, y+2) and self.positions[y+1][x+1] != None and self.positions[y+1][x+1].player == PLAYER_WHITE and self.positions[y+2][x+2] == None):
                    captures.append([x+2, y+2])
                # capture left-down
                if (self.withinBoard(x-2, y-2) and self.positions[y-1][x-1] != None and self.positions[y-1][x-1].player == PLAYER_WHITE and self.positions[y-2][x-2] == None):
                    captures.append([x-2, y-2])
                # capture right-down
                if (self.withinBoard(x+2, y-2) and self.positions[y-1][x+1] != None and self.positions[y-1][x+1].player == PLAYER_WHITE and self.positions[y-2][x+2] == None):
                    captures.append([x+2, y-2])

        else:
            # king moves   
            if(current_piece.player == PLAYER_WHITE):
                opp = PLAYER_BLACK
            else:
                opp = PLAYER_WHITE
            # move/capture left up
            delta = 1
            capturing = False

            while True:
                if self.withinBoard(x-delta, y+delta):

                    pos = self.positions[y+delta][x-delta]
                    if pos == None:

                        if capturing:
                            captures.append([x-delta, y+delta])
                        else:
                            moves.append([x-delta, y+delta])

                    elif pos.player == opp:

                        if capturing:
                            break
                        else:
                            capturing = True

                    else:
                        break

                else:
                    break
                delta += 1

            # move/capture right up
            delta = 1
            capturing = False

            while True:
                if self.withinBoard(x+delta, y+delta):

                    pos = self.positions[y+delta][x+delta]
                    if pos == None:

                        if capturing:
                            captures.append([x+delta, y+delta])
                        else:
                            moves.append([x+delta, y+delta])

                    elif pos.player == opp:

                        if capturing:
                            break
                        else:
                            capturing = True

                    else:
                        break
                    
                else:
                    break
                delta += 1

            # move/capture left down
            delta = 1
            capturing = False

            while True:
                if self.withinBoard(x-delta, y-delta):

                    pos = self.positions[y-delta][x-delta]
                    if pos == None:

                        if capturing:
                            captures.append([x-delta, y-delta])
                        else:
                            moves.append([x-delta, y-delta])

                    elif pos.player == opp:

                        if capturing:
                            break
                        else:
                            capturing = True

                    else:
                        break
                    
                else:
                    break
                delta += 1

            # move/capture right down
            delta = 1
            capturing = False

            while True:
                if self.withinBoard(x+delta, y-delta):

                    pos = self.positions[y-delta][x+delta]
                    if pos == None:

                        if capturing:
                            captures.append([x+delta, y-delta])
                        else:
                            moves.append([x+delta, y-delta])

                    elif pos.player == opp:

                        if capturing:
                            break
                        else:
                            capturing = True

                    else:
                        break
                    
                else:
                    break
                delta += 1
        
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
        
        # you cant move piece A when you can capture with piece B
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
            

    def handlePlayerTurn(self, x:int, y:int, selected:list, current_player:str):
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

        # let the player capture again if multi-capture is possible
        nextMove = self.possibleMoves(x, y, current_player)
        if abs(selected[0] - x) == 2 and len(nextMove) != 0 and abs(nextMove[0][0] - x) == 2:
            nextTurn = False
        else:
            nextTurn = True

        # prepare next turn
        highlighted = []
        playing = True
        if current_player == PLAYER_WHITE:
            # check if white has won
            tempMandatoryMove = self.mandatoryMove
            self.mandatoryMove = None
            if self.numPossibleMoves(PLAYER_BLACK) == 0:
                playing = False
            self.mandatoryMove = tempMandatoryMove

            # finish the turn if no multi-capture is possible
            if nextTurn:
                current_player = PLAYER_BLACK
                selected = [0, 7]
                self.mandatoryMove = None
            else:
                selected = [x, y]
                highlighted = self.possibleMoves(x, y, current_player)
                self.mandatoryMove = [x, y]
        else:
            # check if black has won
            tempMandatoryMove = self.mandatoryMove
            self.mandatoryMove = None
            if self.numPossibleMoves(PLAYER_WHITE) == 0:
                playing = False
            self.mandatoryMove = tempMandatoryMove

            # finish the turn if no multi-capture is possible
            if nextTurn:
                current_player = PLAYER_WHITE
                selected = [7, 0]
                self.mandatoryMove = None
            else:
                selected = [x, y]
                highlighted = self.possibleMoves(x, y, current_player)
                self.mandatoryMove = [x, y]

        return selected, highlighted,  current_player, playing  

    
    def handleBotTurn(self):
        """
        Let the bot take a turn

        Returns:
            list: The position of the default selected square of the player
            list: Empty list of highlighted square positions
            str: The next player, always PLAYER_WHITE
            bool: Whether or not the game has ended
        """
        bestScore = np.inf
        bestPositionsList = []

        print("----------------------------")
        # get best move according to minimax
        for piece in self.getPieces(PLAYER_BLACK):
            for move in self.possibleMoves(piece[0], piece[1], PLAYER_BLACK):

                # create copy of the board to simulate turns
                tempBoard = copy.deepcopy(self)
                tempBoard.move(piece[0], piece[1], move[0], move[1])

                # let the bot capture again if multi-capture is possible
                while True:
                    nextMoves = tempBoard.possibleMoves(move[0], move[1], PLAYER_BLACK)
                    if abs(piece[0] - move[0]) == 2 and len(nextMoves) != 0 and abs(nextMoves[0][0] - move[0]) == 2:
                        # TODO: find a way to implement minimax here
                        nextMove = nextMoves[0]
                        tempBoard.move(move[0], move[1], nextMove[0], nextMove[1])
                        piece = move
                        move = nextMove
                    else:
                        break
                
                # get the score of the move
                score = tempBoard.minimax(0)
                print(score)

                # if this is the best move yet, remember it
                if score < bestScore:
                    bestScore = score
                    bestPositionsList = [tempBoard.positions,]
                elif score == bestScore:
                    bestPositionsList.append(tempBoard.positions)

        print("-------------------", bestScore, "----------------------------")
        self.positions = random.choice(bestPositionsList)

        # check if black has won
        playing = True
        if self.numPossibleMoves(PLAYER_WHITE) == 0:
                playing = False

        return [7,0], [], PLAYER_WHITE, playing
    

    def minimax(self, depth):
        """
        Use recursion to find out what the score of a boardstate is

        Args:
            depth (int): The current search-depth

        Returns:
            int: The score of the boardstate
        """
        #TODO: Verify it works (I think its not optimal due to the absence of minimax in multi-captures)
        #TODO: Make faster(AlphaBetaaaaaaa, Make subfunctions faster)
        if depth % 2 == 0:
            # maximizing
            # current boardstate(self) is directly after black has moved
            movingPlayer = PLAYER_WHITE
            bestScore = -np.inf
            if self.numPossibleMoves(PLAYER_WHITE) == 0:
                # Black wins
                return -100
        else:
            # minimizing
            # current boardstate(self) is directly after black has moved
            movingPlayer = PLAYER_BLACK
            bestScore = np.inf
            if self.numPossibleMoves(PLAYER_BLACK) == 0:
                return 100
            
        if depth == self.maxDepth:
            # Recursion depth found
            return self.estimateScore()

        for piece in self.getPieces(movingPlayer):
            for move in self.possibleMoves(piece[0], piece[1], movingPlayer):

                # create copy of the board to simulate turns
                tempBoard = copy.deepcopy(self)
                tempBoard.move(piece[0], piece[1], move[0], move[1])

                # let the bot capture again if multi-capture is possible
                while True:
                    nextMoves = tempBoard.possibleMoves(move[0], move[1], PLAYER_BLACK)
                    if abs(piece[0] - move[0]) == 2 and len(nextMoves) != 0 and abs(nextMoves[0][0] - move[0]) == 2:
                        # TODO: find a way to implement minimax here (Choose 3capture over 2capture/create separate branch for each nextMove)
                        nextMove = nextMoves[0]
                        tempBoard.move(move[0], move[1], nextMove[0], nextMove[1])
                        piece = move
                        move = nextMove
                    else:
                        break
                
                # get the score of the move
                score = tempBoard.minimax(depth+1)

                if depth % 2 == 0:
                    if score > bestScore:
                        bestScore = score
                else:
                    if score < bestScore:
                        bestScore = score

        return bestScore


    def numPossibleMoves(self, player:str):
        """
        Get the amount of moves a player can make

        Args:
            player (str): The current player

        Returns:
            int: Amount of moves the player can make
        """
        pieces = self.getPieces(player)
        total = 0
        for piece in pieces:
            total += len(self.possibleMoves(piece[0], piece[1], player))
        return total


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
        
        if self.positions[yNew][xNew].type == PIECE:

            # piece capture
            if abs(xOld-xNew) == 2:
                self.positions[(yNew+yOld)//2][(xNew+xOld)//2] = None
        
        else:
            # king capture
            dirX = 1 if (xNew-xOld)>0 else -1
            dirY = 1 if (yNew-yOld)>0 else -1
            while(xOld+dirX!=xNew):
                xOld += dirX
                yOld += dirY
                self.positions[yOld][xOld] = None

        # transform to king
        if (yNew == 7 and self.positions[yNew][xNew].player == PLAYER_WHITE) or (yNew == 0 and self.positions[yNew][xNew].player == PLAYER_BLACK):
            self.positions[yNew][xNew].type = KING
    
    def estimateScore(self):
        """
        Estimate the score of a board state

        Returns:
            int: the score, positive = good for white, negative = good for black
        """
        # TODO: Improve? Only when kings and multi-captures are implemented well
        score = 0
        for x in range(8):
            for y in range(8):
                pos = self.positions[y][x]
                if pos == None:
                    pass
                else:
                    if pos.player == PLAYER_WHITE:
                        multiplier = 1
                    else:
                        multiplier = -1
                    if pos.type == PIECE:
                        score += multiplier*1
                    else:
                        score += multiplier*2
        return score

