# imports
import Board
import menu
from constants import SQUARE_SIZE, PLAYER_BLACK, PLAYER_WHITE, PVP, PVE, PLAYER, BOT


def start_pvp(window):
    """
    Initiate all necessary components for the game loop

    Args:
        window (Pyglet.window): The window object to display the board
    """
    board = Board.Board()
    current_player = PLAYER_WHITE
    playing = True
    selected = [7,0]
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
            if [x,y] in highlighted:
                # make a move
                selected, highlighted, current_player, playing = board.handlePlayerTurn(x, y, selected, current_player)
            else:
                # select a square
                selected, highlighted = board.selectNew(x, y, current_player)
        else:
            print(f"{current_player} lost")
            window.clear()
            menu.open_menu(window)


def start_pve(window, starting_player, maxDepth=1):
    """
    Initiate all necessary components for the game loop

    Args:
        window (Pyglet.window): The window object to display the board
        starting_player (string): The starting entity (PLAYER or BOT)
        maxDepth (int): The max ply for minimax
    """
    board = Board.Board(maxDepth)
    current_player = PLAYER_WHITE
    playing = True
    selected = [7,0]
    highlighted = []
    waitFrame = True
    
    if starting_player == BOT:
        bot_player = PLAYER_WHITE
        selected, highlighted, current_player, playing = board.handleBotTurn(current_player)
    else:
        bot_player = PLAYER_BLACK


    @window.event
    def on_draw():
        """
        Pyglet on_draw function will trigger every frame
        """
        nonlocal highlighted, selected, current_player, playing, board, waitFrame
        window.clear()
        board.draw()
        board.showHighlights(selected, current_player)
        board.drawSelected(selected[0], selected[1])
        if current_player == bot_player and playing:
            if not waitFrame:
                # bot move
                selected, highlighted, current_player, playing = board.handleBotTurn(current_player)
                waitFrame = True
            else:
                waitFrame = False

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
            if current_player != bot_player:
                if [x,y] in highlighted:
                    # make a move
                    selected, highlighted, current_player, playing = board.handlePlayerTurn(x, y, selected, current_player)
                else:
                    # select a square
                    selected, highlighted = board.selectNew(x, y, current_player)
        else:
            print(f"{current_player} lost")
            window.clear()
            menu.open_menu(window)