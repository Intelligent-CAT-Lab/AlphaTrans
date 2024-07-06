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

        pass  # LLM could not translate this method

    def testVerifyNotConnectedMinimumSpanningTree(self) -> None:

        pass  # LLM could not translate this method

    @pytest.mark.skip(reason="Ignore")
    def testP4UniformWeightsMinimumSpanningTree(self) -> None:

        pass  # LLM could not translate this method

    def testP4NonUniformWeightsMinimumSpanningTree(self) -> None:

        pass  # LLM could not translate this method

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
        ).fromSource(a).applyingKruskalAlgorithm(None)

    def testNullGraph(self) -> None:
        with self.assertRaises(RuntimeError):
            CommonsGraph.minimumSpanningTree(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).fromArbitrarySource().applyingKruskalAlgorithm(
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
        ).fromArbitrarySource().applyingKruskalAlgorithm(DoubleWeightBaseOperations())

    def testDisconnectedMinimumSpanningTree(self) -> None:
        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[double]
        ]()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)

        input.addEdge(a, BaseLabeledWeightedEdge[double]("a <-> b", 4.0), b)
        input.addEdge(c, BaseLabeledWeightedEdge[double]("c <-> d", 2.0), d)

        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[double], double
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[double]())

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge[double]("a <-> b", 4.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge[double]("c <-> d", 2.0), d)

        actual = (
            minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge[double]())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        self.assertEqual(expected, actual)
