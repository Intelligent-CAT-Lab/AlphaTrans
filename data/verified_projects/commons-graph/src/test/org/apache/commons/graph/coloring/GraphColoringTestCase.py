import pytest

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
from typing import *
# Imports End

class GraphColoringTestCase(AbstractColoringTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__colors = self._createColorsList(11)
    
    
    @pytest.mark.test
    def testCrawnGraph(self) -> None:
        g = UndirectedMutableGraph()
        GraphUtils.buildCrownGraph(6, g)

        coloredVertices = CommonsGraph.coloring(g)\
            .withColors(self.__colors).applyingGreedyAlgorithm()
        self._checkColoring(g, coloredVertices)
    
    
    @pytest.mark.test
    def testCromaticNumber(self) -> None:
        try:
            g = CommonsGraph.newUndirectedMutableGraph(
                GraphConnectionGraphColoringTestCaseTestCromaticNumber()
            )

            coloredVertices = CommonsGraph.coloring(g)\
                .withColors(self.__colors).applyingGreedyAlgorithm()
            self._checkColoring(g, coloredVertices)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
        
    
    @pytest.mark.test
    def testCromaticNumberBiparted(self) -> None:
        g1 = UndirectedMutableGraph()
        GraphUtils.buildBipartedGraph(100, g1)

        coloredVertices = CommonsGraph.coloring(g1)\
            .withColors(self.__colors).applyingGreedyAlgorithm()
        self._checkColoring(g1, coloredVertices)
    
    
    @pytest.mark.test
    def testCromaticNumberComplete(self) -> None:
        g1 = UndirectedMutableGraph()
        GraphUtils.buildCompleteGraph(100, g1)

        coloredVertices = CommonsGraph.coloring(g1)\
            .withColors(self._createColorsList(100)).applyingGreedyAlgorithm()
        self._checkColoring(g1, coloredVertices)
    
    
    @pytest.mark.test
    def testCromaticNumberSparseGraph(self) -> None:
        g1 = UndirectedMutableGraph()
        for i in range(100):
            g1.addVertex(BaseLabeledVertex(str(i)))
        
        coloredVertices = CommonsGraph.coloring(g1)\
            .withColors(self.__colors).applyingGreedyAlgorithm()
        
        self.assertEqual(1, coloredVertices.getRequiredColors())
        self._checkColoring(g1, coloredVertices)

    
    @pytest.mark.test
    def testEmptyGraph(self) -> None:
        g = UndirectedMutableGraph()

        coloredVertices = CommonsGraph.coloring(g)\
            .withColors(self._createColorsList(1)).applyingGreedyAlgorithm()
        self.assertIsNotNone(coloredVertices)
        self.assertEqual(0, coloredVertices.getRequiredColors())
    
    
    @pytest.mark.test
    def testNotEnoughtColorGreedyGraph(self) -> None:
        with self.assertRaises(NotEnoughColorsException):
            two = BaseLabeledVertex("2")

            g = CommonsGraph.newUndirectedMutableGraph(
                GraphConnectionGraphColoringTestCaseTestNotEnoughtColorGreedyGraph(two)
            )
            CommonsGraph.coloring(g)\
                .withColors(self._createColorsList(1)).applyingGreedyAlgorithm()

    
    @pytest.mark.test
    def testNullColorGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            g = UndirectedMutableGraph()
            CommonsGraph.coloring(g)\
                .withColors(None).applyingBackTrackingAlgorithm0()

    
    @pytest.mark.test
    def testNullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            CommonsGraph.coloring(None)\
                .withColors(None).applyingGreedyAlgorithm()

    
    @pytest.mark.test
    def testSudoku(self) -> None:
        try:
            g1 = UndirectedMutableGraph()
            GraphUtils.buildSudokuGraph(g1)

            col = self._createColorsList(9)
            
            sudoku = CommonsGraph.coloring(g1)\
                .withColors(col).applyingBackTrackingAlgorithm0()
            self._checkColoring(g1, sudoku)
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End


class GraphConnectionGraphColoringTestCaseTestCromaticNumber(AbstractGraphConnection):
    
    def connect0(self) -> None:
        one = self.addVertex(BaseLabeledVertex("1"))
        two = self.addVertex(BaseLabeledVertex("2"))
        three = self.addVertex(BaseLabeledVertex("3"))

        self.addEdge(BaseLabeledEdge("1 -> 2")).from_(one).to(two)
        self.addEdge(BaseLabeledEdge("2 -> 3")).from_(two).to(three)
        self.addEdge(BaseLabeledEdge("3 -> 1")).from_(three).to(one)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GraphConnectionGraphColoringTestCaseTestNotEnoughtColorGreedyGraph(AbstractGraphConnection):
    
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


