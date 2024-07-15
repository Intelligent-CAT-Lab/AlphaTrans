from __future__ import annotations
import re
from abc import ABC
import io


class Category(ABC):

    def getMinimum(self) -> float:
        pass

    def getMaximum(self) -> float:
        pass
