from __future__ import annotations

# Imports Begin
import io
from abc import ABC

# Imports End


class Category(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getMinimum(self) -> float:
        pass

    def getMaximum(self) -> float:
        pass

    # Class Methods End
