from __future__ import annotations
import io
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class FloatWeightBaseOperations(OrderedMonoid):

    __serialVersionUID: int = 8542498901286671169

    def inverse(self, element: float) -> float:

        return -element

    def identity(self) -> float:

        return 0.0

    def compare(self, s1: float, s2: float) -> int:

        if s1 < s2:
            return -1
        elif s1 > s2:
            return 1
        else:
            return 0

    def append(self, s1: float, s2: float) -> float:

        if s1 is None or s2 is None:
            return None
        return s1 + s2
