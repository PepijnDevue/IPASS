# imports
import Board
import menu
from constants import SQUARE_SIZE, PLAYER_BLACK, PLAYER_WHITE, PVP, PVE

def start_game(window, gameMode, maxDepth):
    """
    Initiate all necessary components for the game loop

    Args:
        window (Pyglet.window): The window object to display the board
        gameMode (string): The current game mode (PVE or PVP)
        maxDepth (int): The max ply for minimax
    """
    print(gameMode)
    board = Board.Board(maxDepth)
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
        nonlocal selected, highlighted, current_player, playing, board
        if playing:
            x = x//SQUARE_SIZE
            y = y//SQUARE_SIZE
            if gameMode == PVP or current_player == PLAYER_WHITE:
                if [x,y] in highlighted:
                    # make a move
                    selected, highlighted, current_player, playing = board.handlePlayerTurn(x, y, selected, current_player)
                    if gameMode == PVE and current_player == PLAYER_BLACK and playing:
                        # bot move
                        selected, highlighted, current_player, playing = board.handleBotTurn()
                else:
                    # select a square
                    selected, highlighted = board.selectNew(x, y, current_player)
        else:
            print(f"{current_player} lost")
            window.clear()
            menu.open_menu(window)