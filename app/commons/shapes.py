from pyglet.shapes import Line
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyglet.graphics import Batch, Group
    from typing import Optional


class RectangleBorder():
    def __init__(
            self,
            x: int,
            y: int,
            width: int,
            height: int,
            color: tuple[int, int, int],
            batch: "Optional[Batch]" = None,
            group: "Optional[Group]" = None,
            border: float = 1,
    ) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.color = color
        self.border = border
        self.batch = batch
        self.group = group
        self._create_border()

    def _create_border(self):
        self.lines = [
            Line(
                x=self.x,
                y=self.y,
                x2=self.x + self.width,
                y2=self.y,
                color=self.color,
                batch=self.batch,
                width=self.border,
                group=self.group
            ),
            Line(
                x=self.x,
                y=self.y,
                x2=self.x,
                y2=self.y + self.height,
                color=self.color,
                batch=self.batch,
                width=self.border,
                group=self.group
            ),
            Line(
                x=self.x + self.width,
                y=self.y,
                x2=self.x + self.width,
                y2=self.y + self.height,
                color=self.color,
                batch=self.batch,
                width=self.border,
                group=self.group
            ),
            Line(
                x=self.x,
                y=self.y + self.height,
                x2=self.x + self.width,
                y2=self.y + self.height,
                color=self.color,
                batch=self.batch,
                width=self.border,
                group=self.group
            )
        ]

    def update_vertices(self)->None:
        if len(self.lines) == 0:
            return
        self.lines[0].position = (self.x, self.y)
        self.lines[1].position = (self.x, self.y)
        self.lines[2].position = (self.x + self.width, self.y)
        self.lines[3].position = (self.x, self.y + self.height)

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        self._x = value
        self.update_vertices()

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        self._y = value
        self.update_vertices()

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        self._width = value
        self.update_vertices()

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        self._height = value
        self.update_vertices()