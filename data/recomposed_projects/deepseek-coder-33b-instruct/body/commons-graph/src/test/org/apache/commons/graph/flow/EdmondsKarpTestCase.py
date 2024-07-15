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


class EdmondsKarpTestCase(unittest.TestCase):

    def testSparse(self) -> None:

        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    a,
                    BaseLabeledVertex("B"),
                    BaseLabeledVertex("C"),
                    BaseLabeledVertex("D"),
                    BaseLabeledVertex("E"),
                    BaseLabeledVertex("F"),
                    g,
                ],
                lambda: [
                    (a, BaseLabeledVertex("B"), BaseLabeledEdge("A -> B", 3)),
                    (
                        BaseLabeledVertex("B"),
                        BaseLabeledVertex("C"),
                        BaseLabeledEdge("B -> C", 4),
                    ),
                ],
            )
        )

        expected = 0

        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(g)
            .applyingEdmondsKarp(IntegerWeightBaseOperations())
        )

        self.assertEqual(actual, expected)

    def testNullVertices(self) -> None:

        a = None
        g = None

        graph = DirectedMutableGraph()

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a).to(g).applyingEdmondsKarp(IntegerWeightBaseOperations())

    def testNullGraph(self) -> None:

        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        try:
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a).to(g).applyingEdmondsKarp(IntegerWeightBaseOperations())
        except Exception as e:
            self.assertEqual(str(e), "Max flow can not be calculated on null graph")

    def testFindMaxFlowAndVerify(self) -> None:

        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    a,
                    BaseLabeledVertex("B"),
                    BaseLabeledVertex("C"),
                    BaseLabeledVertex("D"),
                    BaseLabeledVertex("E"),
                    BaseLabeledVertex("F"),
                    g,
                ],
                lambda: [
                    BaseLabeledWeightedEdge("A -> B", 3).from_(a).to(1),
                    BaseLabeledWeightedEdge("A -> D", 3).from_(a).to(3),
                    BaseLabeledWeightedEdge("B -> C", 4).from_(1).to(2),
                    BaseLabeledWeightedEdge("C -> A", 3).from_(2).to(0),
                    BaseLabeledWeightedEdge("C -> D", 1).from_(2).to(3),
                    BaseLabeledWeightedEdge("C -> E", 2).from_(2).to(4),
                    BaseLabeledWeightedEdge("D -> E", 2).from_(3).to(4),
                    BaseLabeledWeightedEdge("D -> F", 6).from_(3).to(5),
                    BaseLabeledWeightedEdge("E -> B", 1).from_(4).to(1),
                    BaseLabeledWeightedEdge("E -> G", 1).from_(4).to(6),
                    BaseLabeledWeightedEdge("F -> G", 9).from_(5).to(6),
                ],
            )
        )

        expected = 5

        actual = (
            CommonsGraph.findMaxFlow(graph)
            .whereEdgesHaveWeights(BaseWeightedEdge())
            .from_(a)
            .to(g)
            .applyingEdmondsKarp(IntegerWeightBaseOperations())
        )

        self.assertEqual(expected, actual)
