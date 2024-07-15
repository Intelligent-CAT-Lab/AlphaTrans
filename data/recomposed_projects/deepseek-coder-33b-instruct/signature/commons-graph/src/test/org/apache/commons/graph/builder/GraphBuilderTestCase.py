from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class GraphBuilderTestCase(unittest.TestCase):

    def testVerifyProducedGraphesAreEquals(self) -> None:

        expected = UndirectedMutableGraph()

        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        expected.addVertex(start)
        expected.addVertex(a)
        expected.addVertex(b)
        expected.addVertex(c)
        expected.addVertex(d)
        expected.addVertex(e)
        expected.addVertex(goal)

        expected.addEdge(start, BaseLabeledWeightedEdge("start <-> a", 1.5), a)
        expected.addEdge(start, BaseLabeledWeightedEdge("start <-> d", 2), d)

        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 2), b)
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3), c)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> goal", 3), goal)

        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 3), e)
        expected.addEdge(e, BaseLabeledWeightedEdge("e <-> goal", 2), goal)

        actual = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    HeadVertexConnector(start)
                    .addEdge(BaseLabeledWeightedEdge("start <-> a", 1.5))
                    .to(a)
                    .addEdge(BaseLabeledWeightedEdge("start <-> d", 2))
                    .to(d),
                    HeadVertexConnector(a)
                    .addEdge(BaseLabeledWeightedEdge("a <-> b", 2))
                    .to(b),
                    HeadVertexConnector(b)
                    .addEdge(BaseLabeledWeightedEdge("b <-> c", 3))
                    .to(c),
                    HeadVertexConnector(c)
                    .addEdge(BaseLabeledWeightedEdge("c <-> goal", 3))
                    .to(goal),
                    HeadVertexConnector(d)
                    .addEdge(BaseLabeledWeightedEdge("d <-> e", 3))
                    .to(e),
                    HeadVertexConnector(e)
                    .addEdge(BaseLabeledWeightedEdge("e <-> goal", 2))
                    .to(goal),
                ]
            )
        )

        self.assertEqual(expected, actual)
