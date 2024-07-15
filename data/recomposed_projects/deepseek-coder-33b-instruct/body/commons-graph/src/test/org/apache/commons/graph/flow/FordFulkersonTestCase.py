from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.flow.FlowWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.flow.FromHeadBuilder import *
from src.main.org.apache.commons.graph.flow.MaxFlowAlgorithmSelector import *
from src.main.org.apache.commons.graph.flow.ToTailBuilder import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *


class FordFulkersonTestCase(unittest.TestCase):

    def testNullVertices(self) -> None:

        graph = DirectedMutableGraph()

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None).to_(None).applyingFordFulkerson(IntegerWeightBaseOperations())

    def testNullGraphAndVertices(self) -> None:

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None).to(None).applyingFordFulkerson(IntegerWeightBaseOperations())

    def testNullGraph(self) -> None:

        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        try:
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a).to(d).applyingFordFulkerson(IntegerWeightBaseOperations())
        except RuntimeError:
            pass

    def testNotConnected_2(self) -> None:

        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: None,
                lambda: [a, BaseLabeledVertex("B"), BaseLabeledVertex("C"), d],
                lambda: [
                    BaseLabeledWeightedEdge("A -> B", 1000)
                    .from_(a)
                    .to(BaseLabeledVertex("B"))
                ],
            )
        )

        expected = 0

        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(d)
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        )

        self.assertEqual(actual, expected)

    def testNotConnected(self) -> None:

        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        graph = CommonsGraph.newDirectedMutableGraph(
            GraphConnection()
            .addVertex(a)
            .addVertex(BaseLabeledVertex("B"))
            .addVertex(BaseLabeledVertex("C"))
            .addVertex(d)
        )

        expected = 0

        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(d)
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        )

        self.assertEqual(actual, expected)

    def testFindMaxFlowAndVerify(self) -> None:

        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    a,
                    BaseLabeledVertex("B"),
                    BaseLabeledVertex("C"),
                    d,
                    BaseLabeledWeightedEdge("A -> B", 1000).from_(a).to(b),
                    BaseLabeledWeightedEdge("A -> C", 1000).from_(a).to(c),
                    BaseLabeledWeightedEdge("B -> C", 1).from_(b).to(c),
                    BaseLabeledWeightedEdge("B -> D", 1000).from_(b).to(d),
                    BaseLabeledWeightedEdge("C -> D", 1000).from_(c).to(d),
                ]
            )
        )

        expected = 2000

        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(d)
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        )

        self.assertEqual(expected, actual)
