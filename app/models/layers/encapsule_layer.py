from app.commons.math import sum_difference
from app.commons.types import PygletElement
from app.models.layers.static_layer import StaticLayer


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
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
            name=name,
            tags=tags,
            order=order
        )
        self._x = x
        self._y = y

        self._width = width
        self._height = height

    def _add_element(
        self,
        element: "PygletElement"
    ) -> "EncapsuleLayer":
        element.x = abs(self.x - element.x)
        element.y = abs(self.y - element.y)
        return super()._add_element(
            element=element
        )

    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y
