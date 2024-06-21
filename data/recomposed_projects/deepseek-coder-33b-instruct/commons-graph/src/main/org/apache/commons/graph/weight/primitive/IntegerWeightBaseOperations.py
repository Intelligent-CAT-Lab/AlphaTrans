from __future__ import annotations
import io
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class IntegerWeightBaseOperations(OrderedMonoid):

    __serialVersionUID: int = -8641477350652350485

    def inverse(self, element: int) -> int:

        return -element

    def identity(self) -> int:

        return 0

    def compare(self, o1: int, o2: int) -> int:

        if o1 < o2:
            return -1
        elif o1 == o2:
            return 0
        else:
            return 1

    def append(self, s1: int, s2: int) -> int:

        if s1 is None or s2 is None:
            return None
        return s1 + s2
