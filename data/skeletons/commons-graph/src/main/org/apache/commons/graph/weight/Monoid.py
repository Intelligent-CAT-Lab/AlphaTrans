from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from abc import ABC

# Imports End


class Monoid(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def inverse(self, element: typing.Any) -> typing.Any:
        pass

    def identity(self) -> typing.Any:
        pass

    def append(self, e1: typing.Any, e2: typing.Any) -> typing.Any:
        pass

    # Class Methods End
