from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *


class ReverseDeleteTestCase(unittest.TestCase):

    def testVerifyNotConnectGraph3(self) -> None:

        pass  # LLM could not translate this method

    def testVerifyNotConnectGraph2(self) -> None:

        pass  # LLM could not translate this method

    def testVerifyNotConnectGraph(self) -> None:
        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double], Double
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[Double]())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)

        actual = (
            minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge[Double]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )
        self.assertEqual(expected, actual)

    def testVerifyMinimumSpanningTree(self) -> None:

        pass  # LLM could not translate this method

    def testNullMonoid(self) -> None:
        input = None
        CommonsGraph.minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).applyingReverseDeleteAlgorithm(None)

    def testNullGraph(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())

    def testEmptyGraph(self) -> None:
        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        tree = (
            minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge[Double]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )
        self.assertEqual(0, tree.getOrder())
        self.assertEqual(0, tree.getSize())
