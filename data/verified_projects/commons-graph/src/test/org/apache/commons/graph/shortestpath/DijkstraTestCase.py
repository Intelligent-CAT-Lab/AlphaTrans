import pytest

# Imports Begin
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import pathlib

# Imports End


class DijkstraTestCase(unittest.TestCase):
    
    @pytest.mark.test
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

        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 6", 14.0), six)
        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 3", 9.0), three)
        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 2", 7.0), two)

        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 3", 10.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 4", 15.0), four)

        graph.addEdge(three, BaseLabeledWeightedEdge("3 -> 6", 2.0), six)
        graph.addEdge(three, BaseLabeledWeightedEdge("3 -> 4", 11.0), four)

        graph.addEdge(four, BaseLabeledWeightedEdge("4 -> 5", 6.0), five)
        graph.addEdge(six, BaseLabeledWeightedEdge("6 -> 5", 9.0), five)

        expected = InMemoryWeightedPath(
            one,
            five,
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge("1 -> 3", 9.0), three
        )
        expected.addConnectionInTail(
            three, BaseLabeledWeightedEdge("3 -> 6", 2.0), six
        )
        expected.addConnectionInTail(
            six, BaseLabeledWeightedEdge("6 -> 5", 9.0), five
        )

        actual = CommonsGraph.findShortestPath(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .from_(one)\
            .to(five)\
            .applyingDijkstra(DoubleWeightBaseOperations())
        
        self.assertEqual(expected, actual)
    
    
    @pytest.mark.test
    def testNotConnectGraph(self) -> None:
        with self.assertRaises(PathNotFoundException):
            graph = UndirectedMutableGraph()

            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")

            graph.addVertex(a)
            graph.addVertex(b)

            CommonsGraph.findShortestPath(graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(a)\
                .to(b)\
                .applyingDijkstra(DoubleWeightBaseOperations())


    @pytest.mark.test
    def testNullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            CommonsGraph.findShortestPath(None)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(None)\
                .to(None)\
                .applyingDijkstra(DoubleWeightBaseOperations())
    
    
    @pytest.mark.test
    def testNullMonoid(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            graph = UndirectedMutableGraph()

            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.addVertex(a)
            graph.addVertex(b)

            CommonsGraph.findShortestPath(graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(a)\
                .to(b)\
                .applyingDijkstra(None)

    
    @pytest.mark.test
    def testNullVertices(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            graph = UndirectedMutableGraph()

            CommonsGraph.findShortestPath(graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(None)\
                .to(None)\
                .applyingDijkstra(DoubleWeightBaseOperations())
