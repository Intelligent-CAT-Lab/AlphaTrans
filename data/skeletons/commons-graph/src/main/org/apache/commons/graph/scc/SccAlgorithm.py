from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from abc import ABC

# Imports End


class SccAlgorithm(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def perform(self) -> typing.Set[typing.Set[typing.Any]]:
        pass

    # Class Methods End
