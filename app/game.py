from app.commons.scsissor_group import ScissorGroup
from app.models.layers.encapsule_layer import EncapsuleLayer
from app.models.layers.static_layer import StaticLayer
from app.utils.colors.base import ColorRGB
from app.window import window, pyglet
from pyglet.shapes import Rectangle

render_layer = ScissorGroup(
    x=30,
    y=30,
    width=500,
    height=400,
    order=1
)

my_layer = EncapsuleLayer(
    x=30.0,
    y=30.0,
    width=500,
    height=400,
    name='my_layer',
    tags=['test'],
    order=10,
    group_instance=render_layer
)
square = Rectangle(
    x=-60.0,
    y=10,
    width=100,
    height=100,
    color=ColorRGB.RED, 
)
my_layer.append(element=square)

@window.event
def on_draw()-> None:
    window.clear()
    my_layer.draw()

def run() -> None:
    pyglet.app.run()
