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

        self.__findShortestPathAndVerify(
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]()
        )

    def testNullGraph(self) -> None:

        with pytest.raises(RuntimeError):
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None).to_(None).applyingDijkstra(DoubleWeightBaseOperations())

    def testNotConnectGraph(self) -> None:

        graph = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

        p = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .applyingFloydWarshall(DoubleWeightBaseOperations())
        )

        with pytest.raises(PathNotFoundException):
            p.findShortestPath(a, b)

    def testDirectedShortestPath(self) -> None:

        self.__findShortestPathAndVerify(
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]()
        )

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

        mutable.addEdge(one, BaseLabeledWeightedEdge("1 -> 6", 14.0), six)
        mutable.addEdge(one, BaseLabeledWeightedEdge("1 -> 3", 9.0), three)
        mutable.addEdge(one, BaseLabeledWeightedEdge("1 -> 2", 7.0), two)

        mutable.addEdge(two, BaseLabeledWeightedEdge("2 -> 3", 10.0), three)
        mutable.addEdge(two, BaseLabeledWeightedEdge("2 -> 4", 15.0), four)

        mutable.addEdge(three, BaseLabeledWeightedEdge("3 -> 6", 2.0), six)
        mutable.addEdge(three, BaseLabeledWeightedEdge("3 -> 4", 11.0), four)

        mutable.addEdge(four, BaseLabeledWeightedEdge("4 -> 5", 6.0), five)
        mutable.addEdge(six, BaseLabeledWeightedEdge("6 -> 5", 9.0), five)

        p = (
            CommonsGraph.findShortestPath(weighted)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .applyingFloydWarshall(DoubleWeightBaseOperations())
        )

        if isinstance(weighted, UndirectedGraph):
            self.assertEqual(11.0, p.getShortestDistance(one, six))

            self.assertEqual(11.0, p.getShortestDistance(six, one))

            self.assertEqual(6.0, p.getShortestDistance(four, five))
            self.assertEqual(6.0, p.getShortestDistance(five, four))

            self.assertEqual(20.0, p.getShortestDistance(one, five))
            self.assertEqual(20.0, p.getShortestDistance(five, one))

            wp = p.findShortestPath(one, six)

            expected = InMemoryWeightedPath(
                one, six, DoubleWeightBaseOperations(), BaseWeightedEdge()
            )
            expected.addConnectionInTail(
                one, BaseLabeledWeightedEdge("1 -> 3", 9.0), three
            )
            expected.addConnectionInTail(
                three, BaseLabeledWeightedEdge("3 -> 6", 2.0), six
            )

            self.assertEqual(expected, wp)
        else:
            self.assertEqual(11.0, p.getShortestDistance(one, six))

            self.assertEqual(6.0, p.getShortestDistance(four, five))

            self.assertEqual(20.0, p.getShortestDistance(one, five))
            self.assertFalse(p.hasShortestDistance(five, one))

            try:
                wp = p.findShortestPath(five, one)
                self.fail("Path from {5} to {1} doesn't exist")
            except PathNotFoundException:
                pass

            expected = InMemoryWeightedPath(
                one, six, DoubleWeightBaseOperations(), BaseWeightedEdge()
            )
            expected.addConnectionInTail(
                one, BaseLabeledWeightedEdge("1 -> 3", 9.0), three
            )
            expected.addConnectionInTail(
                three, BaseLabeledWeightedEdge("3 -> 6", 2.0), six
            )

            wp = p.findShortestPath(one, six)
            self.assertEqual(expected, wp)
