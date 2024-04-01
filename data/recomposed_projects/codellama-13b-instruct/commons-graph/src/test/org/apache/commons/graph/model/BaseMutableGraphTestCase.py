# Imports Begin
from src.main.org.apache.commons.graph.utils.TestRunner import *
from src.main.org.apache.commons.graph.utils.MultiThreadedTestRunner import *
from src.main.org.apache.commons.graph.utils.GraphUtils import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest

# Imports End


class GraphInsert(unittest.TestCase, TestRunner):

    # Class Fields Begin
    __g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
    __start: int = None
    __end: int = None
    # Class Fields End

    # Class Methods Begin
    def runTest(self) -> None:

        for i in range(self.__start, self.__end):
            v = BaseLabeledVertex(str(i))
            self.__g.addVertex(v)
        with self.__g:
            for v1 in self.__g.getVertices0():
                for v2 in self.__g.getVertices0():
                    if not v1.equals(v2):
                        try:
                            e = BaseLabeledEdge(f"{v1} -> {v2}")
                            self.__g.addEdge(v1, e, v2)
                        except GraphException:
                            pass

    def __init__(
        self, g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge], start: int, end: int
    ) -> None:

        self.g = g
        self.start = start
        self.end = end

    # Class Methods End


class BaseMutableGraphTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testUndirectedGraphRemoveEdgeNotExists(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        e = BaseLabeledEdge("NOT EXIST")
        try:
            buildCompleteGraph(10, g)
        except GraphException as ex:
            self.fail(ex.getMessage())
        g.removeEdge(e)

    def testUndirectedGraphRemoveEdge(self) -> None:

        pass  # LLM could not translate method body

    def testMultiThreadUndirectGraph(self) -> None:

        g = MutableGraph[BaseLabeledVertex, BaseLabeledEdge](
            CommonsGraph.synchronize2(
                UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            )
        )
        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)
        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)
        mttr.runRunnables()
        self.assertEqual(30, g.getOrder())
        self.assertEqual((30 * (30 - 1) / 2), g.getSize())

    def testGetNotExistsEdge(self) -> None:

        pass  # LLM could not translate method body

    def testGetEgdeNotExistsVertex_2(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(1)
        target = BaseLabeledVertex(200)
        try:
            buildCompleteGraph(10, g)
        except GraphException as e:
            self.fail(e.message)
        g.getEdge(source, target)

    def testGetEgdeNotExistsVertex(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        source = BaseLabeledVertex(100)
        target = BaseLabeledVertex(2)
        try:
            buildCompleteGraph(10, g)
        except GraphException as e:
            self.fail(e.message)
        g.getEdge(source, target)

    def testGetEdge(self) -> None:

        pass  # LLM could not translate method body

    def testGetConnectedVerticesOnNotConnectedGraph(self) -> None:

        pass  # LLM could not translate method body

    def testGetConnectedVerticesNPE(self) -> None:

        pass  # LLM could not translate method body

    def testGetConnectedVertices(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        buildCompleteGraph(10, g)
        testVertex = BaseLabeledVertex(valueOf(1))
        connectedVertices = g.getConnectedVertices(testVertex)
        assertNotNull(connectedVertices)
        v = []
        for baseLabeledVertex in connectedVertices:
            v.append(baseLabeledVertex)
        self.assertEqual(9, len(v))
        self.assertFalse(testVertex in v)

    def testDirectedMultiTh(self) -> None:

        g = MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            CommonsGraph.synchronize2(
                DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            )
        )
        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)
        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)
        mttr.runRunnables()
        self.assertEqual(30, g.getOrder())
        self.assertEqual((30 * (30 - 1)), g.getSize())

    def testDirectedGraphRemoveEdgeNotExists(self) -> None:

        g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        e = BaseLabeledEdge("NOT EXIST")
        try:
            buildCompleteGraph(10, g)
        except GraphException as ex:
            self.fail(ex.getMessage())
        g.removeEdge(e)

    def testDirectedGraphRemoveEdge(self) -> None:

        pass  # LLM could not translate method body

    def testAddVertexAndEdge(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        self.buildCompleteGraph(50, g)
        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))
        gDirect = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        self.buildCompleteGraph(50, gDirect)
        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))
        gSimple = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        gSimple.addVertex(one)
        gSimple.addVertex(two)
        gSimple.addEdge(one, BaseLabeledEdge("1 -> 2"), two)
        self.assertEqual(2, gSimple.getOrder())
        self.assertEqual(1, gSimple.getSize())
        self.assertEqual(1, gSimple.getDegree(one))
        self.assertEqual(1, gSimple.getDegree(two))
        self.assertEqual(0, gSimple.getInDegree(one))
        self.assertEqual(1, gSimple.getInDegree(two))
        self.assertEqual(1, gSimple.getOutDegree(one))
        self.assertEqual(0, gSimple.getOutDegree(two))
        self.assertFalse(gSimple.containsEdge(BaseLabeledEdge("Not Exist Edge")))
        self.assertFalse(gSimple.containsVertex(BaseLabeledVertex("Not exist vertex")))

    # Class Methods End
