from __future__ import annotations
import re
import io
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class BigIntegerWeightBaseOperations(OrderedMonoid):

    __serialVersionUID: int = 4118152508299694652

    def inverse(self, element: int) -> int:
        return -element

    def identity(self) -> int:
        return 0

    def compare(self, o1: int, o2: int) -> int:
        return o1.compareTo(o2)

    def append(self, s1: int, s2: int) -> int:
        if s1 is None or s2 is None:
            return None
        return s1 + s2
