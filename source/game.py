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

def start_boardstate():
    """
    Generate the starting game state for the game 
    in format of a 2D array containing Piece objects

    return(array[8][8]): The starting game state of the game
    """
    return []

def start_pvp():
    print("PVP")

def start_pve():
    print("PVE")