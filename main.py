import pyglet
from pyglet.window import mouse

window = pyglet.window.Window(800, 800, "IPASS AI")

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event
def on_mouse_press(x,y, button, modifiers):
    print("Click!! X:", x, " Y:", y)


pyglet.app.run()