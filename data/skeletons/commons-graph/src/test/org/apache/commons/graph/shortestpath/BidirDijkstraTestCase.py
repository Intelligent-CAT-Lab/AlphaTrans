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
    def testVerifyTwoNodePath(self) -> None:
        pass

    def testVerifyThreeNodePath(self) -> None:
        pass

    def testNullVertices(self) -> None:
        pass

    def testNullMonoid(self) -> None:
        pass

    def testNullGraph(self) -> None:
        pass

    def testNotConnectGraph(self) -> None:
        pass

    def testFindShortestPathAndVerify(self) -> None:
        pass

    def testCompareToUnidirectional(self) -> None:
        pass

    @staticmethod
    def setUp() -> None:
        pass

    # Class Methods End
