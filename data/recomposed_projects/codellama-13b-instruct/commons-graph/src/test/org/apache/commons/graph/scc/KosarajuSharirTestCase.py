# Imports Begin
from src.main.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import os
import typing
from typing import *
# Imports End

class KosarajuSharirTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testVerifyHasStronglyConnectedComponents(self) -> None:

            a = BaseLabeledVertex("A")
            b = BaseLabeledVertex("B")
            c = BaseLabeledVertex("C")
            d = BaseLabeledVertex("D")
            e = BaseLabeledVertex("E")
            f = BaseLabeledVertex("F")
            g = BaseLabeledVertex("G")
            h = BaseLabeledVertex("H")
            graph = self.newDirectedMutableGraph(
                GraphConnection(
                    [a, b, c, d, e, f, g, h],
                    [
                        BaseLabeledEdge("A -> F", a, f),
                        BaseLabeledEdge("A -> B", a, b),
                        BaseLabeledEdge("B -> D", b, d),
                        BaseLabeledEdge("C -> G", c, g),
                        BaseLabeledEdge("D -> A", d, a),
                        BaseLabeledEdge("D -> G", d, g),
                        BaseLabeledEdge("E -> C", e, c),
                        BaseLabeledEdge("E -> F", e, f),
                        BaseLabeledEdge("F -> E", f, e),
                        BaseLabeledEdge("G -> H", g, h),
                        BaseLabeledEdge("H -> C", h, c),
                    ],
                )
            )
            expected = {
                {a, b, d},
                {e, f},
                {g, h, c},
            }
            actual = self.findStronglyConnectedComponent(graph).applyingKosarajuSharir0()
            self.assertFalse(actual.empty())
            self.assertEqual(expected, actual)
            actual_a = self.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a)
            self.assertFalse(actual_a.empty())
            self.assertEqual({a, b, d}, actual_a)
            actual_e = self.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e)
            self.assertFalse(actual_e.empty())
            self.assertEqual({e, f}, actual_e)
            actual_g = self.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(g)
            self.assertFalse(actual_g.empty())
            self.assertEqual({g, h, c}, actual_g)

    def testUnconnectedGraph(self) -> None:

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")
        graph = self.newDirectedMutableGraph(
            GraphConnection(
                [a, b, c, d, e, f, g, h],
                [
                    BaseLabeledEdge("A -> B"),
                    BaseLabeledEdge("B -> D"),
                    BaseLabeledEdge("C -> G"),
                    BaseLabeledEdge("D -> A"),
                    BaseLabeledEdge("E -> C"),
                    BaseLabeledEdge("E -> F"),
                    BaseLabeledEdge("F -> E"),
                    BaseLabeledEdge("G -> H"),
                    BaseLabeledEdge("H -> C"),
                ],
            )
        )
        expected = {
            {a, b, d},
            {e, f},
            {g, h, c},
        }
        actual = self.findStronglyConnectedComponent(graph).applyingKosarajuSharir0()
        self.assertFalse(actual.empty())
        self.assertEqual(expected, actual)
        actual_a = self.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a)
        self.assertFalse(actual_a.empty())
        self.assertEqual({a, b, d}, actual_a)
        actual_e = self.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(e)
        self.assertFalse(actual_e.empty())
        self.assertEqual({e, f}, actual_e)
        actual_g = self.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(g)
        self.assertFalse(actual_g.empty())
        self.assertEqual({g, h, c}, actual_g)

    def testNullVertices(self) -> None:

            a = None
            graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[Integer]]()
            self.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(a)

    def testNullGraph(self) -> None:

            graph: typing.Any = None
            self.findStronglyConnectedComponent(graph).applyingKosarajuSharir0()

    def testNotExistVertex(self) -> None:

            graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[Integer]]()
            self.findStronglyConnectedComponent(graph).applyingKosarajuSharir1(BaseLabeledVertex("NOT EXISTS"))

    # Class Methods End


class new AbstractGraphConnection<BaseLabeledVertex,BaseLabeledEdge>(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def connect0(self) -> None:

        self.addVertex(a)
        self.addVertex(b)
        self.addVertex(c)
        self.addVertex(d)
        self.addVertex(e)
        self.addVertex(f)
        self.addVertex(g)
        self.addVertex(h)
        self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
        self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
        self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
        self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
        self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
        self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
        self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
        self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
        self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

    def connect0(self) -> None:

        self.add_vertex(a)
        self.add_vertex(b)
        self.add_vertex(c)
        self.add_vertex(d)
        self.add_vertex(e)
        self.add_vertex(f)
        self.add_vertex(g)
        self.add_vertex(h)
        self.add_edge(BaseLabeledEdge("A -> F")).from_(a).to(f)
        self.add_edge(BaseLabeledEdge("A -> B")).from_(a).to(b)
        self.add_edge(BaseLabeledEdge("B -> D")).from_(b).to(d)
        self.add_edge(BaseLabeledEdge("C -> G")).from_(c).to(g)
        self.add_edge(BaseLabeledEdge("D -> A")).from_(d).to(a)
        self.add_edge(BaseLabeledEdge("D -> G")).from_(d).to(g)
        self.add_edge(BaseLabeledEdge("E -> C")).from_(e).to(c)
        self.add_edge(BaseLabeledEdge("E -> F")).from_(e).to(f)
        self.add_edge(BaseLabeledEdge("F -> E")).from_(f).to(e)
        self.add_edge(BaseLabeledEdge("G -> H")).from_(g).to(h)
        self.add_edge(BaseLabeledEdge("H -> C")).from_(h).to(c)

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


