# imports
import pyglet
from constants import WINDOW_SIZE, BLACK, YELLOW, BUTTON_HEIGHT, BUTTON_WIDTH, GREY, PVE, PVP
from game import start_game

def button_clicked(x:int, y:int, button:pyglet.shapes):
    """
    Tell whether or not x, y is within the boundaries of a given button

    Args:
        x (int): The x position of a mouseclick
        y (int): The y position of a mouseclick
        button (pyglet.shapes): The button object

    Returns:
        bool: True when the given button was clicked
    """
    return x > button.x and x < button.x+button.width and y > button.y and y < button.y+button.height

def open_menu(window):
    """
    Open the menu page where the player can choose the game mode, pvp or pve

    Args:
        window (pyglet.window.Window): The window in which the menu should be displayed
    """
    # display a title and background
    menu_background = pyglet.shapes.Rectangle(
        x=0, y=0, width=WINDOW_SIZE, height=WINDOW_SIZE, color=YELLOW)
    title = pyglet.text.Label('Dammen', font_size=54, x=WINDOW_SIZE//2,
                              y=WINDOW_SIZE//1.3, anchor_x='center', anchor_y='center', color=BLACK)
    middle_line = pyglet.shapes.Rectangle(x=358, y= 150, width=4, height=300, color=BLACK)

    # display a button for PvE
    pve_button = pyglet.shapes.Rectangle(x=90, y=390, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, color=GREY)
    pve_label = pyglet.text.Label('1 Speler', font_size=28, x=180,
                                  y=425, anchor_x='center', anchor_y='center', color=BLACK)
    
    # display a button for EvE
    eve_button = pyglet.shapes.Rectangle(x=440, y=390, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, color=GREY)
    eve_label = pyglet.text.Label('2 Bots', font_size=28, x=530,
                                  y=425, anchor_x='center', anchor_y='center', color=BLACK)

    # display a button for PvP
    pvp_button = pyglet.shapes.Rectangle(x=270, y=50, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, color=GREY)
    pvp_label = pyglet.text.Label('2 Spelers', font_size=28, x=360,
                                  y=85, anchor_x='center', anchor_y='center', color=BLACK)
    
    # PvE toggle button for who begins
    pve_toggle_button = pyglet.shapes.Rectangle(x=90, y=330, width=BUTTON_WIDTH, height=BUTTON_HEIGHT//1.4, color=GREY)
    pve_toggle_label = pyglet.text.Label('Speler begint', font_size=20, x=180,
                                  y=355, anchor_x='center', anchor_y='center', color=BLACK)
    pve_start = "PLAYER"

    @window.event
    def on_draw():
        """
        Draw all attributes to the screen after clearing the window
        """
        window.clear()
        menu_background.draw()
        title.draw()
        middle_line.draw()
        pvp_button.draw()
        pve_button.draw()
        eve_button.draw()
        pve_toggle_button.draw()
        pve_toggle_label.draw()
        eve_label.draw()
        pvp_label.draw()
        pve_label.draw()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        """
        Handle mouse clicks

        Args:
            x (int): The x position of the mouse when it was clicked
            y (int): The y position of the mouse when it was clicked
            button (pyglet.window.mouse): Which mouse button was clicked
            modifiers (?): Not used but demanded by pyglet
        """
        nonlocal pve_start
        if button_clicked(x, y, pvp_button):
            start_game(window, PVP)
        elif button_clicked(x, y, pve_button):
            start_game(window, PVE, 3)
        elif button_clicked(x, y, eve_button):
            print("Eve coming soon")
        elif button_clicked(x, y, pve_toggle_button):
            if pve_start == "PLAYER":
                pve_toggle_label.text = "Bot begint"
                pve_start = "BOT"
            else:
                pve_toggle_label.text = "Speler begint"
                pve_start = "PLAYER"
            print(pve_start)