import pyglet
from constants import WINDOW_SIZE
import menu

if __name__ == '__main__':
    window = pyglet.window.Window(WINDOW_SIZE, WINDOW_SIZE, "Dammen")
    menu.open_menu(window)
    pyglet.app.run()