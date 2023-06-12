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
                # make the move
                board.move(selected[0], selected[1], x, y)

                # prepare next turn
                highlighted = []
                if current_player == PLAYER_WHITE:
                    # check if white has won
                    if len(board.getPieces(PLAYER_BLACK)) == 0:
                        playing = False

                    current_player = PLAYER_BLACK
                    selected = [0, 7]
                else:
                    # check if black has won
                    if len(board.getPieces(PLAYER_WHITE)) == 0:
                        playing = False
                    current_player = PLAYER_WHITE
                    selected = [7, 0]
            else:
                # select a square
                board.printPos(x, y)
                selected = [x, y]
                highlighted = board.possibleMoves(selected[0], selected[1], current_player)
            print(f"Player: {current_player}, Highlighted: {highlighted}")
        else:
            print(f"{current_player} lost")
            window.clear()
            menu.open_menu(window)