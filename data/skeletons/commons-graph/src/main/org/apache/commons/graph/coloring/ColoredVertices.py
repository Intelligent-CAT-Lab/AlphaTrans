from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
import typing
from typing import *
import io

# Imports End


class ColoredVertices:

    # Class Fields Begin
    __coloredVertices: typing.Dict[typing.Any, typing.Any] = None
    __usedColor: typing.List[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def getRequiredColors(self) -> int:
        pass

    def getColor(self, v: typing.Any) -> typing.Any:
        pass

    def containsColoredVertex(self, vertex: typing.Any) -> bool:
        pass

    def removeColor(self, v: typing.Any) -> None:
        pass

    def addColor(self, v: typing.Any, color: typing.Any) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
