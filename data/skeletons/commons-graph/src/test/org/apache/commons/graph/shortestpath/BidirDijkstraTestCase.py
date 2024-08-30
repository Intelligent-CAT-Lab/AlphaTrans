from __future__ import annotations

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
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import os
import typing
from typing import *
import io
import pathlib

# Imports End


class BidirDijkstraTestCase(unittest.TestCase):

    # Class Fields Begin
    __TIMES: int = None
    __NODES: int = None
    __EDGES: int = None
    __EPSILON: float = None
    __graph: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]] = (
        None
    )
    __vertices: typing.List[BaseLabeledVertex] = None
    __weightOperations: OrderedMonoid[float] = None
    # Class Fields End

    # Class Methods Begin
    def testVerifyTwoNodePath_test10_decomposed(self) -> None:
        pass

    def testVerifyTwoNodePath_test9_decomposed(self) -> None:
        pass

    def testVerifyTwoNodePath_test8_decomposed(self) -> None:
        pass

    def testVerifyTwoNodePath_test7_decomposed(self) -> None:
        pass

    def testVerifyTwoNodePath_test6_decomposed(self) -> None:
        pass

    def testVerifyTwoNodePath_test5_decomposed(self) -> None:
        pass

    def testVerifyTwoNodePath_test4_decomposed(self) -> None:
        pass

    def testVerifyTwoNodePath_test3_decomposed(self) -> None:
        pass

    def testVerifyTwoNodePath_test2_decomposed(self) -> None:
        pass

    def testVerifyTwoNodePath_test1_decomposed(self) -> None:
        pass

    def testVerifyTwoNodePath_test0_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test12_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test11_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test10_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test9_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test8_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test7_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test6_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test5_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test4_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test3_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test2_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test1_decomposed(self) -> None:
        pass

    def testVerifyThreeNodePath_test0_decomposed(self) -> None:
        pass

    def testNullVertices_test4_decomposed(self) -> None:
        pass

    def testNullVertices_test3_decomposed(self) -> None:
        pass

    def testNullVertices_test2_decomposed(self) -> None:
        pass

    def testNullVertices_test1_decomposed(self) -> None:
        pass

    def testNullVertices_test0_decomposed(self) -> None:
        pass

    def testNullMonoid_test7_decomposed(self) -> None:
        pass

    def testNullMonoid_test6_decomposed(self) -> None:
        pass

    def testNullMonoid_test5_decomposed(self) -> None:
        pass

    def testNullMonoid_test4_decomposed(self) -> None:
        pass

    def testNullMonoid_test3_decomposed(self) -> None:
        pass

    def testNullMonoid_test2_decomposed(self) -> None:
        pass

    def testNullMonoid_test1_decomposed(self) -> None:
        pass

    def testNullMonoid_test0_decomposed(self) -> None:
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

    def testNotConnectGraph_test7_decomposed(self) -> None:
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

    def testFindShortestPathAndVerify_test15_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test14_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test13_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test12_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test11_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test10_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test9_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test8_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test7_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test6_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test5_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test4_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test3_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test2_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test1_decomposed(self) -> None:
        pass

    def testFindShortestPathAndVerify_test0_decomposed(self) -> None:
        pass

    def testCompareToUnidirectional_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def setUp() -> None:
        pass

    # Class Methods End
