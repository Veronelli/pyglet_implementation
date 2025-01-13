from app.commons.scsissor_group import ScissorGroup
from app.utils.colors.base import ColorRGB
from app.window import window, pyglet
from pyglet.shapes import Rectangle
from app.models.layers.layer_factory import factory_encapsule_layer

render_layer = ScissorGroup(
    x=30,
    y=30,
    width=500,
    height=400,
    order=1
)

my_layer = factory_encapsule_layer(
    x=30,
    y=30,
    width=500,
    height=400,
    name='my_layer',
    tags=['test'],
    order=10,
    group_type=ScissorGroup
)
square = Rectangle(
    x=50,
    y=50,
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
