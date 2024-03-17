# Imports Begin
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest

# Imports End


class PrimTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testVerifyWikipediaMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)
        input.addVertex(e)
        input.addVertex(f)
        input.addVertex(g)
        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input.addEdge(a, BaseLabeledWeightedEdge("a <-> d", 5.0), d)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 8.0), c)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> d", 9.0), d)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> e", 7.0), e)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> e", 5.0), e)
        input.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 15.0), e)
        input.addEdge(d, BaseLabeledWeightedEdge("d <-> f", 6.0), f)
        input.addEdge(e, BaseLabeledWeightedEdge("e <-> f", 8.0), f)
        input.addEdge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)
        input.addEdge(f, BaseLabeledWeightedEdge("f <-> g", 11.0), g)
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ]()
        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> d", 5.0), d)
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> e", 7.0), e)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> e", 5.0), e)
        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> f", 6.0), f)
        expected.addEdge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)
        self.__internalPrimAssertion(input, d, expected)

    def testVerifyMinimumSpanningTree2(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")
        g = BaseLabeledVertex("g")
        input.add_vertex(a)
        input.add_vertex(b)
        input.add_vertex(c)
        input.add_vertex(d)
        input.add_vertex(e)
        input.add_vertex(f)
        input.add_vertex(g)
        input.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input.add_edge(a, BaseLabeledWeightedEdge("a <-> c", 14.0), c)
        input.add_edge(a, BaseLabeledWeightedEdge("a <-> d", 30.0), d)
        input.add_edge(b, BaseLabeledWeightedEdge("b <-> c", 21.0), c)
        input.add_edge(c, BaseLabeledWeightedEdge("c <-> d", 10.0), d)
        input.add_edge(c, BaseLabeledWeightedEdge("c <-> e", 1.0), e)
        input.add_edge(e, BaseLabeledWeightedEdge("e <-> f", 6.0), f)
        input.add_edge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)
        input.add_edge(f, BaseLabeledWeightedEdge("f <-> g", 4.0), g)
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ]()
        for vertex in input.get_vertices0():
            expected.add_vertex(vertex)
        expected.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.add_edge(a, BaseLabeledWeightedEdge("a <-> c", 14.0), c)
        expected.add_edge(c, BaseLabeledWeightedEdge("c <-> d", 10.0), d)
        expected.add_edge(c, BaseLabeledWeightedEdge("c <-> e", 1.0), e)
        expected.add_edge(e, BaseLabeledWeightedEdge("e <-> f", 6.0), f)
        expected.add_edge(f, BaseLabeledWeightedEdge("f <-> g", 4.0), g)
        self.__internalPrimAssertion(input, a, expected)

    def testNullVertex(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[Double]()
        ).fromSource(None).applyingPrimAlgorithm(DoubleWeightBaseOperations())

    def testNullMonoid(self) -> None:

        input: UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ] = None
        a: BaseLabeledVertex = None
        try:
            input = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
            ]()
            a = BaseLabeledVertex("A")
            input.addVertex(a)
        except NullPointerException as e:
            self.fail(e.getMessage())
        minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[Double]()
        ).fromSource(a).applyingBoruvkaAlgorithm(None)

    def testNullGraph(self) -> None:

        self.minimumSpanningTree(None).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).fromArbitrarySource().applyingPrimAlgorithm(DoubleWeightBaseOperations())

    def testNotExistVertex(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[Double]()
        ).fromSource(BaseLabeledVertex("NOT EXIST"))

    def testEmptyGraph(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[Double]()
        ).fromArbitrarySource().applyingPrimAlgorithm(DoubleWeightBaseOperations())

    @staticmethod
    def __internalPrimAssertion(
        input: UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float]
        ],
        source: BaseLabeledVertex,
        expected: MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ],
    ) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
