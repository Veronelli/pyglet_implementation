class BaseModel:
    def __init__(self) -> None:
        self._position_x = 0
        self._position_y = 0

        self._direction_x = 0
        self._direction_y = 0

        self._element = None

    def set_direction(self, x: int, y: int) -> None:
        self._direction_x = x
        self._direction_y = y

    def set_position(self, x: int, y: int) -> None:
        self._position_x = x
        self._position_y = y

    def move(self, x: int, y: int) -> None:
        self._position_x += x
        self._position_y += y

    @property
    def position_x(self) -> int:
        return self._position_x 

    @property
    def position_y(self) -> int:
        return self._position_y
    
    @property
    def direction(self) -> tuple[int, int]:
        return (self._direction_x, self._direction_y,)

    @property
    def position(self) -> tuple[int, int]:
        return (self._position_x, self._position_y,)
    
    @property
    def tag(self) -> str:
        return self._tag
    
    @property
    def element(self):
        return self._element

    @element.setter
    def element(self, value):
        self._element = value