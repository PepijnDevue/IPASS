import Board
import pyglet
from constants import SQUARE_SIZE, YELLOW, BROWN, PVE, PVP, PLAYER_BLACK, PLAYER_WHITE

def start_game(window, gameMode):
    """
    Initiate all necessary components for the gameloop

    Args:
        window (Pyglet.window): The window object to display the board
        gameMode (string): The current game mode (PVE or PVP)
    """
    print(gameMode)
    board = Board.Board()
    current_player = PLAYER_WHITE
    selected = [0,0]
    highlighted = []

    @window.event
    def on_draw():
        window.clear()
        for x in range(8):
            for y in range(8):
                if y%2 == x%2:
                    pyglet.shapes.Rectangle(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, BROWN).draw()
                else:
                    pyglet.shapes.Rectangle(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, YELLOW).draw()
                board.drawPiece(x, y)
        board.showHighlights(selected, current_player)
        board.drawSelected(selected[0], selected[1])

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        nonlocal selected
        board.printPos(x//SQUARE_SIZE, y//SQUARE_SIZE)
        selected = [x//SQUARE_SIZE, y//SQUARE_SIZE]
        highlighted = board.possibleMoves(selected[0], selected[1], current_player)
        print(highlighted)