from __future__ import annotations
import re
import logging
import typing
from typing import *
from io import StringIO
import unittest
import pytest
import io
import numbers
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.coloring.AbstractColoringTest import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.coloring.ColorsBuilder import *
from src.main.org.apache.commons.graph.coloring.NotEnoughColorsException import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.utils.GraphUtils import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *


class GraphColoringBackTrackingTestCase(AbstractColoringTest, unittest.TestCase):

    def testSudokuWithConstraints(self) -> None:

        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = self.buildSudokuGraph(g1)

        predefinedColor = ColoredVertices[BaseLabeledVertex, int]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)

        sudoku = (
            coloring(g1)
            .withColors(self._createColorsList(9))
            .applyingBackTrackingAlgorithm1(predefinedColor)
        )
        assert sudoku is not None
        self._checkColoring(g1, sudoku)
        assert sudoku.getRequiredColors() == 9

        assert sudoku.getColor(grid[0][0]) == 1
        assert sudoku.getColor(grid[5][5]) == 8
        assert sudoku.getColor(grid[1][2]) == 5

        sb = io.StringIO()
        nf = "{:02d}".format
        sb.write("\n")
        for i in range(9):
            for j in range(9):
                sb.write("| ")
                sb.write(nf(sudoku.getColor(grid[i][j])))
                sb.write(" | ")
            sb.write("\n")
        logging.getLogger().info(sb.getvalue())

    def testSudoku(self) -> None:

        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        grid = GraphUtils.buildSudokuGraph(g1)

        sudoku = (
            CommonsGraph.coloring(g1)
            .withColors(self._createColorsList(9))
            .applyingBackTrackingAlgorithm0()
        )
        assert sudoku is not None
        self._checkColoring(g1, sudoku)
        assert sudoku.getRequiredColors() == 9

        sb = io.StringIO()
        nf = numbers.NumberFormat("00")
        sb.write("\n")
        for i in range(9):
            for j in range(9):
                sb.write("| " + nf.format(sudoku.getColor(grid[i][j])) + " | ")
            sb.write("\n")
        logging.getLogger().fine(sb.getvalue())

    def testNullGraph(self) -> None:

        with pytest.raises(NullPointerException):
            coloring(None).withColors(None).applyingBackTrackingAlgorithm0()

    def testNullColorGraph(self) -> None:

        g = UndirectedMutableGraph()

        with pytest.raises(NullPointerException):
            coloring(g).withColors(None).applyingBackTrackingAlgorithm0()

    def testNotEnoughtColorGraph(self) -> None:

        pass  # LLM could not translate this method

    def testEmptyGraph(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()

        coloredVertices = (
            CommonsGraph.coloring(g)
            .withColors(self._createColorsList(1))
            .applyingBackTrackingAlgorithm0()
        )
        assert coloredVertices is not None
        assert coloredVertices.getRequiredColors() == 0

    def testCromaticNumberSparseGraph(self) -> None:

        g1 = UndirectedMutableGraph()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))

        coloredVertices = (
            coloring(g1)
            .withColors(self._createColorsList(1))
            .applyingBackTrackingAlgorithm0()
        )
        assert coloredVertices is not None
        assert coloredVertices.getRequiredColors() == 1
        self._checkColoring(g1, coloredVertices)

    def testCromaticNumberComplete(self) -> None:

        g1 = UndirectedMutableGraph()

        GraphUtils.buildCompleteGraph(100, g1)

        coloredVertices = (
            CommonsGraph.coloring(g1)
            .withColors(self._createColorsList(100))
            .applyingBackTrackingAlgorithm0()
        )
        assert coloredVertices is not None
        assert coloredVertices.getRequiredColors() == 100
        GraphUtils._checkColoring(g1, coloredVertices)

    def testCromaticNumberBiparted(self) -> None:

        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()

        GraphUtils.buildBipartedGraph(100, g1)

        coloredVertices = (
            CommonsGraph.coloring(g1)
            .withColors(self._createColorsList(2))
            .applyingBackTrackingAlgorithm0()
        )
        assert coloredVertices is not None
        assert coloredVertices.getRequiredColors() == 2
        GraphUtils._checkColoring(g1, coloredVertices)

    def testCromaticNumber(self) -> None:

        two = BaseLabeledVertex("2")

        g = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: None,
                lambda: [
                    (
                        BaseLabeledVertex("1"),
                        lambda e: e.from_vertex(BaseLabeledVertex("1")).to(two),
                    ),
                    (two, lambda e: e.from_vertex(two).to(BaseLabeledVertex("3"))),
                    (
                        BaseLabeledVertex("3"),
                        lambda e: e.from_vertex(BaseLabeledVertex("3")).to(
                            BaseLabeledVertex("1")
                        ),
                    ),
                ],
                lambda: [
                    (
                        BaseLabeledEdge("1 -> 2"),
                        lambda e: e.from_vertex(BaseLabeledVertex("1")).to(two),
                    ),
                    (
                        BaseLabeledEdge("2 -> 3"),
                        lambda e: e.from_vertex(two).to(BaseLabeledVertex("3")),
                    ),
                    (
                        BaseLabeledEdge("3 -> 1"),
                        lambda e: e.from_vertex(BaseLabeledVertex("3")).to(
                            BaseLabeledVertex("1")
                        ),
                    ),
                ],
            )
        )

        coloredVertex = ColoredVertices()
        coloredVertex.addColor(two, 2)

        coloredVertices = (
            CommonsGraph.coloring(g)
            .withColors(self._createColorsList(3))
            .applyingBackTrackingAlgorithm1(coloredVertex)
        )
        assert coloredVertices is not None
        assert coloredVertices.getRequiredColors() == 3
        assert coloredVertices.getColor(two) == 2
        self._checkColoring(g, coloredVertices)

    def testCrawnGraph(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()

        GraphUtils.buildCrownGraph(6, g)

        coloredVertices = (
            CommonsGraph.coloring(g)
            .withColors(self._createColorsList(2))
            .applyingBackTrackingAlgorithm0()
        )
        assert coloredVertices is not None
        assert coloredVertices.getRequiredColors() == 2
        GraphUtils._checkColoring(g, coloredVertices)
