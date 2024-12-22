from app.commons.models.base_model import BaseModel

__all__ = ['BaseModelBuilder']

class BaseModelBuilder:
    def __init__(self):
        self._base_model = BaseModel()

    def set_position(self, x: int, y: int) -> 'BaseModelBuilder':
        self._base_model.move(x, y)
        return self

    def set_direction(self, x: int, y: int) -> 'BaseModelBuilder':
        self._base_model.set_direction(x, y)
        return self
    
    def set_position(self, x: int, y: int) -> 'BaseModelBuilder':
        self._base_model.set_position(x, y)
        return self

    def set_element(self, element) -> 'BaseModelBuilder':
        self._base_model.element = element
        return self

    def build(self) -> BaseModel:
        return self._base_model