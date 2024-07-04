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


class CheriyanMehlhornGabowTestCase(unittest.TestCase):

    def testVerifyHasStronglyConnectedComponents(self) -> None:

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge]()
            .addVertex(a)
            .addVertex(b)
            .addVertex(c)
            .addVertex(d)
            .addVertex(e)
            .addVertex(f)
            .addVertex(g)
            .addVertex(h)
            .addEdge(BaseLabeledEdge("A -> F"))
            .from_(a)
            .to(f)
            .addEdge(BaseLabeledEdge("A -> B"))
            .from_(a)
            .to(b)
            .addEdge(BaseLabeledEdge("B -> D"))
            .from_(b)
            .to(d)
            .addEdge(BaseLabeledEdge("C -> G"))
            .from_(c)
            .to(g)
            .addEdge(BaseLabeledEdge("D -> A"))
            .from_(d)
            .to(a)
            .addEdge(BaseLabeledEdge("D -> G"))
            .from_(d)
            .to(g)
            .addEdge(BaseLabeledEdge("E -> C"))
            .from_(e)
            .to(c)
            .addEdge(BaseLabeledEdge("E -> F"))
            .from_(e)
            .to(f)
            .addEdge(BaseLabeledEdge("F -> E"))
            .from_(f)
            .to(e)
            .addEdge(BaseLabeledEdge("G -> H"))
            .from_(g)
            .to(h)
            .addEdge(BaseLabeledEdge("H -> C"))
            .from_(h)
            .to(c)
        )

        expected = {frozenset({a, b, d}), frozenset({e, f}), frozenset({g, h, c})}

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingCheriyanMehlhornGabow()

        assert not not actual, "Actual should not be empty"
        self.assertEqual(expected, actual)

    def testSparse(self) -> None:

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection[
                BaseLabeledVertex, BaseLabeledWeightedEdge[int]
            ]().connect0(
                addVertex(BaseLabeledVertex("A")),
                addVertex(BaseLabeledVertex("B")),
                addVertex(BaseLabeledVertex("C")),
                addVertex(BaseLabeledVertex("D")),
                addVertex(BaseLabeledVertex("E")),
                addVertex(BaseLabeledVertex("F")),
            )
        )

        expected = 6

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingCheriyanMehlhornGabow()

        self.assertEqual(len(actual), expected)

    def testNullGraph(self) -> None:

        graph = None

        with pytest.raises(Exception):
            CommonsGraph.findStronglyConnectedComponent(
                graph
            ).applyingCheriyanMehlhornGabow()

    def testEmptyGraph(self) -> None:

        graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()

        CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingCheriyanMehlhornGabow()
