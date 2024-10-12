from typing import Optional
import math

class Node:
    def __init__(self, state: float, parent: Optional['Node']):
        self.state = state
        self.parent = parent

    def __repr__(self) -> str:
            return str(self.state)
    def __str__(self) -> str:
        if self.parent:
            return f"{self.parent} => {self.state}"
        else:
            return str(self.state)