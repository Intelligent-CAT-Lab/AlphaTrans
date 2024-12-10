from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from io import StringIO
from abc import ABC

# Imports End


class CallStack(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> bool:
        pass

    def fillInStackTrace(self) -> None:
        pass

    def clear(self) -> None:
        pass

    # Class Methods End
