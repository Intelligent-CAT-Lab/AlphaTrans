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
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *


class KruskalTestCase(unittest.TestCase):

    def testVerifyWikipediaMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)
        input.addVertex(e)
        input.addVertex(f)
        input.addVertex(g)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7), b)
        input.addEdge(a, BaseLabeledWeightedEdge("a <-> d", 5), d)

        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 8), c)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> d", 9), d)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> e", 7), e)

        input.addEdge(c, BaseLabeledWeightedEdge("c <-> e", 5), e)

        input.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 15), e)
        input.addEdge(d, BaseLabeledWeightedEdge("d <-> f", 6), f)

        input.addEdge(e, BaseLabeledWeightedEdge("e <-> f", 8), f)
        input.addEdge(e, BaseLabeledWeightedEdge("e <-> g", 9), g)

        input.addEdge(f, BaseLabeledWeightedEdge("f <-> g", 11), g)

        expected = MutableSpanningTree(DoubleWeightBaseOperations(), BaseWeightedEdge())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7), b)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> d", 5), d)
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> e", 9), e)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> e", 5), e)
        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> f", 6), f)
        expected.addEdge(e, BaseLabeledWeightedEdge("e <-> g", 9), g)

        actual = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testVerifyNotConnectedMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7), b)

        expected = MutableSpanningTree(DoubleWeightBaseOperations(), BaseWeightedEdge())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7), b)

        actual = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    @pytest.mark.skip(reason="Ignore")
    def testP4UniformWeightsMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 1.0), b)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 1.0), c)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 1.0), d)

        expected = MutableSpanningTree(DoubleWeightBaseOperations(), BaseWeightedEdge())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 1.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 1.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 1.0), d)

        actual = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testP4NonUniformWeightsMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 4), b)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3), c)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 2), d)

        expected = MutableSpanningTree(DoubleWeightBaseOperations(), BaseWeightedEdge())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 4), b)
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3), c)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 2), d)

        actual = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testNullVertex(self) -> None:

        with pytest.raises(RuntimeError):
            input = UndirectedMutableGraph()
            CommonsGraph.minimumSpanningTree(input).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).fromSource(None).applyingKruskalAlgorithm(DoubleWeightBaseOperations())

    def testNullMonoid(self) -> None:

        input = None
        a = None
        try:
            input = UndirectedMutableGraph()
            a = BaseLabeledVertex("A")
            input.addVertex(a)
        except Exception as e:
            self.fail(str(e))

        CommonsGraph.minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).fromSource(a).applyingKruskalAlgorithm(None)

    def testNullGraph(self) -> None:

        with pytest.raises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).fromArbitrarySource().applyingKruskalAlgorithm(
                DoubleWeightBaseOperations()
            )

    def testNotExistVertex(self) -> None:

        input = UndirectedMutableGraph()

        with pytest.raises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).fromSource(BaseLabeledVertex("NOT EXIST"))

    def testEmptyGraph(self) -> None:

        input = UndirectedMutableGraph()

        with pytest.raises(RuntimeError):
            CommonsGraph.minimumSpanningTree(input).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).fromArbitrarySource().applyingKruskalAlgorithm(
                DoubleWeightBaseOperations()
            )

    def testDisconnectedMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 4), b)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 2), d)

        expected = MutableSpanningTree(DoubleWeightBaseOperations(), BaseWeightedEdge())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 4), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 2), d)

        actual = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)
