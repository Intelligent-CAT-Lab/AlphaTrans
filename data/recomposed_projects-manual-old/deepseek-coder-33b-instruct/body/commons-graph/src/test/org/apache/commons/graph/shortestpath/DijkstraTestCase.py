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
from src.main.org.apache.commons.graph.WeightedPath import *
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


class DijkstraTestCase(unittest.TestCase):

    def testNullVertices(self) -> None:

        with pytest.raises(RuntimeError):
            graph = UndirectedMutableGraph()

            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_vertex(None).to_vertex(None).applyingDijkstra(
                DoubleWeightBaseOperations()
            )

    def testNullMonoid(self) -> None:

        graph = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

        with pytest.raises(RuntimeError):
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a).to(b).applyingDijkstra(None)

    def testNullGraph(self) -> None:

        with pytest.raises(RuntimeError):
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None).to_(None).applyingDijkstra(DoubleWeightBaseOperations())

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
            ).from_(a).to(b).applyingDijkstra(DoubleWeightBaseOperations())
        except PathNotFoundException:
            pass

    def testFindShortestPathAndVerify(self) -> None:

        graph = DirectedMutableGraph()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        six = BaseLabeledVertex("6")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)
        graph.addVertex(six)

        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 6", 14), six)
        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 3", 9), three)
        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 2", 7), two)

        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 3", 10), three)
        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 4", 15), four)

        graph.addEdge(three, BaseLabeledWeightedEdge("3 -> 6", 2), six)
        graph.addEdge(three, BaseLabeledWeightedEdge("3 -> 4", 11), four)

        graph.addEdge(four, BaseLabeledWeightedEdge("4 -> 5", 6), five)
        graph.addEdge(six, BaseLabeledWeightedEdge("6 -> 5", 9), five)

        expected = InMemoryWeightedPath(
            one, five, DoubleWeightBaseOperations(), BaseWeightedEdge()
        )

        expected.addConnectionInTail(one, BaseLabeledWeightedEdge("1 -> 3", 9), three)
        expected.addConnectionInTail(three, BaseLabeledWeightedEdge("3 -> 6", 2), six)
        expected.addConnectionInTail(six, BaseLabeledWeightedEdge("6 -> 5", 9), five)

        actual = (
            CommonsGraph.findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(one)
            .to(five)
            .applyingDijkstra(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)
