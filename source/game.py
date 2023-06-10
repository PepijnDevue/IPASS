import Board
import pyglet
from constants import SQUARE_SIZE, YELLOW, BROWN

def draw_window(window, board):
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
                
    

def start_pvp(window):
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        board.printPos(x//SQUARE_SIZE, y//SQUARE_SIZE)

    print("PVP")
    board = Board.Board()
    draw_window(window, board)

def start_pve(window):
    @window.event
    def on_mouse_press(x, y, button, modifiers):
        board.printPos(x//SQUARE_SIZE, y//SQUARE_SIZE)

    print("PVE")
    board = Board.Board()
    draw_window(window, board)