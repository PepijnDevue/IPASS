import pyglet
from pyglet.window import mouse

WINDOW_SIZE = 720
SQUARE_SIZE = WINDOW_SIZE//90

YELLOW = (238, 255, 204)

def open_menu():
    window = pyglet.window.Window(WINDOW_SIZE, WINDOW_SIZE, "Dammen menu")

    label = pyglet.text.Label('Dammen',font_size=54, x=WINDOW_SIZE//2, y=WINDOW_SIZE//1.3, anchor_x='center', anchor_y='center', color=(0,0,0,255))
    menu_background = pyglet.shapes.Rectangle(x=0, y=0, width=WINDOW_SIZE, height=WINDOW_SIZE, color=YELLOW)

    pvp_button = pyglet.shapes.Rectangle(x=WINDOW_SIZE//2, y=WINDOW_SIZE//2, color=(155,155,155), width=150, height=100)

    @window.event
    def on_draw():
        window.clear()
        menu_background.draw()
        label.draw()
        pvp_button.draw()

    @window.event
    def on_mouse_press(x,y, button, modifiers):
        print("Click!! X:", x, " Y:", y)

def open_game(game_mode):
    window = pyglet.window.Window(WINDOW_SIZE, WINDOW_SIZE, "Dammen spel")

    background = pyglet.shapes.Rectangle(x=0, y=0, width=WINDOW_SIZE, height=WINDOW_SIZE, color=YELLOW)

    #draw black squares
    black_squares = []
    for x in range(8):
        for y in range(8):
            if(x//2 == y//2):
                black_squares.append(pyglet.shapes.Rectangle(x=x*SQUARE_SIZE,y=y*SQUARE_SIZE, width=SQUARE_SIZE, height=SQUARE_SIZE, color=(0,0,0)))

    @window.event
    def on_draw():
        window.clear()
        background.draw()
        for square in black_squares:
            square.draw()

if __name__ == '__main__':
    open_menu()
    pyglet.app.run()