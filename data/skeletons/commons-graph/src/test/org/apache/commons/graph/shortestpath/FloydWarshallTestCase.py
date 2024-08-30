from __future__ import annotations

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
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import os
import io
import pathlib

# Imports End


class FloydWarshallTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testUndirectedShortestPath_test0_decomposed(self) -> None:
        pass

    def testNullGraph_test4_decomposed(self) -> None:
        pass

    def testNullGraph_test3_decomposed(self) -> None:
        pass

    def testNullGraph_test2_decomposed(self) -> None:
        pass

    def testNullGraph_test1_decomposed(self) -> None:
        pass

    def testNullGraph_test0_decomposed(self) -> None:
        pass

    def testNotConnectGraph_test6_decomposed(self) -> None:
        pass

    def testNotConnectGraph_test5_decomposed(self) -> None:
        pass

    def testNotConnectGraph_test4_decomposed(self) -> None:
        pass

    def testNotConnectGraph_test3_decomposed(self) -> None:
        pass

    def testNotConnectGraph_test2_decomposed(self) -> None:
        pass

    def testNotConnectGraph_test1_decomposed(self) -> None:
        pass

    def testNotConnectGraph_test0_decomposed(self) -> None:
        pass

    def testDirectedShortestPath_test0_decomposed(self) -> None:
        pass

    def __findShortestPathAndVerify(
        self, weighted: Graph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
    ) -> None:
        pass

    # Class Methods End
