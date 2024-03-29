from typing import Tuple, Optional, Callable
from icecream import ic


def _min_max_filtering(value: int, max_value: int) -> int:
    return max(min(value, max_value), 0)


class Cursor:
    def __init__(
        self,
        size: Tuple[int, int],
        init_y: int = 0,
        init_x: int = 0,
        filter: Callable[[int, int], int] = _min_max_filtering,
    ):
        self.size = size
        self.filter = filter
        self.set(y=init_y, x=init_x)

    def filtering_point_y(self, value: int) -> int:
        return self.filter(value, self.size[0] - 1)

    def filtering_point_x(self, value: int) -> int:
        return self.filter(value, self.size[1] - 1)

    def get(self) -> Tuple[int, int]:
        """_summary_

        Returns:
            Tuple[int, int]: (y,x)
        """
        return (self.y, self.x)

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def set(self, y: Optional[int] = None, x: Optional[int] = None) -> Tuple[int, int]:
        if isinstance(y, int):
            self.y = self.filtering_point_y(y)
        if isinstance(x, int):
            self.x = self.filtering_point_x(x)
        return self.get()

    def change(
        self, cy: Optional[int] = None, cx: Optional[int] = None
    ) -> Tuple[int, int]:
        (y, x) = self.get()
        if cy is not None:
            y = self.filtering_point_y(y + cy)
        if cx is not None:
            x = self.filtering_point_x(x + cx)

        return self.set(y, x)
