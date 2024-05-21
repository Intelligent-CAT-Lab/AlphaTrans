from __future__ import annotations

# Imports Begin
from src.test.org.apache.commons.graph.utils.TestRunner import *
from src.test.org.apache.commons.graph.utils.MultiThreadedTestRunner import *
from src.test.org.apache.commons.graph.utils.GraphUtils import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import io

# Imports End


class GraphInsert(TestRunner):

    # Class Fields Begin
    __g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
    __start: int = None
    __end: int = None
    # Class Fields End

    # Class Methods Begin
    def runTest(self) -> None:
        pass

    def __init__(
        self, g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge], start: int, end: int
    ) -> None:
        pass

    # Class Methods End


class BaseMutableGraphTestCase:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testUndirectedGraphRemoveEdgeNotExists(self) -> None:
        pass

    def testUndirectedGraphRemoveEdge(self) -> None:
        pass

    def testMultiThreadUndirectGraph(self) -> None:
        pass

    def testGetNotExistsEdge(self) -> None:
        pass

    def testGetEgdeNotExistsVertex_2(self) -> None:
        pass

    def testGetEgdeNotExistsVertex(self) -> None:
        pass

    def testGetEdge(self) -> None:
        pass

    def testGetConnectedVerticesOnNotConnectedGraph(self) -> None:
        pass

    def testGetConnectedVerticesNPE(self) -> None:
        pass

    def testGetConnectedVertices(self) -> None:
        pass

    def testDirectedMultiTh(self) -> None:
        pass

    def testDirectedGraphRemoveEdgeNotExists(self) -> None:
        pass

    def testDirectedGraphRemoveEdge(self) -> None:
        pass

    def testAddVertexAndEdge(self) -> None:
        pass

    # Class Methods End
