from pyglet.sprite import Sprite
from pyglet.shapes import ShapeBase
from pyglet.text import Label

__all__ = ('PygletElement',)

PygletElement = Sprite | ShapeBase | Label