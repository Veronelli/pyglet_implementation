from typing import TYPE_CHECKING
from app.commons.types import PygletElement
from app.models.layers.static_layer import StaticLayer

if TYPE_CHECKING:
    from pyglet.graphics import Group

class EncapsuleLayer(StaticLayer):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        name: str,
        tags: list[str],
        order: int,
        group_instance: "Group"
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
            name=name,
            tags=tags,
            order=order,
            group_instance=group_instance
        )
        self._x = x
        self._y = y

        self._width = width
        self._height = height

    def _add_element(
        self,
        element: "PygletElement"
    ) -> "EncapsuleLayer":
        x = abs(element._x - self.x) + element.x
        y = abs(element._y - self.y) + element.y
        element.position = (x, y)
        return super()._add_element(
            element=element
        )

    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y
