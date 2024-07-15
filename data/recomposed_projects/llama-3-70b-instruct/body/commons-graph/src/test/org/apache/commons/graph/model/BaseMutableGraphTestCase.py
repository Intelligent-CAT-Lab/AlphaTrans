from __future__ import annotations
import re
import typing
from typing import *
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
        for i in range(self.__start, self.__end):
            v: BaseLabeledVertex = BaseLabeledVertex(str(i))
            self.__g.addVertex(v)
        with self.__g:
            for v1 in self.__g.getVertices0():
                for v2 in self.__g.getVertices0():
                    if v1 != v2:
                        try:
                            e: BaseLabeledEdge = BaseLabeledEdge(v1 + " -> " + v2)
                            self.__g.addEdge(v1, e, v2)
                        except GraphException as e:
                            pass

    def __init__(
        self, g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge], start: int, end: int
    ) -> None:
        self.__g = g
        self.__start = start
        self.__end = end


class BaseMutableGraphTestCase(unittest.TestCase):

    def testUndirectedGraphRemoveEdgeNotExists(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        e: BaseLabeledEdge = None
        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            e = BaseLabeledEdge("NOT EXIST")
        except GraphException as ex:
            self.fail(ex.getMessage())

        g.removeEdge(e)

    def testUndirectedGraphRemoveEdge(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )

        source: BaseLabeledVertex = BaseLabeledVertex("1")
        target: BaseLabeledVertex = BaseLabeledVertex("2")

        GraphUtils.buildCompleteGraph(10, g)

        e: BaseLabeledEdge = g.getEdge(source, target)
        g.removeEdge(e)

        edge: BaseLabeledEdge = g.getEdge(source, target)

        self.assertIsNone(edge)

    def testMultiThreadUndirectGraph(self) -> None:
        g = CommonsGraph.synchronize2(UndirectedMutableGraph())
        tr1 = GraphInsert(g, 0, 10)
        tr2 = GraphInsert(g, 10, 20)
        tr3 = GraphInsert(g, 20, 30)
        trs = [tr1, tr2, tr3]
        mttr = MultiThreadedTestRunner(trs)
        mttr.runRunnables()
        self.assertEqual(30, g.getOrder())
        self.assertEqual((30 * (30 - 1) / 2), g.getSize())

    def testGetNotExistsEdge(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        for i in range(0, 4):
            v: BaseLabeledVertex = BaseLabeledVertex(str(i))
            g.addVertex(v)

        source: BaseLabeledVertex = BaseLabeledVertex(str(1))
        target: BaseLabeledVertex = BaseLabeledVertex(str(2))
        edge: BaseLabeledEdge = g.getEdge(source, target)
        self.assertIsNone(edge)

    def testGetEgdeNotExistsVertex_2(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        source: BaseLabeledVertex = None
        target: BaseLabeledVertex = None
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
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        source: BaseLabeledVertex = None
        target: BaseLabeledVertex = None
        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            source = BaseLabeledVertex(str(100))
            target = BaseLabeledVertex(str(2))
        except GraphException as e:
            self.fail(e.getMessage())

        with self.assertRaises(GraphException):
            g.getEdge(source, target)

    def testGetEdge(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            UndirectedMutableGraph()
        )
        GraphUtils.buildCompleteGraph(10, g)

        source: BaseLabeledVertex = BaseLabeledVertex("1")
        target: BaseLabeledVertex = BaseLabeledVertex("2")
        edge: BaseLabeledEdge = g.getEdge(source, target)
        self.assertIsNotNone(edge)

    def testGetConnectedVerticesOnNotConnectedGraph(self) -> None:

        pass  # LLM could not translate this method

    def testGetConnectedVerticesNPE(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        notExistsVertex: BaseLabeledVertex = None
        try:
            g = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            notExistsVertex = BaseLabeledVertex(str(1000))
        except GraphException as e:
            self.fail(e.getMessage())
        g.getConnectedVertices(notExistsVertex)

    def testGetConnectedVertices(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        GraphUtils.buildCompleteGraph(10, g)

        testVertex: BaseLabeledVertex = BaseLabeledVertex("1")
        connectedVertices: Iterable[BaseLabeledVertex] = g.getConnectedVertices(
            testVertex
        )
        self.assertIsNotNone(connectedVertices)

        v: List[BaseLabeledVertex] = []
        for baseLabeledVertex in connectedVertices:
            v.append(baseLabeledVertex)

        self.assertEqual(9, len(v))
        self.assertFalse(testVertex in v)

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
        g: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
        e: BaseLabeledEdge = None
        try:
            g = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            GraphUtils.buildCompleteGraph(10, g)

            e = BaseLabeledEdge("NOT EXIST")
        except GraphException as ex:
            self.fail(ex.getMessage())

        g.removeEdge(e)

    def testDirectedGraphRemoveEdge(self) -> None:
        g: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            DirectedMutableGraph()
        )
        source: BaseLabeledVertex = BaseLabeledVertex("1")
        target: BaseLabeledVertex = BaseLabeledVertex("2")
        GraphUtils.buildCompleteGraph(10, g)
        e: BaseLabeledEdge = g.getEdge(source, target)
        g.removeEdge(e)
        edge: BaseLabeledEdge = g.getEdge(source, target)
        self.assertIsNone(edge)

    def testAddVertexAndEdge(self) -> None:
        g: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        GraphUtils.buildCompleteGraph(50, g)

        self.assertEqual(50, g.getOrder())
        self.assertEqual(1225, g.getSize())
        for v in g.getVertices0():
            self.assertEqual(49, g.getDegree(v))

        gDirect: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        GraphUtils.buildCompleteGraph(50, gDirect)

        self.assertEqual(50, gDirect.getOrder())
        self.assertEqual(2450, gDirect.getSize())
        for v in gDirect.getVertices0():
            self.assertEqual(98, gDirect.getDegree(v))

        gSimple: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
        )
        one: BaseLabeledVertex = BaseLabeledVertex("1")
        two: BaseLabeledVertex = BaseLabeledVertex("2")
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
