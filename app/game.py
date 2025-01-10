from app.window import window, pyglet
from app.models.layer import Layer
from pyglet.shapes import Rectangle

my_layer = Layer(name='my_layer', tags=['test'], order=0, width=500, height=300, x=20, y=100)
square = Rectangle(x=10, y=0, width=50, height=50, color=(255, 0, 0), batch=my_layer.batch, group=my_layer.group)
my_layer.append(element=square)

@window.event
def on_draw():
    window.clear()
    my_layer.draw()

def run():
    pyglet.app.run()
