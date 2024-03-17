# Imports Begin
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
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import pathlib

# Imports End


class DijkstraTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testNullVertices(self) -> None:

        pass  # LLM could not translate method body

    def testNullMonoid(self) -> None:

        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.add_vertex(a)
        graph.add_vertex(b)
        findShortestPath(graph).where_edges_have_weights(
            BaseWeightedEdge[Double]()
        ).from_(a).to_(b).applying_dijkstra(None)

    def testNullGraph(self) -> None:

        self.findShortestPath(None).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
            None
        ).to_(None).applyingDijkstra(DoubleWeightBaseOperations())

    def testNotConnectGraph(self) -> None:

        graph = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.add_vertex(a)
        graph.add_vertex(b)
        self.findShortestPath(graph).where_edges_have_weights(
            BaseWeightedEdge[Double]()
        ).from_(a).to_(b).applying_dijkstra(DoubleWeightBaseOperations())

    def testFindShortestPathAndVerify(self) -> None:

        graph = DirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
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
        graph.add_edge(one, BaseLabeledWeightedEdge[Double]("1 -> 6", 14.0), six)
        graph.add_edge(one, BaseLabeledWeightedEdge[Double]("1 -> 3", 9.0), three)
        graph.add_edge(one, BaseLabeledWeightedEdge[Double]("1 -> 2", 7.0), two)
        graph.add_edge(two, BaseLabeledWeightedEdge[Double]("2 -> 3", 10.0), three)
        graph.add_edge(two, BaseLabeledWeightedEdge[Double]("2 -> 4", 15.0), four)
        graph.add_edge(three, BaseLabeledWeightedEdge[Double]("3 -> 6", 2.0), six)
        graph.add_edge(three, BaseLabeledWeightedEdge[Double]("3 -> 4", 11.0), four)
        graph.add_edge(four, BaseLabeledWeightedEdge[Double]("4 -> 5", 6.0), five)
        graph.add_edge(six, BaseLabeledWeightedEdge[Double]("6 -> 5", 9.0), five)
        expected = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double], Double
        ](one, five, DoubleWeightBaseOperations(), BaseWeightedEdge[Double]())
        expected.add_connection_in_tail(
            one, BaseLabeledWeightedEdge[Double]("1 -> 3", 9.0), three
        )
        expected.add_connection_in_tail(
            three, BaseLabeledWeightedEdge[Double]("3 -> 6", 2.0), six
        )
        expected.add_connection_in_tail(
            six, BaseLabeledWeightedEdge[Double]("6 -> 5", 9.0), five
        )
        actual = (
            findShortestPath(graph)
            .where_edges_have_weights(BaseWeightedEdge[Double]())
            .from_(one)
            .to(five)
            .applying_dijkstra(DoubleWeightBaseOperations())
        )
        self.assertEqual(expected, actual)

    # Class Methods End
