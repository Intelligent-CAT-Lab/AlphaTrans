from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from abc import ABC

# Imports End


class UsageTracking(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def use(self, pooledObject: typing.Any) -> None:
        pass

    # Class Methods End
