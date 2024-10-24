from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from io import StringIO
from abc import ABC

# Imports End


class BaseObject(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def _toStringAppendFields(
        self, builder: typing.Union[typing.List[str], io.StringIO]
    ) -> None:
        pass

    # Class Methods End
