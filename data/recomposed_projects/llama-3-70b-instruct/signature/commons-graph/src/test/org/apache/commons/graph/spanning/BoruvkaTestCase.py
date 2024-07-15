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

        pass  # LLM could not translate this method

    def testNullVertex(self) -> None:
        input: UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ] = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[Double]]()
        CommonsGraph.minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[Double]()
        ).fromSource(None).applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())

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
        input: UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ] = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[Double]]()
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
