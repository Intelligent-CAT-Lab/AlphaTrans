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
        self.buildSudokuGraph(g1)

        col = self._createColorsList(9)

        sudoku = (
            CommonsGraph.coloring(g1).withColors(col).applyingBackTrackingAlgorithm0()
        )
        GraphUtils._checkColoring(g1, sudoku)

    def testNullGraph(self) -> None:

        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(None).withColors(None).applyingGreedyAlgorithm()

    def testNullColorGraph(self) -> None:

        g = UndirectedMutableGraph()

        with pytest.raises(RuntimeError):
            CommonsGraph.coloring(g).withColors(None).applyingBackTrackingAlgorithm0()

    def testNotEnoughtColorGreedyGraph(self) -> None:

        pass  # LLM could not translate this method

    def testEmptyGraph(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()

        coloredVertices = (
            CommonsGraph.coloring(g)
            .withColors(self._createColorsList(1))
            .applyingGreedyAlgorithm()
        )
        assert coloredVertices is not None
        assert coloredVertices.getRequiredColors() == 0

    def testCromaticNumberSparseGraph(self) -> None:

        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
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
        GraphUtils.checkColoring(g1, coloredVertices)

    def testCromaticNumberBiparted(self) -> None:

        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        buildBipartedGraph(100, g1)

        coloredVertices = (
            CommonsGraph.coloring(g1)
            .withColors(self.__colors)
            .applyingGreedyAlgorithm()
        )

        self._checkColoring(g1, coloredVertices)

    def testCromaticNumber(self) -> None:

        g = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection().connect0(
                lambda: [
                    BaseLabeledVertex("1"),
                    BaseLabeledVertex("2"),
                    BaseLabeledVertex("3"),
                ],
                lambda: [
                    (BaseLabeledEdge("1 -> 2"), "1", "2"),
                    (BaseLabeledEdge("2 -> 3"), "2", "3"),
                    (BaseLabeledEdge("3 -> 1"), "3", "1"),
                ],
            )
        )

        coloredVertices = (
            ColoringAlgorithmsSelector(g)
            .withColors(self.__colors)
            .applyingGreedyAlgorithm()
        )
        self._checkColoring(g, coloredVertices)

    def testCrawnGraph(self) -> None:

        g = UndirectedMutableGraph()
        buildCrownGraph(6, g)

        coloredVertices = (
            CommonsGraph.coloring(g).withColors(self.__colors).applyingGreedyAlgorithm()
        )
        self._checkColoring(g, coloredVertices)
