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


class PrimTestCase(unittest.TestCase):

    def testVerifyWikipediaMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

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

        input.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)

        input.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 8.0), c)
        input.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> d", 9.0), d)
        input.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> e", 7.0), e)

        input.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)

        input.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> e", 15.0), e)
        input.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)

        input.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> f", 8.0), f)
        input.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)

        input.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> g", 11.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> d", 5.0), d)
        expected.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> e", 7.0), e)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> e", 5.0), e)
        expected.addEdge(d, BaseLabeledWeightedEdge[float]("d <-> f", 6.0), f)
        expected.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)

        self.__internalPrimAssertion(input, d, expected)

    def testVerifyMinimumSpanningTree2(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")
        g = BaseLabeledVertex("g")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)
        input.addVertex(e)
        input.addVertex(f)
        input.addVertex(g)

        input.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        input.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> c", 14.0), c)
        input.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> d", 30.0), d)

        input.addEdge(b, BaseLabeledWeightedEdge[float]("b <-> c", 21.0), c)

        input.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 10.0), d)
        input.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> e", 1.0), e)

        input.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> f", 6.0), f)
        input.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> g", 9.0), g)

        input.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> g", 4.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> b", 7.0), b)
        expected.addEdge(a, BaseLabeledWeightedEdge[float]("a <-> c", 14.0), c)

        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> d", 10.0), d)
        expected.addEdge(c, BaseLabeledWeightedEdge[float]("c <-> e", 1.0), e)

        expected.addEdge(e, BaseLabeledWeightedEdge[float]("e <-> f", 6.0), f)

        expected.addEdge(f, BaseLabeledWeightedEdge[float]("f <-> g", 4.0), g)

        self.__internalPrimAssertion(input, a, expected)

    def testNullVertex(self) -> None:

        input = UndirectedMutableGraph()

        with pytest.raises(RuntimeError):
            minimumSpanningTree(input).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).fromSource(None).applyingPrimAlgorithm(DoubleWeightBaseOperations())

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
        ).fromSource(a).applyingBoruvkaAlgorithm(None)

    def testNullGraph(self) -> None:

        with pytest.raises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).fromArbitrarySource().applyingPrimAlgorithm(DoubleWeightBaseOperations())

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
            ).fromArbitrarySource().applyingPrimAlgorithm(DoubleWeightBaseOperations())

    @staticmethod
    def __internalPrimAssertion(
        input: UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ],
        source: BaseLabeledVertex,
        expected: MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ],
    ) -> None:

        actual = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge[float]())
            .fromSource(source)
            .applyingPrimAlgorithm(DoubleWeightBaseOperations())
        )

        assert expected == actual
