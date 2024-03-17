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

class CheriyanMehlhornGabowTestCase(unittest.TestCase):

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
            graph = newDirectedMutableGraph(
                GraphConnection(
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
            expected = {
                {a, b, d},
                {e, f},
                {g, h, c},
            }
            actual = findStronglyConnectedComponent(graph).applyingCheriyanMehlhornGabow()
            self.assertFalse(actual.isEmpty())
            self.assertEqual(expected, actual)

    def testSparse(self) -> None:

            graph = self.newDirectedMutableGraph(
                GraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[int]]()
            )
            graph.connect0()
            expected = 6
            actual = self.findStronglyConnectedComponent(graph).applyingCheriyanMehlhornGabow()
            self.assertEqual(len(actual), expected)

    def testNullGraph(self) -> None:

            graph: typing.Any = None
            self.findStronglyConnectedComponent(graph).applyingCheriyanMehlhornGabow()

    def testEmptyGraph(self) -> None:

            graph = DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[Integer]]()
            self.findStronglyConnectedComponent(graph).applyingCheriyanMehlhornGabow()

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

        self.addVertex(a)
        self.addVertex(b)
        self.addVertex(c)
        self.addVertex(d)
        self.addVertex(e)
        self.addVertex(f)
        self.addVertex(g)
        self.addVertex(h)
        self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
        self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
        self.addEdge(BaseLabeledEdge("B -> D")).from_(b).to(d)
        self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
        self.addEdge(BaseLabeledEdge("D -> A")).from_(d).to(a)
        self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
        self.addEdge(BaseLabeledEdge("E -> C")).from_(e).to(c)
        self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
        self.addEdge(BaseLabeledEdge("F -> E")).from_(f).to(e)
        self.addEdge(BaseLabeledEdge("G -> H")).from_(g).to(h)
        self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

    def (self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


