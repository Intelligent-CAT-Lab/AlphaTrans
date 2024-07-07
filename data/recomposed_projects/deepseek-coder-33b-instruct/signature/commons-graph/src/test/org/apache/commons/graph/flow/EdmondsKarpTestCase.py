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
                lambda: None,
                lambda v: v,
                lambda e: e,
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
                    BaseLabeledWeightedEdge("A -> B", 3).from_(a).to(b),
                    BaseLabeledWeightedEdge("B -> C", 4).from_(b).to(c),
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

        with pytest.raises(RuntimeError):
            CommonsGraph.findMaxFlow(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a).to(g).applyingEdmondsKarp(IntegerWeightBaseOperations())

    def testFindMaxFlowAndVerify(self) -> None:

        pass  # LLM could not translate this method
