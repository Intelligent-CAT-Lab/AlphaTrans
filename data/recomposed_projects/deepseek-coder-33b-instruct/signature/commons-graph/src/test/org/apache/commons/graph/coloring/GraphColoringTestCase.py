from __future__ import annotations
import re
import typing
from typing import *
import unittest
import pytest
import io
import numbers
import unittest
import typing
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.coloring.AbstractColoringTest import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.coloring.ColorsBuilder import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.utils.GraphUtils import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *


class GraphColoringTestCase(AbstractColoringTest, unittest.TestCase):

    __colors: typing.Set[int] = set(range(11))

    def testSudoku(self) -> None:

        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        buildSudokuGraph(g1)

        col = self._createColorsList(9)

        sudoku = (
            CommonsGraph.coloring(g1).withColors(col).applyingBackTrackingAlgorithm0()
        )
        self._checkColoring(g1, sudoku)

    def testNullGraph(self) -> None:

        with pytest.raises(TypeError):
            coloring(None).withColors(None).applyingGreedyAlgorithm()

    def testNullColorGraph(self) -> None:

        g = UndirectedMutableGraph()

        with pytest.raises(NullPointerException):
            coloring(g).withColors(None).applyingBackTrackingAlgorithm0()

    def testNotEnoughtColorGreedyGraph(self) -> None:

        pass  # LLM could not translate this method

    def testEmptyGraph(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()

        coloredVertices = (
            coloring(g).withColors(self._createColorsList(1)).applyingGreedyAlgorithm()
        )
        assert coloredVertices is not None
        self.assertEqual(0, coloredVertices.getRequiredColors())

    def testCromaticNumberSparseGraph(self) -> None:

        g1 = UndirectedMutableGraph()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))

        coloredVertices = (
            CommonsGraph.coloring(g1)
            .withColors(self.__colors)
            .applyingGreedyAlgorithm()
        )

        self.assertEqual(1, coloredVertices.getRequiredColors())
        self._checkColoring(g1, coloredVertices)

    def testCromaticNumberComplete(self) -> None:

        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(100, g1)

        coloredVertices = (
            CommonsGraph.coloring(g1)
            .withColors(self._createColorsList(100))
            .applyingGreedyAlgorithm()
        )
        self._checkColoring(g1, coloredVertices)

    def testCromaticNumberBiparted(self) -> None:

        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildBipartedGraph(100, g1)

        coloredVertices = (
            CommonsGraph.coloring(g1)
            .withColors(self.__colors)
            .applyingGreedyAlgorithm()
        )

        self._checkColoring(g1, coloredVertices)

    def testCromaticNumber(self) -> None:

        pass  # LLM could not translate this method

    def testCrawnGraph(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCrownGraph(6, g)

        coloredVertices = (
            CommonsGraph.coloring(g).withColors(self.__colors).applyingGreedyAlgorithm()
        )
        self._checkColoring(g, coloredVertices)
