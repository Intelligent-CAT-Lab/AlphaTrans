from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.FromStringFactory import *
import io
from abc import ABC

# Imports End


class Test3Interface(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    # Class Methods End
