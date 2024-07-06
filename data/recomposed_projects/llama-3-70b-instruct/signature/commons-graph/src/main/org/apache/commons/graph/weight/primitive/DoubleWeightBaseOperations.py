from __future__ import annotations
import re
import io
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class DoubleWeightBaseOperations(OrderedMonoid):

    __serialVersionUID: int = 4440399710792243877

    def inverse(self, element: float) -> float:
        return -element

    def identity(self) -> float:
        return 0.0

    def compare(self, s1: float, s2: float) -> int:
        return s1.__cmp__(s2)

    def append(self, s1: float, s2: float) -> float:
        if s1 is None or s2 is None:
            return None
        return s1 + s2
