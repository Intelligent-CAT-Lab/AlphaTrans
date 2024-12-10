from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.utils.Assertions import *
import typing
from typing import *
import io

# Imports End


class BaseLabeledEdge:

    # Class Fields Begin
    __serialVersionUID: int = None
    __label: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    def getLabel(self) -> str:
        pass

    def __init__(self, label: str) -> None:
        pass

    # Class Methods End
