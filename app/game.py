from app.window import window, pyglet
from app.models.layer import Layer
from pyglet.shapes import Rectangle

my_layer = Layer('my_layer', ['test'], 0)
square = Rectangle(100, 100, 100, 100, color=(255, 0, 0), batch=my_layer.batch, group=my_layer.group)
my_layer.add_element(square)

@window.event
def on_draw():
    window.clear()
    my_layer.draw()

def run():
    pyglet.app.run()
