from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *


class TarjanTestCase(unittest.TestCase):

    @pytest.mark.skip(reason="Ignore")
    def verifyHasStronglyConnectedComponents(self) -> None:

        pass  # LLM could not translate this method

    def testSparse(self) -> None:
        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection[
                BaseLabeledVertex, BaseLabeledWeightedEdge[int]
            ]().connect0(
                lambda: [
                    graph.addVertex(BaseLabeledVertex("A")),
                    graph.addVertex(BaseLabeledVertex("B")),
                    graph.addVertex(BaseLabeledVertex("C")),
                    graph.addVertex(BaseLabeledVertex("D")),
                    graph.addVertex(BaseLabeledVertex("E")),
                    graph.addVertex(BaseLabeledVertex("F")),
                ]
            )
        )

        expected = 6

        actual = CommonsGraph.findStronglyConnectedComponent(graph).applyingTarjan()

        self.assertEqual(actual.size(), expected)

    def testNullGraph(self) -> None:
        graph = None
        CommonsGraph.findStronglyConnectedComponent(graph).applyingTarjan()

    def testEmptyGraph(self) -> None:
        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
        CommonsGraph.findStronglyConnectedComponent(graph).applyingTarjan()
