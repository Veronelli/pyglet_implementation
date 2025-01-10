from typing import Any
from pyglet.graphics import Group, Batch

from app.commons.math import sum_difference
from app.commons.shapes import RectangleBorder
from app.commons.types import PygletElement
from enum import StrEnum, auto


class ContainerTypeEnum(StrEnum):
    IN = auto()
    OUT = auto()
    IN_OUT = auto()


class ConfigLayer:
    def __init__(self, container: ContainerTypeEnum) -> None:
        self.container = container


class Layer:
    
    def __init__(
        self,
        name: str,
        tags:list[str],
        order: int,
        width: int = 0, 
        height: int = 0,
        x: int = 0,
        y: int = 0
    )-> None:
        self.name = name
        self.tags = tags
        self.order = order

        self.group = Group(order=100)
        self.batch = Batch()
        self.elements: list[PygletElement] = []


        self._width = width
        self._height = height

        self._x = x
        self._y = y

        self.layer_element = RectangleBorder(
            x=self._x,
            y=self._y,
            width=self._width,
            height=self._height,
            color=(0, 122, 255),
            border=2.0,
            batch=self.batch,
            group=self.group
        )

    @property
    def x(self) -> int | None:
        if self._x is None and len(self.elements) > 0:
            self._x = self.elements[0].x
        self.layer_element.update_vertices()
        return self._x
    
    @property
    def y(self) -> int | None:
        if self._y is None and len(self.elements) > 0:
            self._y = self.elements[0].y
        self.layer_element.update_vertices()
        return self._y

    @property
    def width(self) -> int:
        for element in self.elements:
            if element.x + element.width > self._width:
                self._width = (self.x - element.x) + element.width
        return self._width
    
    @property
    def height(self) -> int:
        for element in self.elements:
            if element.y + element.height > self._height:
                self._height = (self.y - element.y) + element.height
        return self._height

    def __move_in(self, element: PygletElement) -> 'Layer':
        '''
        Move an element to the layer
        Args:
            element (PygletElement): The element to move
        Returns:
            Layer: The layer instance
        '''
        element.x = sum_difference(a=self.x, b=self.x)
        element.y = sum_difference(a=self.y, b=self.y)
        return self

    def __add_element(
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
    
    def append(self, element: PygletElement) -> 'Layer':
        self.__add_element(element=element)
        self.__move_in(element=element)
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
    
