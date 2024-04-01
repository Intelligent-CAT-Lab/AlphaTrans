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


class KruskalTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testVerifyWikipediaMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        input.add_vertex(a)
        input.add_vertex(b)
        input.add_vertex(c)
        input.add_vertex(d)
        input.add_vertex(e)
        input.add_vertex(f)
        input.add_vertex(g)
        input.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input.add_edge(a, BaseLabeledWeightedEdge("a <-> d", 5.0), d)
        input.add_edge(b, BaseLabeledWeightedEdge("b <-> c", 8.0), c)
        input.add_edge(b, BaseLabeledWeightedEdge("b <-> d", 9.0), d)
        input.add_edge(b, BaseLabeledWeightedEdge("b <-> e", 7.0), e)
        input.add_edge(c, BaseLabeledWeightedEdge("c <-> e", 5.0), e)
        input.add_edge(d, BaseLabeledWeightedEdge("d <-> e", 15.0), e)
        input.add_edge(d, BaseLabeledWeightedEdge("d <-> f", 6.0), f)
        input.add_edge(e, BaseLabeledWeightedEdge("e <-> f", 8.0), f)
        input.add_edge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)
        input.add_edge(f, BaseLabeledWeightedEdge("f <-> g", 11.0), g)
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double], Double
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[Double]())
        for vertex in input.get_vertices0():
            expected.add_vertex(vertex)
        expected.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.add_edge(a, BaseLabeledWeightedEdge("a <-> d", 5.0), d)
        expected.add_edge(b, BaseLabeledWeightedEdge("b <-> e", 9.0), e)
        expected.add_edge(c, BaseLabeledWeightedEdge("c <-> e", 5.0), e)
        expected.add_edge(d, BaseLabeledWeightedEdge("d <-> f", 6.0), f)
        expected.add_edge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)
        actual = minimumSpanningTree(input).where_edges

    def testVerifyNotConnectedMinimumSpanningTree(self) -> None:

        pass  # LLM could not translate method body

    def testP4UniformWeightsMinimumSpanningTree(self) -> None:

        pass  # LLM could not translate method body

    def testP4NonUniformWeightsMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)
        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 4.0), b)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 2.0), d)
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double], Double
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[Double]())
        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 4.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 2.0), d)
        actual = (
            minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge[Double]())
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )
        self.assertEqual(expected, actual)

    def testNullVertex(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[Double]()
        ).fromSource(None).applyingKruskalAlgorithm(DoubleWeightBaseOperations())

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
        ).fromSource(a).applyingKruskalAlgorithm(None)

    def testNullGraph(self) -> None:

        self.minimumSpanningTree(None).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).fromArbitrarySource().applyingKruskalAlgorithm(DoubleWeightBaseOperations())

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
        ).fromArbitrarySource().applyingKruskalAlgorithm(DoubleWeightBaseOperations())

    def testDisconnectedMinimumSpanningTree(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
