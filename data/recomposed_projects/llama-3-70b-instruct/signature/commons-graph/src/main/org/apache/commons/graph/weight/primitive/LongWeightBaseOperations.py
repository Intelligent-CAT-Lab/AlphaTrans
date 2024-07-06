from __future__ import annotations
import re
import io
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class LongWeightBaseOperations(OrderedMonoid):

    __serialVersionUID: int = 3149327896191098756

    def inverse(self, element: int) -> int:
        return -element

    def identity(self) -> int:
        return 0

    def compare(self, s1: int, s2: int) -> int:
        return s1 - s2

    def append(self, s1: int, s2: int) -> int:
        if s1 is None or s2 is None:
            return None
        return s1 + s2
