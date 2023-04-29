import pyglet
from pyglet.window import mouse

WIDTH, HEIGHT = 720, 720



window = pyglet.window.Window(WIDTH, HEIGHT, "IPASS AI")

label = pyglet.text.Label('Dammen',font_size=54, x=WIDTH//2, y=HEIGHT//1.3, anchor_x='center', anchor_y='center', color=(0,0,0,255))
menu_background = pyglet.shapes.Rectangle(x=0, y=0, width=WIDTH, height=HEIGHT, color=(238, 255, 204))

pvp_button = pyglet.shapes.Rectangle(x=WIDTH//2, y=HEIGHT//2, color=(155,155,155), width=150, height=100, anchor_position=(360,360))

@window.event
def on_draw():
    window.clear()
    menu_background.draw()
    label.draw()
    pvp_button.draw()

@window.event
def on_mouse_press(x,y, button, modifiers):
    print("Click!! X:", x, " Y:", y)


pyglet.app.run()