from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.VertexPair import *
import typing
from typing import *
import numbers
import io
from abc import ABC

# Imports End


class AbstractColoringTest(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _createColorsList(self, colorNumber: int) -> typing.Set[int]:
        pass

    def _createColorMap(self, numColor: int) -> typing.Dict[int, str]:
        pass

    def _checkColoring(
        self,
        g: UndirectedMutableGraph[typing.Any, typing.Any],
        coloredVertices: ColoredVertices[typing.Any, typing.Any],
    ) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
