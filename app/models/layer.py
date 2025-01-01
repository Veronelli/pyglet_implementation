from typing import Any
from pyglet.graphics import Group, Batch

from app.commons.types import PygletElement


class Layer:
    def __init__(
        self,
        name: str,
        tags:list[str],
        order: int
    )-> None:
        self.name = name
        self.tags = tags
        self.order = order
        self.group = Group(order=order)
        self.batch = Batch()
        self.elements: list[PygletElement] = []

    def add_element(
        self,
        element: PygletElement
    ) -> 'Layer':
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
    
    def remove_element(
        self,
        element: PygletElement
    ) -> 'Layer':
        '''
        Remove an element from the layer
        Args:
            element (PygletElement): The element to remove
        Returns:
            Layer: The layer instance
        '''
        self.elements.remove(element)
        return self
    
    def draw(self) -> None:
        '''
        Draw all elements in the layer
        '''
        self.batch.draw()
    
