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


class BoruvkaTestCase(unittest.TestCase):

    def testverifySparseGraphMinimumSpanningTree(self) -> None:
        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        input.addVertex(BaseLabeledVertex("A"))
        input.addVertex(BaseLabeledVertex("B"))
        input.addVertex(BaseLabeledVertex("C"))
        input.addVertex(BaseLabeledVertex("D"))
        input.addVertex(BaseLabeledVertex("E"))
        input.addVertex(BaseLabeledVertex("F"))
        input.addVertex(BaseLabeledVertex("G"))
        CommonsGraph.minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[Double]()
        ).fromArbitrarySource().applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())

    def testVerifyWikipediaMinimumSpanningTree(self) -> None:
        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[double]
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

        input.addEdge(a, BaseLabeledWeightedEdge[double]("a <-> b", 7.0), b)
        input.addEdge(a, BaseLabeledWeightedEdge[double]("a <-> c", 14.0), c)
        input.addEdge(a, BaseLabeledWeightedEdge[double]("a <-> d", 30.0), d)

        input.addEdge(b, BaseLabeledWeightedEdge[double]("b <-> c", 21.0), c)

        input.addEdge(c, BaseLabeledWeightedEdge[double]("c <-> d", 10.0), d)
        input.addEdge(c, BaseLabeledWeightedEdge[double]("c <-> e", 1.0), e)

        input.addEdge(e, BaseLabeledWeightedEdge[double]("e <-> f", 6.0), f)
        input.addEdge(e, BaseLabeledWeightedEdge[double]("e <-> g", 9.0), g)

        input.addEdge(f, BaseLabeledWeightedEdge[double]("f <-> g", 4.0), g)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[double], double
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[double]())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge[double]("a <-> b", 7.0), b)
        expected.addEdge(a, BaseLabeledWeightedEdge[double]("a <-> c", 14.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge[double]("c <-> d", 10.0), d)
        expected.addEdge(c, BaseLabeledWeightedEdge[double]("c <-> e", 1.0), e)
        expected.addEdge(e, BaseLabeledWeightedEdge[double]("e <-> f", 6.0), f)
        expected.addEdge(f, BaseLabeledWeightedEdge[double]("e <-> g", 9.0), g)

        actual = (
            CommonsGraph.minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge[double]())
            .fromArbitrarySource()
            .applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)

    def testNullVertex(self) -> None:

        pass  # LLM could not translate this method

    def testNullMonoid(self) -> None:
        input: UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ] = None
        a: BaseLabeledVertex = None
        try:
            input = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
            ]()
            a = BaseLabeledVertex("A")
            input.addVertex(a)
        except RuntimeError as e:
            self.fail(e.getMessage())

        CommonsGraph.minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[Double]()
        ).fromSource(a).applyingBoruvkaAlgorithm(None)

    def testNullGraph(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).fromArbitrarySource().applyingBoruvkaAlgorithm(
                DoubleWeightBaseOperations()
            )

    def testNotExistVertex(self) -> None:
        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        with self.assertRaises(RuntimeError):
            minimumSpanningTree(input).whereEdgesHaveWeights(
                BaseWeightedEdge[Double]()
            ).fromSource(BaseLabeledVertex("NOT EXIST"))

    def testEmptyGraph(self) -> None:
        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        CommonsGraph.minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[Double]()
        ).fromArbitrarySource().applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())
