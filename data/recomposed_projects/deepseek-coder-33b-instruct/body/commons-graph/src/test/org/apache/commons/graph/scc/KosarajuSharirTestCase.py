from __future__ import annotations
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *


class KosarajuSharirTestCase(unittest.TestCase):

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
            AbstractGraphConnection(
                lambda: [
                    addVertex(a),
                    addVertex(b),
                    addVertex(c),
                    addVertex(d),
                    addVertex(e),
                    addVertex(f),
                    addVertex(g),
                    addVertex(h),
                    addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f),
                    addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b),
                    addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d),
                    addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g),
                    addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a),
                    addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g),
                    addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c),
                    addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f),
                    addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e),
                    addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h),
                    addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c),
                ]
            )
        )

        expected = {frozenset({a, b, d}), frozenset({e, f}), frozenset({g, h, c})}

        actual = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir0()

        self.assertTrue(bool(actual))
        self.assertEqual(expected, actual)

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)

        self.assertTrue(bool(actualA))
        self.assertEqual(frozenset({a, b, d}), actualA)

        actualE = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)

        self.assertTrue(bool(actualE))
        self.assertEqual(frozenset({e, f}), actualE)

        actualG = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(g)

        self.assertTrue(bool(actualG))
        self.assertEqual(frozenset({g, h, c}), actualG)

    def testUnconnectedGraph(self) -> None:

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection()
            .addVertex(a)
            .addVertex(b)
            .addVertex(c)
            .addVertex(d)
            .addVertex(e)
            .addVertex(f)
            .addVertex(g)
            .addVertex(h)
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
        ).applyingKosarajuSharir0()

        self.assertFalse(not actual)
        self.assertEqual(expected, actual)

        actualA = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(a)

        self.assertFalse(not actualA)
        self.assertEqual(frozenset({a, b, d}), actualA)

        actualE = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(e)

        self.assertFalse(not actualE)
        self.assertEqual(frozenset({e, f}), actualE)

        actualG = CommonsGraph.findStronglyConnectedComponent(
            graph
        ).applyingKosarajuSharir1(g)

        self.assertFalse(not actualG)
        self.assertEqual(frozenset({g, h, c}), actualG)

    def testNullVertices(self) -> None:

        a = None
        graph = DirectedMutableGraph()

        with pytest.raises(RuntimeError):
            CommonsGraph.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(
                a
            )

    def testNullGraph(self) -> None:

        graph = None
        with pytest.raises(Exception):
            CommonsGraph.findStronglyConnectedComponent(graph).applyingKosarajuSharir0()

    def testNotExistVertex(self) -> None:

        graph = DirectedMutableGraph()

        with pytest.raises(RuntimeError):
            CommonsGraph.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(
                BaseLabeledVertex("NOT EXISTS")
            )
