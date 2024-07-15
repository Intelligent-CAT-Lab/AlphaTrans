from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.GraphException import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *


class GraphUtils:

    @staticmethod
    def buildSudokuGraph(
        sudoku: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> typing.List[typing.List[BaseLabeledVertex]]:
        grid: typing.List[typing.List[BaseLabeledVertex]] = [
            [BaseLabeledVertex(format("%s, %s", row, col)) for col in range(9)]
            for row in range(9)
        ]
        for row in range(9):
            for col in range(9):
                sudoku.addVertex(grid[row][col])
        rowsOffsets: typing.List[int] = [0, 3, 6]
        colsOffsets: typing.List[int] = [0, 3, 6]
        for rof in range(3):
            for cof in range(3):
                boxes: typing.List[BaseLabeledVertex] = []
                for row in range(rowsOffsets[rof], 3 + rowsOffsets[rof]):
                    for col in range(colsOffsets[cof], 3 + colsOffsets[cof]):
                        boxes.append(grid[row][col])
                for v1 in boxes:
                    for v2 in boxes:
                        e: BaseLabeledEdge = BaseLabeledEdge(format("%s -> %s", v1, v2))
                        if not v1.equals(v2):
                            try:
                                sudoku.addEdge(v1, e, v2)
                            except GraphException:
                                pass
        for j in range(9):
            for i in range(9):
                for h in range(9):
                    v1: BaseLabeledVertex = grid[j][i]
                    v2: BaseLabeledVertex = grid[j][h]
                    if not v1.equals(v2):
                        e: BaseLabeledEdge = BaseLabeledEdge(format("%s -> %s", v1, v2))
                        try:
                            sudoku.addEdge(v1, e, v2)
                        except GraphException:
                            pass
        for j in range(9):
            for i in range(9):
                for h in range(9):
                    v1: BaseLabeledVertex = grid[i][j]
                    v2: BaseLabeledVertex = grid[h][j]
                    if not v1.equals(v2):
                        e: BaseLabeledEdge = BaseLabeledEdge(format("%s -> %s", v1, v2))
                        try:
                            sudoku.addEdge(v1, e, v2)
                        except GraphException:
                            pass
        return grid

    @staticmethod
    def buildCrownGraph(
        nVertices: int, g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:
        tmp: List[BaseLabeledVertex] = []

        for i in range(nVertices):
            v: BaseLabeledVertex = BaseLabeledVertex(str(i))
            g.addVertex(v)
            tmp.append(v)

        for i in range(nVertices):
            next: int = i + 1
            if i == (nVertices - 1):
                next = 0
            e: BaseLabeledEdge = BaseLabeledEdge(format("%s -> %s", i, next))
            try:
                g.addEdge(tmp[i], e, tmp[next])
            except GraphException as ge:
                pass

    @staticmethod
    def buildCompleteGraph(
        nVertices: int, g: BaseMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def buildBipartedGraph(
        nVertices: int, g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:

        pass  # LLM could not translate this method

    def __init__(self) -> None:
        pass
