from __future__ import annotations
import re
from abc import ABC
import io


class Category(ABC):

    def getMinimum(self) -> float:
        return 0.0

    def getMaximum(self) -> float:
        return self.maximum
