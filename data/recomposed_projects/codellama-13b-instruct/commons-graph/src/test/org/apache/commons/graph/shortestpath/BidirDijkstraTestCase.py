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
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import typing
from typing import *
import pathlib
# Imports End

class BidirDijkstraTestCase(unittest.TestCase):

    # Class Fields Begin
    __TIMES: int = 10
    __NODES: int = 5000
    __EDGES: int = 100000
    __EPSILON: float = "" # LLM could not translate field
    __graph: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]] = None
    __vertices: typing.List[BaseLabeledVertex] = None
    __weightOperations: OrderedMonoid[float] = None
    # Class Fields End

    # Class Methods Begin
    def testVerifyTwoNodePath(self) -> None:


        pass # LLM could not translate method body

    def testVerifyThreeNodePath(self) -> None:


        pass # LLM could not translate method body

    def testNullVertices(self) -> None:


        pass # LLM could not translate method body

    def testNullMonoid(self) -> None:

            graph = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[Double]]()
            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.add_vertex(a)
            graph.add_vertex(b)
            self.findShortestPath(graph) \
                .where_edges_have_weights(BaseWeightedEdge[Double]()) \
                .from_(a) \
                .to_(b) \
                .applying_bidirectional_dijkstra(None)

    def testNullGraph(self) -> None:

            self.findShortestPath(None) \
                .whereEdgesHaveWeights(BaseWeightedEdge()) \
                .from_(None) \
                .to_(None) \
                .applyingBidirectionalDijkstra(DoubleWeightBaseOperations())

    def testNotConnectGraph(self) -> None:

            graph = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[Double]]()
            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.add_vertex(a)
            graph.add_vertex(b)
            findShortestPath(graph) \
                .where_edges_have_weights(BaseWeightedEdge[Double]()) \
                .from_(a) \
                .to_(b) \
                .applying_bidirectional_dijkstra(DoubleWeightBaseOperations())

    def testFindShortestPathAndVerify(self) -> None:

            graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[Double]]()
            one = BaseLabeledVertex("1")
            two = BaseLabeledVertex("2")
            three = BaseLabeledVertex("3")
            four = BaseLabeledVertex("4")
            five = BaseLabeledVertex("5")
            six = BaseLabeledVertex("6")
            graph.add_vertex(one)
            graph.add_vertex(two)
            graph.add_vertex(three)
            graph.add_vertex(four)
            graph.add_vertex(five)
            graph.add_vertex(six)
            graph.add_edge(one, BaseLabeledWeightedEdge("1 -> 6", 14.0), six)
            graph.add_edge(one, BaseLabeledWeightedEdge("1 -> 3", 9.0), three)
            graph.add_edge(one, BaseLabeledWeightedEdge("1 -> 2", 7.0), two)
            graph.add_edge(two, BaseLabeledWeightedEdge("2 -> 3", 10.0), three)
            graph.add_edge(two, BaseLabeledWeightedEdge("2 -> 4", 15.0), four)
            graph.add_edge(three, BaseLabeledWeightedEdge("3 -> 6", 2.0), six)
            graph.add_edge(three, BaseLabeledWeightedEdge("3 -> 4", 11.0), four)
            graph.add_edge(four, BaseLabeledWeightedEdge("4 -> 5", 6.0), five)
            graph.add_edge(six, BaseLabeledWeightedEdge("6 -> 5", 9.0), five)
            expected = InMemoryWeightedPath[BaseLabeledVertex, BaseLabeledWeightedEdge[Double], Double](
                one,
                five,
                DoubleWeightBaseOperations(),
                BaseWeightedEdge[Double]()
            )
            expected.add_connection_in_tail(one, BaseLabeledWeightedEdge("1 -> 3", 9.0), three)
            expected.add_connection_in_tail(three, BaseLabeledWeightedEdge("3 -> 6", 2.0), six)
            expected.add_connection_in_tail(six, BaseLabeledWeightedEdge("6 -> 5", 9.0), five)
            actual = findShortestPath(graph) \
                .where_edges_have_weights(BaseWeightedEdge[Double]()) \
                .from_(one) \
                .to_(five) \
                .applying_bidirectional_dijkstra(DoubleWeightBaseOperations())
            self.assertEqual(expected, actual)

    def testCompareToUnidirectional(self) -> None:

            r = random.Random()
            for _ in range(self.__TIMES):
                s = self.__vertices[r.randint(0, len(self.__vertices) - 1)]
                t = self.__vertices[r.randint(0, len(self.__vertices) - 1)]
                while s.equals(t):
                    t = self.__vertices[r.randint(0, len(self.__vertices) - 1)]
                path_uni = self.findShortestPath(self.__graph) \
                    .whereEdgesHaveWeights(BaseWeightedEdge()) \
                    .from_(s) \
                    .to(t) \
                    .applyingDijkstra(self.__weightOperations)
                path_bi = self.findShortestPath(self.__graph) \
                    .whereEdgesHaveWeights(BaseWeightedEdge()) \
                    .from_(s) \
                    .to(t) \
                    .applyingBidirectionalDijkstra(self.__weightOperations)
                assert path_uni.getSize() == path_bi.getSize()
                assert path_uni.getWeight() == path_bi.getWeight()

    @staticmethod

    def setUp() -> None:


        pass # LLM could not translate method body

    # Class Methods End


class new AbstractGraphConnection<BaseLabeledVertex,BaseLabeledWeightedEdge<Double>>(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def connect0(self) -> None:

            self.vertices = []
            for i in range(NODES):
                v = BaseLabeledVertex(str(i))
                self.addVertex(v)
                self.vertices.append(v)
            for i in range(NODES - 1):
                self.__addEdge(self.vertices[i], self.vertices[i + 1])
            self.__addEdge(self.vertices[NODES - 1], self.vertices[0])
            max_edges = max(0, EDGES - NODES)
            for i in range(max_edges):
                while not self.__addEdge(
                        self.vertices[r.nextInt(NODES)],
                        self.vertices[r.nextInt(NODES)]):
                    pass

    def __addEdge(self, src: BaseLabeledVertex, dst: BaseLabeledVertex) -> bool:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


