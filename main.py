import pyglet

WINDOW_SIZE = 720
SQUARE_SIZE = WINDOW_SIZE//90

BUTTON_WIDTH = 180
BUTTON_HEIGHT = 60

YELLOW = (238, 255, 204)
GREY = (155, 155, 155)
BLACK = (0,0,0,255)

def start_pvp():
    print("PVP")

def start_pve():
    print("PVE")

def open_menu(window):
    """
    Open the menu page where the player can choose the gamemode, pvp or pve

    Args:
        window (pyglet.window.Window): The window in which the menu should be displayed
    """
    title = pyglet.text.Label('Dammen',font_size=54, x=WINDOW_SIZE//2, y=WINDOW_SIZE//1.3, anchor_x='center', anchor_y='center', color=BLACK)
    menu_background = pyglet.shapes.Rectangle(x=0, y=0, width=WINDOW_SIZE, height=WINDOW_SIZE, color=YELLOW)

    pve_button = pyglet.shapes.Rectangle(x=WINDOW_SIZE//2-BUTTON_WIDTH//2, y=WINDOW_SIZE//2-BUTTON_HEIGHT//2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,color=GREY)
    pve_label = pyglet.text.Label('1 Speler', font_size=28, x=WINDOW_SIZE//2, y=WINDOW_SIZE//2+5, anchor_x='center', anchor_y='center', color=BLACK)

    pvp_button = pyglet.shapes.Rectangle(x=WINDOW_SIZE//2-BUTTON_WIDTH//2, y=WINDOW_SIZE//3-BUTTON_HEIGHT//2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,color=GREY)
    pvp_label = pyglet.text.Label('2 Spelers', font_size=28, x=WINDOW_SIZE//2, y=WINDOW_SIZE//3+5, anchor_x='center', anchor_y='center', color=BLACK)

    @window.event
    def on_draw():
        window.clear()
        menu_background.draw()
        title.draw()
        pvp_button.draw()
        pve_button.draw()
        pvp_label.draw()
        pve_label.draw()
        

    @window.event
    def on_mouse_press(x,y, button, modifiers):
        if(x > pvp_button.x and x < pvp_button.x+pvp_button.width and y > pvp_button.y and y < pvp_button.y+pvp_button.height and button == pyglet.window.mouse.LEFT):
            print("PVP")
        elif(x > pve_button.x and x < pve_button.x+pve_button.width and y > pve_button.y and y < pve_button.y+pve_button.height and button == pyglet.window.mouse.LEFT):
            print("PVE")
        

# def open_game(game_mode):
#     window = pyglet.window.Window(WINDOW_SIZE, WINDOW_SIZE, "Dammen spel")

#     background = pyglet.shapes.Rectangle(x=0, y=0, width=WINDOW_SIZE, height=WINDOW_SIZE, color=YELLOW)

#     #draw black squares
#     black_squares = []
#     for x in range(8):
#         for y in range(8):
#             if(x//2 == y//2):
#                 black_squares.append(pyglet.shapes.Rectangle(x=x*SQUARE_SIZE,y=y*SQUARE_SIZE, width=SQUARE_SIZE, height=SQUARE_SIZE, color=(0,0,0)))

#     @window.event
#     def on_draw():
#         window.clear()
#         background.draw()
#         for square in black_squares:
#             square.draw()

if __name__ == '__main__':
    window = pyglet.window.Window(WINDOW_SIZE, WINDOW_SIZE, "Dammen")
    open_menu(window)
    pyglet.app.run()