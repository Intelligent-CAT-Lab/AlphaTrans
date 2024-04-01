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


class BoruvkaTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def verifySparseGraphMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        input.addVertex(BaseLabeledVertex("A"))
        input.addVertex(BaseLabeledVertex("B"))
        input.addVertex(BaseLabeledVertex("C"))
        input.addVertex(BaseLabeledVertex("D"))
        input.addVertex(BaseLabeledVertex("E"))
        input.addVertex(BaseLabeledVertex("F"))
        input.addVertex(BaseLabeledVertex("G"))
        minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[Double]()
        ).fromArbitrarySource().applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())

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
        input.add_edge(a, BaseLabeledWeightedEdge("a <-> c", 14.0), c)
        input.add_edge(a, BaseLabeledWeightedEdge("a <-> d", 30.0), d)
        input.add_edge(b, BaseLabeledWeightedEdge("b <-> c", 21.0), c)
        input.add_edge(c, BaseLabeledWeightedEdge("c <-> d", 10.0), d)
        input.add_edge(c, BaseLabeledWeightedEdge("c <-> e", 1.0), e)
        input.add_edge(e, BaseLabeledWeightedEdge("e <-> f", 6.0), f)
        input.add_edge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)
        input.add_edge(f, BaseLabeledWeightedEdge("f <-> g", 4.0), g)
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double], Double
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[Double]())
        for vertex in input.get_vertices0():
            expected.add_vertex(vertex)
        expected.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.add_edge(a, BaseLabeledWeightedEdge("a <-> c", 14.0), c)
        expected.add_edge(c, BaseLabeledWeightedEdge("c <-> d", 10.0), d)
        expected.add_edge(c, BaseLabeledWeightedEdge("c <-> e", 1.0), e)
        expected.add_edge(e, BaseLabeledWeightedEdge("e <-> f", 6.0), f)
        expected.add_edge(f, BaseLabeledWeightedEdge("e <-> g", 9.0), g)
        actual = (
            minimumSpanningTree(input)
            .where_edges_have_weights(BaseWeightedEdge[Double]())
            .from_arbitrary_source()
            .applying_boruvka_algorithm(DoubleWeightBaseOperations())
        )
        self.assertEqual(expected, actual)

    def testNullVertex(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[Double]()
        ).fromSource(None).applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())

    def testNullMonoid(self) -> None:

        input: typing.Optional[
            UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
        ] = None
        a: typing.Optional[BaseLabeledVertex] = None
        try:
            input = UndirectedMutableGraph[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float]
            ]()
            a = BaseLabeledVertex("A")
            input.addVertex(a)
        except NullPointerException as e:
            self.fail(e.getMessage())
        minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge[float]()
        ).fromSource(a).applyingBoruvkaAlgorithm(None)

    def testNullGraph(self) -> None:

        self.minimumSpanningTree(None).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).fromArbitrarySource().applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())

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
        ).fromArbitrarySource().applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())

    # Class Methods End
