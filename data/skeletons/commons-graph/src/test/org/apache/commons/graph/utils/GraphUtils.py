from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.GraphException import *
import typing
from typing import *
import io

# Imports End


class GraphUtils:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def buildSudokuGraph(
        sudoku: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> typing.List[typing.List[BaseLabeledVertex]]:
        pass

    @staticmethod
    def buildCrownGraph(
        nVertices: int, g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:
        pass

    @staticmethod
    def buildCompleteGraph(
        nVertices: int, g: BaseMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:
        pass

    @staticmethod
    def buildBipartedGraph(
        nVertices: int, g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
