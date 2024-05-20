from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from abc import ABC

# Imports End


class ProgressListener(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def update(self, pBytesRead: int, pContentLength: int, pItems: int) -> None:
        pass

    # Class Methods End
