# Imports Begin
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
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


class ReverseDeleteTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testVerifyNotConnectGraph3(self) -> None:

        pass  # LLM could not translate method body

    def testVerifyNotConnectGraph2(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)
        input.addVertex(e)
        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 21.0), c)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)
        input.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 4.0), e)
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double], Double
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[Double]())
        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)
        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 4.0), e)
        actual = (
            minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge[Double]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )
        self.assertEqual(expected, actual)

    def testVerifyNotConnectGraph(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double], Double
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[Double]())
        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        actual = (
            minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge[Double]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )
        self.assertEqual(expected, actual)

    def testVerifyMinimumSpanningTree(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 21.0), c)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)
        expected = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double], Double
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[Double]())
        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)
        actual = (
            minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge[Double]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )
        self.assertEqual(expected, actual)

    def testNullMonoid(self) -> None:

        input = None
        minimumSpanningTree(input).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).applyingReverseDeleteAlgorithm(None)

    def testNullGraph(self) -> None:

        self.minimumSpanningTree(None).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())

    def testEmptyGraph(self) -> None:

        input = UndirectedMutableGraph[
            BaseLabeledVertex, BaseLabeledWeightedEdge[Double]
        ]()
        tree = (
            minimumSpanningTree(input)
            .whereEdgesHaveWeights(BaseWeightedEdge[Double]())
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        )
        self.assertEqual(0, tree.getOrder())
        self.assertEqual(0, tree.getSize())

    # Class Methods End
