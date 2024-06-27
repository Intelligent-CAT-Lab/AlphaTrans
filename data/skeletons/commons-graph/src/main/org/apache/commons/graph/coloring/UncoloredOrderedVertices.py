from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class UncoloredOrderedVertices:

    # Class Fields Begin
    __orderedVertices: typing.Dict[int, typing.Set[typing.Any]] = None
    # Class Fields End

    # Class Methods Begin
    def size(self) -> int:
        pass

    def iterator(self) -> typing.Iterator[typing.Any]:
        pass

    def compare(self, o1: int, o2: int) -> int:
        pass

    def addVertexDegree(self, v: typing.Any, degree: int) -> None:
        pass

    # Class Methods End
