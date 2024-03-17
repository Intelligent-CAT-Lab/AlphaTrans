# Imports Begin
from src.main.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
import typing
from typing import *
# Imports End

class TarjanTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def verifyHasStronglyConnectedComponents(self) -> None:

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
                    lambda: [a, b, c, d, e, f, g, h],
                    lambda: [
                        BaseLabeledEdge("A -> F").from_(a).to(f),
                        BaseLabeledEdge("A -> B").from_(a).to(b),
                        BaseLabeledEdge("B -> D").from_(b).to(d),
                        BaseLabeledEdge("C -> G").from_(c).to(g),
                        BaseLabeledEdge("D -> A").from_(d).to(a),
                        BaseLabeledEdge("D -> G").from_(d).to(g),
                        BaseLabeledEdge("E -> C").from_(e).to(c),
                        BaseLabeledEdge("E -> F").from_(e).to(f),
                        BaseLabeledEdge("F -> E").from_(f).to(e),
                        BaseLabeledEdge("G -> H").from_(g).to(h),
                        BaseLabeledEdge("H -> C").from_(h).to(c),
                    ],
                )
            )
            expected = {
                {a, b, d},
                {e, f},
                {g, h, c},
            }
            actual = self.findStronglyConnectedComponent(graph).applying_tarjan()
            assert not actual.empty()
            assert expected == actual

    def testSparse(self) -> None:

            graph = self.newDirectedMutableGraph(
                GraphConnection(
                    BaseLabeledVertex("A"),
                    BaseLabeledVertex("B"),
                    BaseLabeledVertex("C"),
                    BaseLabeledVertex("D"),
                    BaseLabeledVertex("E"),
                    BaseLabeledVertex("F")
                )
            )
            expected = 6
            actual = self.findStronglyConnectedComponent(graph).applyingTarjan()
            self.assertEqual(len(actual), expected)

    def testNullGraph(self) -> None:

            graph: typing.Any = None
            self.findStronglyConnectedComponent(graph).applyingTarjan()

    def testEmptyGraph(self) -> None:

            graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
            self.findStronglyConnectedComponent(graph).applyingTarjan()

    # Class Methods End


class new AbstractGraphConnection<BaseLabeledVertex,BaseLabeledWeightedEdge<Integer>>(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def connect0(self) -> None:

        self.addVertex(BaseLabeledVertex("A"))
        self.addVertex(BaseLabeledVertex("B"))
        self.addVertex(BaseLabeledVertex("C"))
        self.addVertex(BaseLabeledVertex("D"))
        self.addVertex(BaseLabeledVertex("E"))
        self.addVertex(BaseLabeledVertex("F"))

    def (self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


class new AbstractGraphConnection<BaseLabeledVertex,BaseLabeledEdge>(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
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

    # Class Methods End


