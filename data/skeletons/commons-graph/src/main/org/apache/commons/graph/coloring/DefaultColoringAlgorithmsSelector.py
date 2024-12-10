from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.coloring.UncoloredOrderedVertices import *
from src.main.org.apache.commons.graph.coloring.NotEnoughColorsException import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultColoringAlgorithmsSelector:

    # Class Fields Begin
    __g: UndirectedGraph[typing.Any, typing.Any] = None
    __colors: typing.Set[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def applyingGreedyAlgorithm(self) -> ColoredVertices[typing.Any, typing.Any]:
        pass

    def applyingBackTrackingAlgorithm1(
        self, partialColoredVertex: ColoredVertices[typing.Any, typing.Any]
    ) -> ColoredVertices[typing.Any, typing.Any]:
        pass

    def applyingBackTrackingAlgorithm0(self) -> ColoredVertices[typing.Any, typing.Any]:
        pass

    def __init__(
        self, g: UndirectedGraph[typing.Any, typing.Any], colors: typing.Set[typing.Any]
    ) -> None:
        pass

    def __isThereColorConflict(
        self,
        currentVertex: typing.Any,
        coloredVertices: ColoredVertices[typing.Any, typing.Any],
    ) -> bool:
        pass

    def __backtraking(
        self,
        currentVertexIndex: int,
        verticesList: typing.List[typing.Any],
        coloredVertices: ColoredVertices[typing.Any, typing.Any],
    ) -> bool:
        pass

    # Class Methods End
