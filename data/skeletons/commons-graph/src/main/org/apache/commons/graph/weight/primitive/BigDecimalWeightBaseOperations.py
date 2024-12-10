from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
import decimal
import io

# Imports End


class BigDecimalWeightBaseOperations(OrderedMonoid):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def inverse(self, element: decimal.Decimal) -> decimal.Decimal:
        pass

    def identity(self) -> decimal.Decimal:
        pass

    def compare(self, o1: decimal.Decimal, o2: decimal.Decimal) -> int:
        pass

    def append(self, s1: decimal.Decimal, s2: decimal.Decimal) -> decimal.Decimal:
        pass

    # Class Methods End
