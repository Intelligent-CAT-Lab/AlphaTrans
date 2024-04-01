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
from src.main.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
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

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testNullVertices(self) -> None:

        pass  # LLM could not translate method body

    def testNullMonoid(self) -> None:

        graph: typing.Any = None
        a: BaseLabeledVertex = None
        try:
            graph = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()
            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.add_vertex(a)
            graph.add_vertex(b)
        except NullPointerException as e:
            self.fail(e.getMessage())
        self.findShortestPath(graph).where_edges_have_weights(
            BaseWeightedEdge[float]()
        ).from_(a).applying_belmann_ford(None)

    def testNullGraph(self) -> None:

        self.findShortestPath(None).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            None
        ).applyingBelmannFord(DoubleWeightBaseOperations())

    def testNotConnectGraph(self) -> None:

        pass  # LLM could not translate method body

    def testFindShortestPathAndVerify(self) -> None:

        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        one = BaseLabeledVertex("1")
        two = BaseLabeledVertex("2")
        three = BaseLabeledVertex("3")
        four = BaseLabeledVertex("4")
        five = BaseLabeledVertex("5")
        graph.add_vertex(one)
        graph.add_vertex(two)
        graph.add_vertex(three)
        graph.add_vertex(four)
        graph.add_vertex(five)
        graph.add_edge(one, BaseLabeledWeightedEdge("1 -> 2", 6.0), two)
        graph.add_edge(one, BaseLabeledWeightedEdge("1 -> 4", 7.0), four)
        graph.add_edge(two, BaseLabeledWeightedEdge("2 -> 3", 5.0), three)
        graph.add_edge(two, BaseLabeledWeightedEdge("2 -> 5", -4.0), five)
        graph.add_edge(two, BaseLabeledWeightedEdge("2 -> 4", 8.0), four)
        graph.add_edge(three, BaseLabeledWeightedEdge("3 -> 2", -2.0), two)
        graph.add_edge(four, BaseLabeledWeightedEdge("4 -> 3", -3.0), three)
        graph.add_edge(four, BaseLabeledWeightedEdge("4 -> 5", 9.0), five)
        graph.add_edge(five, BaseLabeledWeightedEdge("5 -> 3", 7.0), three)
        graph.add_edge(five, BaseLabeledWeightedEdge("5 -> 1", 2.0), one)
        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double], Double
        ](one, three, DoubleWeightBaseOperations(), BaseWeightedEdge[Double]())
        expected.add_connection_in_tail(
            one, BaseLabeledWeightedEdge("1 -> 4", 7.0), four
        )
        expected.add_connection_in_tail(
            four, BaseLabeledWeightedEdge("4 -> 3", -3.0), three
        )
        all_vertex_pairs_shortest_path = (
            self.find_shortest_path(graph)
            .where_edges_have_weights(BaseWeightedEdge[Double]())
            .from_(one)
            .applying_belmann_ford(DoubleWeightBaseOperations())
        )
        actual = all_vertex_pairs_shortest_path.find_shortest_path(one, three)
        assert expected == actual

    # Class Methods End
