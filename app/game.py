from app.models.layers.static_layer import StaticLayer
from app.utils.colors.base import ColorRGB
from app.window import window, pyglet
from pyglet.shapes import Rectangle

my_layer = StaticLayer(
    x=100,
    y=100,
    width=500,
    height=300,
    name='my_layer',
    tags=['test'],
    order=0
)
square = Rectangle(x=100, y=100, width=50, height=50, color=ColorRGB.RED, batch=my_layer.batch, group=my_layer.group)
my_layer.append(element=square)

@window.event
def on_draw()-> None:
    window.clear()
    my_layer.draw()

def run() -> None:
    pyglet.app.run()
