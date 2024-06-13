# Imports Begin
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
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
import typing
from typing import *
import pathlib

# Imports End


class BellmannFordTestCase(unittest.TestCase):

    def testFindShortestPathAndVerify(self) -> None:
        graph = DirectedMutableGraph()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")

        graph.addVertex(one)
        graph.addVertex(two)
        graph.addVertex(three)
        graph.addVertex(four)
        graph.addVertex(five)

        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 2", 6.0), two)
        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 4", 7.0), four)

        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 3", 5.0), three)
        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 5", -4.0), five)
        graph.addEdge(two, BaseLabeledWeightedEdge("2 -> 4", 8.0), four)

        graph.addEdge(three, BaseLabeledWeightedEdge("3 -> 2", -2.0), two)

        graph.addEdge(four, BaseLabeledWeightedEdge("4 -> 3", -3.0), three)
        graph.addEdge(four, BaseLabeledWeightedEdge("4 -> 5", 9.0), five)

        graph.addEdge(five, BaseLabeledWeightedEdge("5 -> 3", 7.0), three)
        graph.addEdge(five, BaseLabeledWeightedEdge("5 -> 1", 2.0), one)

        expected = InMemoryWeightedPath(
            one,
            three,
            DoubleWeightBaseOperations(), 
            BaseWeightedEdge()
        )
        expected.addConnectionInTail(
            one, BaseLabeledWeightedEdge("1 -> 4", 7.0), four
        )
        expected.addConnectionInTail(
            four, BaseLabeledWeightedEdge("4 -> 3", -3.0), three
        )

        allVertexPairsShortestPath = CommonsGraph.findShortestPath(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .from_(one)\
            .applyingBelmannFord(DoubleWeightBaseOperations())
        
        actual = allVertexPairsShortestPath.findShortestPath(one, three)
        self.assertEqual(expected, actual)
    
    
    def testNotConnectGraph(self) -> None:
        with self.assertRaises(PathNotFoundException):
            a = None
            b = None
            allVertexPairsShortestPath = None
            try:
                graph = UndirectedMutableGraph()

                a = BaseLabeledVertex("a")
                b = BaseLabeledVertex("b")
                graph.addVertex(a)
                graph.addVertex(b)

                allVertexPairsShortestPath = CommonsGraph.findShortestPath(graph)\
                    .whereEdgesHaveWeights(BaseWeightedEdge())\
                    .from_(a)\
                    .applyingBelmannFord(DoubleWeightBaseOperations())
            except PathNotFoundException as e:
                self.fail(str(e))
            allVertexPairsShortestPath.findShortestPath(a, b)

    
    def testNullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            CommonsGraph.findShortestPath(None)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(None)\
                .applyingBelmannFord(DoubleWeightBaseOperations())

    
    def testNullMonoid(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            graph = None
            a = None
            try:
                graph = UndirectedMutableGraph()

                a = BaseLabeledVertex("a")
                b = BaseLabeledVertex("b")
                graph.addVertex(a)
                graph.addVertex(b)
            except NullPointerException as e:
                self.fail(e.getMessage())

            CommonsGraph.findShortestPath(graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(a)\
                .applyingBelmannFord(None)

    
    def testNullVertices(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            graph = UndirectedMutableGraph()

        CommonsGraph.findShortestPath(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .from_(None)\
            .applyingBelmannFord(DoubleWeightBaseOperations())
