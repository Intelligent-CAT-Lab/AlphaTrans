from __future__ import annotations
import re
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
        g1: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        grid: typing.List[typing.List[BaseLabeledVertex]] = GraphUtils.buildSudokuGraph(
            g1
        )

        predefinedColor: ColoredVertices[BaseLabeledVertex, int] = ColoredVertices[
            BaseLabeledVertex, int
        ]()
        predefinedColor.addColor(grid[0][0], 1)
        predefinedColor.addColor(grid[5][5], 8)
        predefinedColor.addColor(grid[1][2], 5)

        sudoku: ColoredVertices[BaseLabeledVertex, int] = (
            CommonsGraph.coloring(g1)
            .withColors(self._createColorsList(9))
            .applyingBackTrackingAlgorithm1(predefinedColor)
        )
        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)
        self.assertEqual(9, sudoku.getRequiredColors())

        self.assertEqual(1, sudoku.getColor(grid[0][0]))
        self.assertEqual(8, sudoku.getColor(grid[5][5]))
        self.assertEqual(5, sudoku.getColor(grid[1][2]))

        sb: io.StringIO = io.StringIO()
        nf: numbers.Number = numbers.Number()
        sb.append("\n")
        for i in range(9):
            for j in range(9):
                sb.append("| ")
                sb.append(nf.format(sudoku.getColor(grid[i][j])))
                sb.append(" | ")
            sb.append("\n")
        Logger.getAnonymousLogger().fine(sb.toString())

    def testSudoku(self) -> None:
        g1: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        grid: typing.List[typing.List[BaseLabeledVertex]] = GraphUtils.buildSudokuGraph(
            g1
        )

        sudoku: ColoredVertices[BaseLabeledVertex, int] = (
            CommonsGraph.coloring(g1)
            .withColors(self._createColorsList(9))
            .applyingBackTrackingAlgorithm0()
        )
        self.assertIsNotNone(sudoku)
        self._checkColoring(g1, sudoku)
        self.assertEqual(9, sudoku.getRequiredColors())

        sb: io.StringIO = io.StringIO()
        nf: numbers.Number = numbers.Number()
        sb.append("\n")
        for i in range(9):
            for j in range(9):
                sb.append("| " + nf.format(sudoku.getColor(grid[i][j])) + " | ")
            sb.append("\n")
        Logger.getAnonymousLogger().fine(sb.toString())

    def testNullGraph(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.coloring(None).withColors(
                None
            ).applyingBackTrackingAlgorithm0()

    def testNullColorGraph(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        CommonsGraph.coloring(g).withColors(None).applyingBackTrackingAlgorithm0()

    def testNotEnoughtColorGraph(self) -> None:

        pass  # LLM could not translate this method

    def testEmptyGraph(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        coloredVertices: ColoredVertices[BaseLabeledVertex, int] = (
            CommonsGraph.coloring(g)
            .withColors(self._createColorsList(1))
            .applyingBackTrackingAlgorithm0()
        )
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(0, coloredVertices.getRequiredColors())

    def testCromaticNumberSparseGraph(self) -> None:
        g1 = UndirectedMutableGraph(BaseLabeledVertex, BaseLabeledEdge)
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))
        coloredVertices = (
            CommonsGraph.coloring(g1)
            .withColors(self._createColorsList(1))
            .applyingBackTrackingAlgorithm0()
        )
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(1, coloredVertices.getRequiredColors())
        self._checkColoring(g1, coloredVertices)

    def testCromaticNumberComplete(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        buildCompleteGraph(100, g1)
        coloredVertices = (
            CommonsGraph.coloring(g1)
            .withColors(self._createColorsList(100))
            .applyingBackTrackingAlgorithm0()
        )
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(100, coloredVertices.getRequiredColors())
        self._checkColoring(g1, coloredVertices)

    def testCromaticNumberBiparted(self) -> None:
        g1 = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        buildBipartedGraph(100, g1)
        coloredVertices = (
            CommonsGraph.coloring(g1)
            .withColors(self._createColorsList(2))
            .applyingBackTrackingAlgorithm0()
        )
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(2, coloredVertices.getRequiredColors())
        self._checkColoring(g1, coloredVertices)

    def testCromaticNumber(self) -> None:

        pass  # LLM could not translate this method

    def testCrawnGraph(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            UndirectedMutableGraph()
        )
        buildCrownGraph(6, g)
        coloredVertices: ColoredVertices[BaseLabeledVertex, int] = (
            coloring(g)
            .withColors(self._createColorsList(2))
            .applyingBackTrackingAlgorithm0()
        )
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(2, coloredVertices.getRequiredColors())
        self._checkColoring(g, coloredVertices)
