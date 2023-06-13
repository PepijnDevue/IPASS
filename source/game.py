# imports
import Board
import menu
import pyglet
from constants import SQUARE_SIZE, PLAYER_BLACK, PLAYER_WHITE

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
    playing = True
    selected = [0,0]
    highlighted = []

    @window.event
    def on_draw():
        """
        Pyglet on_draw function will trigger every frame
        """
        window.clear()
        board.draw()
        board.showHighlights(selected, current_player)
        board.drawSelected(selected[0], selected[1])

    @window.event
    def on_mouse_press(x:int, y:int, button, modifiers):
        """
        Pyglet on_mouse_press function will trigger every mouse click

        Args:
            x (int): The x coordinate of the window
            y (int): The y coordinate of the window
            button (pyglet.window.mouse): Pyglet object
            modifiers (pyglet.window.mouse): Pyglet object
        """
        nonlocal selected, highlighted, current_player, playing

        if playing:
            x = x//SQUARE_SIZE
            y = y//SQUARE_SIZE
            if [x,y] in highlighted:
                selected, highlighted, current_player, playing = board.handleTurn(x, y, selected, current_player)
            else:
                # select a square
                selected, highlighted = board.selectNew(x, y, current_player)
        else:
            print(f"{current_player} lost")
            window.clear()
            menu.open_menu(window)