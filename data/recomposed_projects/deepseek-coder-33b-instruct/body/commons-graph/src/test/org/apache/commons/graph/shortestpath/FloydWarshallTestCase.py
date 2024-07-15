from __future__ import annotations
import re
import unittest
import pytest
import pathlib
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *


class FloydWarshallTestCase(unittest.TestCase):

    def testUndirectedShortestPath(self) -> None:

        weighted = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        self.__findShortestPathAndVerify(weighted)

    def testNullGraph(self) -> None:

        with pytest.raises(RuntimeError):
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None).to(None).applyingDijkstra(DoubleWeightBaseOperations())

    def testNotConnectGraph(self) -> None:

        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

        p = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingFloydWarshall(DoubleWeightBaseOperations())
        )

        with pytest.raises(PathNotFoundException):
            p.findShortestPath(a, b)

    def testDirectedShortestPath(self) -> None:

        weighted = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        self.__findShortestPathAndVerify(weighted)

    def __findShortestPathAndVerify(
        self, weighted: Graph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
    ) -> None:

        mutable = cast(
            MutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]], weighted
        )

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")

        mutable.addVertex(one)
        mutable.addVertex(two)
        mutable.addVertex(three)
        mutable.addVertex(four)
        mutable.addVertex(five)
        mutable.addVertex(six)

        mutable.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 6", 14.0), six)
        mutable.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three)
        mutable.addEdge(one, BaseLabeledWeightedEdge[float]("1 -> 2", 7.0), two)

        mutable.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 3", 10.0), three)
        mutable.addEdge(two, BaseLabeledWeightedEdge[float]("2 -> 4", 15.0), four)

        mutable.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six)
        mutable.addEdge(three, BaseLabeledWeightedEdge[float]("3 -> 4", 11.0), four)

        mutable.addEdge(four, BaseLabeledWeightedEdge[float]("4 -> 5", 6.0), five)
        mutable.addEdge(six, BaseLabeledWeightedEdge[float]("6 -> 5", 9.0), five)

        p = (
            CommonsGraph.findShortestPath(weighted)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .applyingFloydWarshall(DoubleWeightBaseOperations())
        )

        if isinstance(weighted, UndirectedGraph):
            assert p.getShortestDistance(one, six) == 11.0
            assert p.getShortestDistance(six, one) == 11.0
            assert p.getShortestDistance(four, five) == 6.0
            assert p.getShortestDistance(five, four) == 6.0
            assert p.getShortestDistance(one, five) == 20.0
            assert p.getShortestDistance(five, one) == 20.0

            wp = p.findShortestPath(one, six)

            expected = InMemoryWeightedPath[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
            ](one, six, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
            expected.addConnectionInTail(
                one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three
            )
            expected.addConnectionInTail(
                three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six
            )

            assert wp == expected
        else:
            assert p.getShortestDistance(one, six) == 11.0
            assert p.getShortestDistance(four, five) == 6.0
            assert p.getShortestDistance(one, five) == 20.0
            assert not p.hasShortestDistance(five, one)

            try:
                wp = p.findShortestPath(five, one)
                pytest.fail("Path from {5} to {1} doesn't exist")
            except PathNotFoundException:
                pass

            expected = InMemoryWeightedPath[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
            ](one, six, DoubleWeightBaseOperations(), BaseWeightedEdge[float]())
            expected.addConnectionInTail(
                one, BaseLabeledWeightedEdge[float]("1 -> 3", 9.0), three
            )
            expected.addConnectionInTail(
                three, BaseLabeledWeightedEdge[float]("3 -> 6", 2.0), six
            )

            wp = p.findShortestPath(one, six)
            assert wp == expected
