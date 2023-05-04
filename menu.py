import pyglet
from constants import WINDOW_SIZE, BLACK, YELLOW, BUTTON_HEIGHT, BUTTON_WIDTH, GREY
from game import start_pve, start_pvp

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
            start_pvp()
        elif(x > pve_button.x and x < pve_button.x+pve_button.width and y > pve_button.y and y < pve_button.y+pve_button.height and button == pyglet.window.mouse.LEFT):
            start_pve()