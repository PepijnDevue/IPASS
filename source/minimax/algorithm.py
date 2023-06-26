# imports
from copy import deepcopy
from constants import PLAYER_BLACK, PLAYER_WHITE
from numpy import Inf



def minimax(self, depth:int, alpha:int, beta:int, isMaximizing:bool):
    """
    Use the minimax algorithm recursively to find out what the score of a boardstate is

    Args:
        depth (int): Current depth, counting down from maxDepth to 0
        alpha (int): The maximizing player's best option
        beta (int): The minimizing player's best option
        isMaximizing (bool): True if the current call is maximizing

    Returns:
        int: The score of the current state of the game
    """
    # Recursion depth found
    if depth == 0:
        return self.estimateScore()
    
    if isMaximizing:
        if self.numPossibleMoves(PLAYER_WHITE) == 0:
            # Black wins
            return -100
        movingPlayer = PLAYER_WHITE
        bestScore = -Inf

    else:
        if self.numPossibleMoves(PLAYER_BLACK) == 0:
            return 100
        movingPlayer = PLAYER_BLACK
        bestScore = Inf    

    # loop through all childnodes (all possible following turns)
    for piece in self.getPieces(movingPlayer):
        for move in self.possibleMoves(piece[0], piece[1], movingPlayer)[0]:

            # create copy of the board to simulate turns
            tempBoard = deepcopy(self)
            captured = tempBoard.move(piece[0], piece[1], move[0], move[1])

            # let the bot capture again if multi-capture is possible
            while True:
                nextMoves, capturing = tempBoard.possibleMoves(move[0], move[1], movingPlayer)
                if captured and len(nextMoves) != 0 and capturing:
                    nextMove = nextMoves[0]
                    captured = tempBoard.move(move[0], move[1], nextMove[0], nextMove[1])
                    move = nextMove
                else:
                    break
            
            # get the score of the move
            score = tempBoard.minimax(depth-1, alpha, beta, not isMaximizing)

            # save the score if it is the best yet
            if isMaximizing:
                if score > bestScore:
                    bestScore = score
                if score > alpha:
                    alpha = score

            else:
                if score < bestScore:
                    bestScore = score
                if score < beta:
                    beta = score

            # prune if beta's best option is worse than alpha's best option  
            if beta <= alpha:
                return bestScore

    return bestScore