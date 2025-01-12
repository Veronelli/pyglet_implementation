from app.commons.shapes import RectangleBorder
from app.models.layers.base import BaseLayer
from app.utils.colors.base import ColorRGB as Color

class StaticLayer(BaseLayer):
    def __init__(
        self,
        name: str,
        order: int,
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
        tags: list[str] = [],
    ) -> None:
        super().__init__(
            name=name,
            order=order,
            tags=tags,
        )
        
        self.layer_element = RectangleBorder(
            x=x,
            y=y,
            width=width,
            height=height,
            color=Color.BLUE,
            border=2.0,
            batch=self.batch,
            group=self.group
        )


    
