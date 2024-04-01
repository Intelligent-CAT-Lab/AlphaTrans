# Imports Begin
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
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
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import pathlib

# Imports End


class FloydWarshallTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testUndirectedShortestPath(self) -> None:

        self.__findShortestPathAndVerify(
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
        )

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
        graph.addVertex(a)
        graph.addVertex(b)
        p = (
            findShortestPath(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge[Double]())
            .applyingFloydWarshall(DoubleWeightBaseOperations())
        )
        p.findShortestPath(a, b)

    def testDirectedShortestPath(self) -> None:

        self.__findShortestPathAndVerify(
            DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
        )

    def __findShortestPathAndVerify(
        self, weighted: Graph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
    ) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
