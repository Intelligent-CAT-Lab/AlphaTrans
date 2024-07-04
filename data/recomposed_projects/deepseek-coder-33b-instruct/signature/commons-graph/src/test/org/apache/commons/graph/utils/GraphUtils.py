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

        pass  # LLM could not translate this method

    @staticmethod
    def buildCrownGraph(
        nVertices: int, g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:

        tmp = []

        for i in range(nVertices):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)
            tmp.append(v)

        for i in range(nVertices):
            next = i + 1
            if i == (nVertices - 1):
                next = 0
            e = BaseLabeledEdge(f"{i} -> {next}")
            try:
                g.addEdge(tmp[i], e, tmp[next])
            except GraphException:
                pass

    @staticmethod
    def buildCompleteGraph(
        nVertices: int, g: BaseMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:

        for i in range(nVertices):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        for v1 in g.getVertices0():
            for v2 in g.getVertices0():
                if v1 != v2:
                    try:
                        g.addEdge(v1, BaseLabeledEdge(f"{v1} -> {v2}"), v2)
                    except GraphException:
                        pass

    @staticmethod
    def buildBipartedGraph(
        nVertices: int, g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]
    ) -> None:

        pass  # LLM could not translate this method

    def __init__(self) -> None:
        pass
