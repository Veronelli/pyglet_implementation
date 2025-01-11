
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.models.layer import ConfigLayer
    from app.commons.types import PygletElement
    from app.models.layer import Layer
    from pyglet.graphics import Batch



class BaseLayer:
    batch: "Batch"
    
    def __init__(
        self,
        name: str,
        order: int,
        config_layer: "ConfigLayer",
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
        tags: list[str] = [],
    ) -> None:
        pass

    def __add_element(
        self,
        element: "PygletElement"
    ) -> "Layer":
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
    
    def append(self, element: "PygletElement") -> "Layer":
        self.__add_element(element=element)
        return self
    
    def draw(self) -> None:
        self.batch.draw()