from __future__ import annotations
import copy
import re
import io
import decimal
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class BigDecimalWeightBaseOperations(OrderedMonoid):

    __serialVersionUID: int = -317234195461348466

    def inverse(self, element: decimal.Decimal) -> decimal.Decimal:
        return element.copy_negate()

    def identity(self) -> decimal.Decimal:
        return decimal.Decimal(0)

    def compare(self, o1: decimal.Decimal, o2: decimal.Decimal) -> int:
        return (o1 > o2) - (o1 < o2)

    def append(self, s1: decimal.Decimal, s2: decimal.Decimal) -> decimal.Decimal:

        if s1 is None or s2 is None:
            return None
        return s1 + s2
