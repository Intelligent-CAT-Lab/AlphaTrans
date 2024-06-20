from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import io

# Imports End


class KruskalTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testVerifyWikipediaMinimumSpanningTree(self) -> None:
        pass

    def testVerifyNotConnectedMinimumSpanningTree(self) -> None:
        pass

    def testP4UniformWeightsMinimumSpanningTree(self) -> None:
        pass

    def testP4NonUniformWeightsMinimumSpanningTree(self) -> None:
        pass

    def testNullVertex(self) -> None:
        pass

    def testNullMonoid(self) -> None:
        pass

    def testNullGraph(self) -> None:
        pass

    def testNotExistVertex(self) -> None:
        pass

    def testEmptyGraph(self) -> None:
        pass

    def testDisconnectedMinimumSpanningTree(self) -> None:
        pass

    # Class Methods End
