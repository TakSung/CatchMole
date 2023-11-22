import __init__
from typing import Tuple, Optional

class Cursor:
    def __init__(self, size:int, init_y:int=0, init_x:int=0):
        self.size = size
        self.set(y=init_y, x=init_x)
    
    def filtering_point(self, value:int)->int:
        return max(min(value, self.size-1),0)
    
    def get(self)->Tuple[int, int]:
        return (self.y, self.x)

    def get_x(self)->int:
        return self.x

    def get_y(self)->int:
        return self.y
    
    def set(self, y:Optional[int]=None, x:Optional[int]=None)->Tuple[int,int]:
        if y is not None:
            self.y = self.filtering_point(y)
        if x is not None:
            self.x = self.filtering_point(x)
        return self.get()
    
    def change(self, cy:Optional[int]=None, cx:Optional[int]=None)-> Tuple[int,int]:
        (y, x) = self.get()
        if cy is not None:
            y = self.filtering_point(y+cy)
        if cx is not None:
            x = self.filtering_point(x+cx)
        
        return self.set(y, x)
        