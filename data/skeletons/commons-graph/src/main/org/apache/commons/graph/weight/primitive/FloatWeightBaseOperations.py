from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
import io

# Imports End


class FloatWeightBaseOperations(OrderedMonoid):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def inverse(self, element: float) -> float:
        pass

    def identity(self) -> float:
        pass

    def compare(self, s1: float, s2: float) -> int:
        pass

    def append(self, s1: float, s2: float) -> float:
        pass

    # Class Methods End
