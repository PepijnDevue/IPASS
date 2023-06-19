# imports
import pyglet
from constants import WINDOW_SIZE, BLACK, YELLOW, BUTTON_HEIGHT, BUTTON_WIDTH, GREY, PVE, PVP
from game import start_game

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

    # display a button for PvE
    pve_button = pyglet.shapes.Rectangle(x=WINDOW_SIZE//2-BUTTON_WIDTH//2, y=WINDOW_SIZE //
                                         2-BUTTON_HEIGHT//2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, color=GREY)
    pve_label = pyglet.text.Label('1 Speler', font_size=28, x=WINDOW_SIZE//2,
                                  y=WINDOW_SIZE//2+5, anchor_x='center', anchor_y='center', color=BLACK)

    # display a button for PvP
    pvp_button = pyglet.shapes.Rectangle(x=WINDOW_SIZE//2-BUTTON_WIDTH//2, y=WINDOW_SIZE //
                                         3-BUTTON_HEIGHT//2, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, color=GREY)
    pvp_label = pyglet.text.Label('2 Spelers', font_size=28, x=WINDOW_SIZE//2,
                                  y=WINDOW_SIZE//3+5, anchor_x='center', anchor_y='center', color=BLACK)

    @window.event
    def on_draw():
        """
        Draw all attributes to the screen after clearing the window
        """
        window.clear()
        menu_background.draw()
        title.draw()
        pvp_button.draw()
        pve_button.draw()
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
        # if the click position was within the PvP button
        if (x > pvp_button.x and x < pvp_button.x+pvp_button.width and y > pvp_button.y and y < pvp_button.y+pvp_button.height and button == pyglet.window.mouse.LEFT):
            start_game(window, PVP)
        # else if the click position was within the PvE button
        elif (x > pve_button.x and x < pve_button.x+pve_button.width and y > pve_button.y and y < pve_button.y+pve_button.height and button == pyglet.window.mouse.LEFT):
            start_game(window, PVE, 3)