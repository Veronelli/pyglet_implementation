
from typing import TYPE_CHECKING
from pyglet.graphics import Batch, Group


if TYPE_CHECKING:
    from app.commons.types import PygletElement


class BaseLayer:
    batch: "Batch"
    elements: "list[PygletElement]"

    def __init__(
        self,
        name: str,
        order: int,
        tags: list[str] = [],
    ) -> None:
        self.name = name
        self.order = order

        self.tags = tags

        self.batch = Batch()
        self.group = Group(order=order)
        self.elements = []

    def _add_element(
        self,
        element: "PygletElement"
    ) -> "BaseLayer":
        '''
        Add an element to the layer
        Args:
            element (Any): The element to add
        Returns:
            Layer: The layer instance
        '''
        element.batch = self.batch
        element.group = self.group
        self.elements.append(element)
        return self
    
    def append(self, element: "PygletElement") -> "BaseLayer":
        self._add_element(element=element)
        return self
    
    def remove(self, element: "PygletElement") -> "BaseLayer":
        self.elements.remove(element)
        return self
    
    def draw(self) -> None:
        self.batch.draw()