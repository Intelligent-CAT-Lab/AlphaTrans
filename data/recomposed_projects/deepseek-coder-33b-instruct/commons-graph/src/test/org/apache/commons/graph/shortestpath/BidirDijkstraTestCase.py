# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.GraphException import *
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
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import random
from typing import *
import pathlib
# Imports End

class BidirDijkstraTestCase(unittest.TestCase):

    # Class Fields Begin
    __TIMES = 10
    __NODES = 5000
    __EDGES = 100000
    __EPSILON = 1.0e-6

    __graph = None
    __vertices = []
    __weightOperations = None
    # Class Fields End

    # Class Methods Begin
    @classmethod
    def setUpClass(cls) -> None:
        BidirDijkstraTestCase.__weightOperations = DoubleWeightBaseOperations()

        BidirDijkstraTestCase.__graph = CommonsGraph.newDirectedMutableGraph(
            GraphConnectionBidirDijkstraTestCaseSetUp()
        )

    
    def test_CompareToUnidirectional(self) -> None:
        r = random.Random()
        for ii in range(self.__TIMES):
            s = BidirDijkstraTestCase\
                .__vertices[r.randint(0, len(BidirDijkstraTestCase.__vertices) - 1)]
            t = BidirDijkstraTestCase\
                .__vertices[r.randint(0, len(BidirDijkstraTestCase.__vertices) - 1)]

            while s.equals(t):
                t = BidirDijkstraTestCase\
                    .__vertices[r.randint(0, len(BidirDijkstraTestCase.__vertices) - 1)]
                
            pathUni = CommonsGraph.findShortestPath(BidirDijkstraTestCase.__graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(s)\
                .to(t)\
                .applyingDijkstra(BidirDijkstraTestCase.__weightOperations)
            
            pathBi = CommonsGraph.findShortestPath(BidirDijkstraTestCase.__graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(s)\
                .to(t)\
                .applyingBidirectionalDijkstra(BidirDijkstraTestCase.__weightOperations)
            
            self.assertEqual(pathUni.getSize(), pathBi.getSize())
            self.assertEqual(pathUni.getWeight(), pathBi.getWeight())

    
    def test_FindShortestPathAndVerify(self) -> None:
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

        expected.addConnectionInTail(one, BaseLabeledWeightedEdge("1 -> 3", 9.0), three)
        expected.addConnectionInTail(three, BaseLabeledWeightedEdge("3 -> 6", 2.0), six)
        expected.addConnectionInTail(six, BaseLabeledWeightedEdge("6 -> 5", 9.0), five)

        actual = CommonsGraph.findShortestPath(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge()) \
            .from_(one)\
            .to(five)\
            .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())
        
        self.assertEqual(expected, actual)

    
    def test_NotConnectGraph(self) -> None:
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
                .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())

    
    def test_NullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            CommonsGraph.findShortestPath(None)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(None)\
                .to(None)\
                .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())
    
    
    def test_NullMonoid(self) -> None:
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
                .applyingBidirectionalDijkstra(None)

    
    def test_NullVertices(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            graph = UndirectedMutableGraph()

            CommonsGraph.findShortestPath(graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(None)\
                .to(None)\
                .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())

    
    def test_VerifyThreeNodePath(self) -> None:
        graph = DirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        graph.addVertex(a)
        graph.addVertex(b)
        graph.addVertex(c)

        graph.addEdge(a, BaseLabeledWeightedEdge("a -> b", 14.0), b)
        graph.addEdge(b, BaseLabeledWeightedEdge("b -> c", 10.0), c)

        expected = InMemoryWeightedPath(
            a,
            c,
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        expected.addConnectionInTail(a, BaseLabeledWeightedEdge("a -> b", 14.0), b)
        expected.addConnectionInTail(b, BaseLabeledWeightedEdge("b -> c", 10.0), c)

        actual = CommonsGraph.findShortestPath(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .from_(a)\
            .to(c)\
            .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())

        self.assertEqual(expected, actual)
    
    
    def test_VerifyTwoNodePath(self) -> None:
        graph = DirectedMutableGraph()

        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")

        graph.addVertex(one)
        graph.addVertex(two)

        graph.addEdge(one, BaseLabeledWeightedEdge("1 -> 2", 14.0), two)

        expected = InMemoryWeightedPath(
            one,
            two,
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        expected.addConnectionInTail(one, BaseLabeledWeightedEdge("1 -> 2", 14.0), two)

        actual = CommonsGraph.findShortestPath(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .from_(one)\
            .to(two)\
            .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())

        self.assertEqual(expected, actual)

    # Class Methods End


class GraphConnectionBidirDijkstraTestCaseSetUp(AbstractGraphConnection):

    def __addEdge(self, src, dst) -> bool:
        try:
            edge = BaseLabeledWeightedEdge(
                "{src} -> {dst}".format(src=src, dst=dst),
                10.0 * self.r.random() + 1.0
            )
            self.addEdge(edge).from_(src).to(dst)
            return True
        except GraphException as e:
            return False

    
    def connect0(self) -> None:
        BidirDijkstraTestCase.__vertices = []
        for i in range(BidirDijkstraTestCase.__NODES):
            v = BaseLabeledVertex(str(i))
            self.addVertex(v)
            BidirDijkstraTestCase.__vertices.append(v)
        
        for i in range(BidirDijkstraTestCase.__NODES - 1):
            self.__addEdge(
                BidirDijkstraTestCase.__vertices[i],
                BidirDijkstraTestCase.__vertices[i + 1]
            )

        self.__addEdge(
            BidirDijkstraTestCase.__vertices[BidirDijkstraTestCase.__NODES - 1],
            BidirDijkstraTestCase.__vertices[0]
        )
        
        maxEdges = max(
            0,
            BidirDijkstraTestCase.__EDGES - BidirDijkstraTestCase.__NODES
        )

        for i in range(maxEdges):
            while not self.__addEdge(
                BidirDijkstraTestCase\
                    .__vertices[self.r.randint(0, BidirDijkstraTestCase.__NODES - 1)],
                BidirDijkstraTestCase\
                    .__vertices[self.r.randint(0, BidirDijkstraTestCase.__NODES - 1)]
            ):
                pass
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.r = random.Random()
