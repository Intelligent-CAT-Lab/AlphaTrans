from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from abc import ABC

# Imports End


class SwallowedExceptionListener(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def onSwallowException(self, e: Exception) -> None:
        pass

    # Class Methods End
