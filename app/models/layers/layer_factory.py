from pyglet.graphics import Group
from app.models.layers.encapsule_layer import EncapsuleLayer
from app.commons.scsissor_group import ScissorGroup

def factory_encapsule_layer(
    x: int,
    y: int,
    width: int,
    height: int,
    name: str,
    tags: list[str],
    order: int,
    group_type: Group = Group
) -> EncapsuleLayer:
    """
    Factory function to create an EncapsuleLayer instance.
    Args:
        x (int): The x-coordinate of the layer.
        y (int): The y-coordinate of the layer.
        width (int): The width of the layer.
        height (int): The height of the layer.
        name (str): The name of the layer.
        tags (list[str]): A list of tags associated with the layer.
        order (int): The rendering order of the layer.
        group_type (Group): The type of group to use for the layer.
    Returns:
        EncapsuleLayer: An instance of EncapsuleLayer with the specified properties.
    """
    if group_type is ScissorGroup:
        group_instance = ScissorGroup(
            x=x,
            y=y,
            width=width,
            height=height,
            order=order
        )
    else:
        group_instance = Group(order=order)
    
    return EncapsuleLayer(
        x=x,
        y=y,
        width=width,
        height=height,
        name=name,
        tags=tags,
        order=order,
        group_instance=group_instance
    )