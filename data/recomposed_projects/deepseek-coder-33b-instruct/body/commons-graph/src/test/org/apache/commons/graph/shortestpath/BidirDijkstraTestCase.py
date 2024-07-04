from __future__ import annotations
import re
import random
import os
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class BidirDijkstraTestCase(unittest.TestCase):

    __weightOperations: OrderedMonoid[float] = None

    __vertices: typing.List[BaseLabeledVertex] = None

    __graph: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]] = (
        None
    )

    __EPSILON: float = 1.0e-6
    __EDGES: int = 100000
    __NODES: int = 5000
    __TIMES: int = 10

    def testVerifyTwoNodePath(self) -> None:

        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")

        graph.addVertex(one)
        graph.addVertex(two)

        graph.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](one, two, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge[float]("1 -> 2", 14.0), two
        )

        actual = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(one)
            .to(two)
            .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testVerifyThreeNodePath(self) -> None:

        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)

        graph.addEdge(a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c)

        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](a, c, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        expected.addConnectionInTail(
            a, BaseLabeledWeightedEdge[float]("a -> b", 14.0), b
        )
        expected.addConnectionInTail(
            b, BaseLabeledWeightedEdge[float]("b -> c", 10.0), c
        )

        actual = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .from_(a)
            .to(c)
            .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testNullVertices(self) -> None:

        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        with pytest.raises(RuntimeError):
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(None).to_(None).applyingBidirectionalDijkstra(
                DoubleWeightBaseOperations()
            )

    def testNullMonoid(self) -> None:

        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

        with pytest.raises(RuntimeError):
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a).to(b).applyingBidirectionalDijkstra(None)

    def testNullGraph(self) -> None:

        with pytest.raises(RuntimeError):
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None).to_(None).applyingBidirectionalDijkstra(
                DoubleWeightBaseOperations()
            )

    def testNotConnectGraph(self) -> None:

        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

        try:
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge[float]()
            ).from_(a).to(b).applyingBidirectionalDijkstra(DoubleWeightBaseOperations())
        except PathNotFoundException:
            pass
        else:
            raise AssertionError("Expected PathNotFoundException")

    def testFindShortestPathAndVerify(self) -> None:

        pass  # LLM could not translate this method

    def testCompareToUnidirectional(self) -> None:

        r = random.Random()

        for ii in range(self.__TIMES):
            s = self.__vertices[r.randint(0, len(self.__vertices) - 1)]
            t = None

            while True:
                t = self.__vertices[r.randint(0, len(self.__vertices) - 1)]
                if not s.equals(t):
                    break

            pathUni = (
                CommonsGraph.findShortestPath(self.__graph)
                .whereEdgesHaveWeights(BaseWeightedEdge())
                .from_(s)
                .to(t)
                .applyingDijkstra(self.__weightOperations)
            )

            pathBi = (
                CommonsGraph.findShortestPath(self.__graph)
                .whereEdgesHaveWeights(BaseWeightedEdge())
                .from_(s)
                .to(t)
                .applyingBidirectionalDijkstra(self.__weightOperations)
            )

            self.assertEqual(pathUni.getSize(), pathBi.getSize())
            self.assertAlmostEqual(
                pathUni.getWeight(), pathBi.getWeight(), delta=self.__EPSILON
            )

    @staticmethod
    def setUp() -> None:

        pass  # LLM could not translate this method
