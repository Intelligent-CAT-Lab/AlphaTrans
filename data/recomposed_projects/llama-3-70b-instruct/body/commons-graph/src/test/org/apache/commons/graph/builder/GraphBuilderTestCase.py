from __future__ import annotations
import re
import typing
from typing import *
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
        expected = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[typing.Any]
        ]()

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

        expected.addEdge(
            start, BaseLabeledWeightedEdge[typing.Any]("start <-> a", 1.5), a
        )
        expected.addEdge(
            start, BaseLabeledWeightedEdge[typing.Any]("start <-> d", 2), d
        )

        expected.addEdge(a, BaseLabeledWeightedEdge[typing.Any]("a <-> b", 2), b)
        expected.addEdge(b, BaseLabeledWeightedEdge[typing.Any]("b <-> c", 3), c)
        expected.addEdge(c, BaseLabeledWeightedEdge[typing.Any]("c <-> goal", 3), goal)

        expected.addEdge(d, BaseLabeledWeightedEdge[typing.Any]("d <-> e", 3), e)
        expected.addEdge(e, BaseLabeledWeightedEdge[typing.Any]("e <-> goal", 2), goal)

        actual = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[
                BaseLabeledVertex, BaseLabeledWeightedEdge[typing.Any]
            ](lambda: None)
        )

        self.assertEqual(expected, actual)
