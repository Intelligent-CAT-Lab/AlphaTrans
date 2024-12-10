from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
import io

# Imports End


class LongWeightBaseOperations(OrderedMonoid):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def inverse(self, element: int) -> int:
        pass

    def identity(self) -> int:
        pass

    def compare(self, s1: int, s2: int) -> int:
        pass

    def append(self, s1: int, s2: int) -> int:
        pass

    # Class Methods End
