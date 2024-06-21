from __future__ import annotations
from abc import ABC
import io
from src.main.org.joda.convert.FromStringFactory import *
from src.main.org.joda.convert.ToString import *


class Test3Interface(ABC):

    def toString(self) -> str:

        return super().toString()
