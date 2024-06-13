# Imports Begin
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.test.org.apache.commons.graph.utils.GraphUtils import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.coloring.NotEnoughColorsException import *
from src.main.org.apache.commons.graph.coloring.ColorsBuilder import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.test.org.apache.commons.graph.coloring.AbstractColoringTest import AbstractColoringTest
import logging
from typing import *
from io import StringIO
from textwrap import dedent
# Imports End

class GraphColoringBackTrackingTestCase(AbstractColoringTest):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testCrawnGraph(self) -> None:
        g = UndirectedMutableGrap()

        GraphUtils.buildCrownGraph(6, g)

        coloredVertices = CommonsGraph.coloring(g)\
            .withColors(self._createColorsList(2)).applyingBackTrackingAlgorithm0()
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(2, coloredVertices.getRequiredColors())
        self._checkColoring(g, coloredVertices)

    
    def testCromaticNumber(self) -> None:
        two = BaseLabeledVertex("2")

        g = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionGraphColoringBackTrackingTestCase(two)
        )

        coloredVertex = ColoredVertices()
        coloredVertex.addColor(two, 2)

        coloredVertices = CommonsGraph.coloring(g)\
            .withColors(self._createColorsList(3)).applyingBackTrackingAlgorithm1(coloredVertex)
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(3, coloredVertices.getRequiredColors())
        self.assertEqual(2, coloredVertices.getColor(two))
        self._checkColoring(g, coloredVertices)

    
    def testCromaticNumberBiparted(self) -> None:
        g1 = UndirectedMutableGraph()

        GraphUtils.buildBipartedGraph(100, g1)

        coloredVertices = CommonsGraph.coloring(g1)\
            .withColors(self._createColorsList(2)).applyingBackTrackingAlgorithm0()
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(2, coloredVertices.getRequiredColors())
        self._checkColoring(g1, coloredVertices)

    
    def testCromaticNumberComplete(self) -> None:
        g1 = UndirectedMutableGraph()

        GraphUtils.buildCompleteGraph(100, g1)

        coloredVertices = CommonsGraph.coloring(g1)\
            .withColors(self._createColorsList(100)).applyingBackTrackingAlgorithm0()
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(100, coloredVertices.getRequiredColors())
        self._checkColoring(g1, coloredVertices)

    
    def testCromaticNumberSparseGraph(self) -> None:
        g1 = UndirectedMutableGraph()

        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))
        
        coloredVertices = CommonsGraph.coloring(g1)\
            .withColors(self._createColorsList(1)).applyingBackTrackingAlgorithm0()
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(1, coloredVertices.getRequiredColors())
        self._checkColoring(g1, coloredVertices)
    
    
    def testEmptyGraph(self) -> None:
        g = UndirectedMutableGraph()

        coloredVertices = CommonsGraph.coloring(g)\
            .withColors(createColorsList(1)).applyingBackTrackingAlgorithm0()
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(0, coloredVertices.getRequiredColors())

    
    def testNotEnoughtColorGraph(self) -> None:
        with self.assertRaises(NotEnoughColorsException):
            two = BaseLabeledVertex("2")

            g = CommonsGraph.newUndirectedMutableGraph(
                GraphConnectionGraphColoringBackTrackingTestCase(two)
            )
            CommonsGraph.coloring(g)\
                .withColors(self._createColorsList(1)).applyingBackTrackingAlgorithm0()

    
    def testNullColorGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            CommonsGraph.coloring(g)\
                .withColors(None).applyingBackTrackingAlgorithm0()

    
    def testNullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            CommonsGraph.coloring(None)\
                .withColors(None).applyingBackTrackingAlgorithm0()

    
    def testSudoku(self) -> None:
        try:
            g1 = UndirectedMutableGraph()
            grid = GraphUtils.buildSudokuGraph(g1)

            sudoku = CommonsGraph.coloring(g1)\
                .withColors(self._createColorsList(9)).applyingBackTrackingAlgorithm0()
            self.assertIsNotNone(sudoku)
            self._checkColoring(g1, sudoku)
            self.assertEqual(9, sudoku.getRequiredColors())

            sb = StringIO()
            nf = "{:02d}".format
            sb.write("\n")
            for i in range(9):
                for j in range(9):
                    color = sudoku.getColor(grid[i][j])
                    try:
                        sb.write(f"| {nf(int(color))} | ")
                    except Exception:
                        sb.write(f"| {color} | ")
                sb.write("\n")
            result = dedent(sb.getvalue())
            sb.close()
            logger = logging.getLogger('AnonymousLogger')
            logger.setLevel(logging.DEBUG)
            logger.debug(result)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def testSudokuWithConstraints(self) -> None:
        try:
            g1 = UndirectedMutableGraph()
            grid = GraphUtils.buildSudokuGraph(g1)

            predefinedColor = ColoredVertices()
            predefinedColor.addColor(grid[0][0], 1)
            predefinedColor.addColor(grid[5][5], 8)
            predefinedColor.addColor(grid[1][2], 5)

            sudoku = CommonsGraph.coloring(g1)\
                .with_colors(self._create_colors_list(9))\
                .applyingBacktrackingAlgorithm1(predefinedColor)
            self.assertIsNotNone(sudoku)
            self._checkColoring(g1, sudoku)

            self.assertEqual(9, sudoku.getRequiredColors())
            self.assertEqual(1, int(sudoku.getColor(grid[0][0])))
            self.assertEqual(8, int(sudoku.getColor(grid[5][5])))
            self.assertEqual(5, int(sudoku.getColor(grid[1][2])))

            sb = StringIO()
            nf = "{:02d}".format
            sb.write("\n")
            for i in range(9):
                for j in range(9):
                    color = sudoku.getColor(grid[i][j])
                    try:
                        sb.write(f"| {nf(int(color))} | ")
                    except Exception:
                        sb.write(f"| {color} | ")
                sb.write("\n")
            result = dedent(sb.getvalue())
            sb.close()
            logger = logging.getLogger('AnonymousLogger')
            logger.setLevel(logging.DEBUG)
            logger.debug(result)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End


class GraphConnectionGraphColoringBackTrackingTestCase(AbstractGraphConnection):
    
    def connect0(self) -> None:
        one = self.addVertex(BaseLabeledVertex("1"))
        self.addVertex(self.two)
        three = self.addVertex(BaseLabeledVertex("3"))
        
        self.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(self.two)
        self.addEdge(BaseLabeledEdge("2 -> 3")).from_(self.two).to(three)
        self.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)
    

    def __init__(self, two, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.two = two