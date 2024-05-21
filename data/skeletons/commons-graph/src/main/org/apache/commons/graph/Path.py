from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io
import pathlib
from abc import ABC

# Imports End


class Path(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getTarget(self) -> typing.Any:
        pass

    def getSource(self) -> typing.Any:
        pass

    # Class Methods End
