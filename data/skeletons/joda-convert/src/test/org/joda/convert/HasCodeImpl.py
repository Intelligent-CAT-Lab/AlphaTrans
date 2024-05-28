from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.ToString import *
from src.test.org.joda.convert.HasCodeInterface import *
from src.main.org.joda.convert.FromString import *
import io

# Imports End


class HasCodeImpl(HasCodeInterface):

    # Class Fields Begin
    code: str = None
    # Class Fields End

    # Class Methods Begin
    def getCode(self) -> str:
        pass

    def __init__(self, code: str) -> None:
        pass

    # Class Methods End
