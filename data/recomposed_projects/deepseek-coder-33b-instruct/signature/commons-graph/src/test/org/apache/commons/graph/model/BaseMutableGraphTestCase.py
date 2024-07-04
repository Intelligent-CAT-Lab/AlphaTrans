from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.utils.GraphUtils import *
from src.test.org.apache.commons.graph.utils.MultiThreadedTestRunner import *
from src.test.org.apache.commons.graph.utils.TestRunner import *


class GraphInsert(TestRunner):

    __end: int = 0

    __start: int = 0

    __g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None

    def runTest(self) -> None:

        pass  # LLM could not translate this method

    def __init__(
        self, g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge], start: int, end: int
    ) -> None:
        self.__g = g
        self.__start = start
        self.__end = end


class BaseMutableGraphTestCase(unittest.TestCase):

    def testUndirectedGraphRemoveEdgeNotExists(self) -> None:

        g = None
        e = None
        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            e = BaseLabeledEdge("NOT EXIST")
        except GraphException as ex:
            self.fail(ex.getMessage())

        with self.assertRaises(GraphException):
            g.removeEdge(e)

    def testUndirectedGraphRemoveEdge(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()

        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))

        GraphUtils.buildCompleteGraph(10, g)

        e = g.getEdge(source, target)
        g.removeEdge(e)

        edge = g.getEdge(source, target)

        self.assertIsNone(edge)

    def testMultiThreadUndirectGraph(self) -> None:

        g = CommonsGraph.synchronize2(
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
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

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))
        edge = g.getEdge(source, target)
        self.assertIsNone(edge)

    def testGetEgdeNotExistsVertex_2(self) -> None:

        g = None
        source = None
        target = None
        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            source = BaseLabeledVertex("1")
            target = BaseLabeledVertex("200")
        except GraphException as e:
            self.fail(e.getMessage())

        with self.assertRaises(GraphException):
            g.getEdge(source, target)

    def testGetEgdeNotExistsVertex(self) -> None:

        g = None
        source = None
        target = None
        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            source = BaseLabeledVertex("100")
            target = BaseLabeledVertex("2")
        except GraphException as e:
            self.fail(e.getMessage())

        with self.assertRaises(GraphException):
            g.getEdge(source, target)

    def testGetEdge(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)

        source = BaseLabeledVertex("1")
        target = BaseLabeledVertex("2")
        edge = g.getEdge(source, target)
        self.assertIsNotNone(edge)

    def testGetConnectedVerticesOnNotConnectedGraph(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()

        for i in range(4):
            v = BaseLabeledVertex(str(i))
            g.addVertex(v)

        testVertex = BaseLabeledVertex(str(1))
        connectedVertices = g.getConnectedVertices(testVertex)
        assert connectedVertices is not None

        v = []
        for baseLabeledVertex in connectedVertices:
            v.append(baseLabeledVertex)

        assert len(v) == 0

    def testGetConnectedVerticesNPE(self) -> None:

        g = None
        notExistsVertex = None
        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            notExistsVertex = BaseLabeledVertex(str(1000))
        except GraphException as e:
            self.fail(e.getMessage())

        with self.assertRaises(GraphException):
            g.getConnectedVertices(notExistsVertex)

    def testGetConnectedVertices(self) -> None:

        g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        GraphUtils.buildCompleteGraph(10, g)

        testVertex = BaseLabeledVertex("1")
        connectedVertices = g.getConnectedVertices(testVertex)
        assert connectedVertices is not None

        v = []
        for baseLabeledVertex in connectedVertices:
            v.append(baseLabeledVertex)

        assert len(v) == 9
        assert testVertex not in v

    def testDirectedMultiTh(self) -> None:

        g = CommonsGraph.synchronize2(DirectedMutableGraph())

        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)

        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)
        mttr.runRunnables()

        self.assertEqual(30, g.getOrder())

        self.assertEqual((30 * (30 - 1)), g.getSize())

    def testDirectedGraphRemoveEdgeNotExists(self) -> None:

        g = None
        e = None
        try:
            g = DirectedMutableGraph()
            GraphUtils.buildCompleteGraph(10, g)

            e = BaseLabeledEdge("NOT EXIST")
        except GraphException as ex:
            self.fail(ex.getMessage())

        with self.assertRaises(GraphException):
            g.removeEdge(e)

    def testDirectedGraphRemoveEdge(self) -> None:

        g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()

        source = BaseLabeledVertex(str(1))
        target = BaseLabeledVertex(str(2))

        GraphUtils.buildCompleteGraph(10, g)

        e = g.getEdge(source, target)
        g.removeEdge(e)

        edge = g.getEdge(source, target)
        self.assertIsNone(edge)

    def testAddVertexAndEdge(self) -> None:

        pass  # LLM could not translate this method
