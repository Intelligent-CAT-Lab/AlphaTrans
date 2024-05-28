from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.ToString import *
from src.main.org.joda.convert.FromString import *
import io
from abc import ABC

# Imports End


class Test3SuperClass(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def parse(amount: str) -> Test3SuperClass:
        pass

    def print(self) -> str:
        pass

    # Class Methods End
