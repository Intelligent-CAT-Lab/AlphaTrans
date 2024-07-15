from __future__ import annotations
import re
import typing
from typing import *
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

        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)
        input.addVertex(e)
        input.addVertex(f)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7), b)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 21), c)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4), a)

        input.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 7), e)
        input.addEdge(e, BaseLabeledWeightedEdge("e <-> f", 21), f)
        input.addEdge(f, BaseLabeledWeightedEdge("f <-> d", 4), d)

        expected = MutableSpanningTree(DoubleWeightBaseOperations(), BaseWeightedEdge())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4), a)

        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 4), e)
        expected.addEdge(f, BaseLabeledWeightedEdge("f <-> d", 4), d)

        actual = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testVerifyNotConnectGraph2(self) -> None:

        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)
        input.addVertex(e)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7), b)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 21), c)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4), a)

        input.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 4), e)

        expected = MutableSpanningTree(DoubleWeightBaseOperations(), BaseWeightedEdge())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4), a)

        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 4), e)

        actual = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )
        self.assertEqual(expected, actual)

    def testVerifyNotConnectGraph(self) -> None:

        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)

        expected = MutableSpanningTree(DoubleWeightBaseOperations(), BaseWeightedEdge())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)

        actual = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testVerifyMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7), b)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 21), c)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4), a)

        expected = MutableSpanningTree(DoubleWeightBaseOperations(), BaseWeightedEdge())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4), a)

        actual = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testNullMonoid(self) -> None:

        input = None

        with pytest.raises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).applyingReverseDeleteAlgorithm(None)

    def testNullGraph(self) -> None:

        with pytest.raises(TypeError):
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())

    def testEmptyGraph(self) -> None:

        input = UndirectedMutableGraph()

        tree = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(0, tree.getOrder())
        self.assertEqual(0, tree.getSize())
