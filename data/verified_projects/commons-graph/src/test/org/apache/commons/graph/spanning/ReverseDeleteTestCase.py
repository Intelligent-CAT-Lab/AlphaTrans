import pytest

from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest



class ReverseDeleteTestCase(unittest.TestCase):

    @pytest.mark.test
    def testEmptyGraph(self) -> None:
        input = UndirectedMutableGraph()

        tree = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        
        self.assertEqual(0, tree.getOrder())
        self.assertEqual(0, tree.getSize())

    
    @pytest.mark.test
    def testNullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            CommonsGraph.minimumSpanningTree(None)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())

    
    @pytest.mark.test
    def testNullMonoid(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            input = None

            CommonsGraph.minimumSpanningTree(input)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .applyingReverseDeleteAlgorithm(None)

    
    @pytest.mark.test
    def testVerifyMinimumSpanningTree(self) -> None:
        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 21.0), c)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)

        expected = MutableSpanningTree(
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)

        actual = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        self.assertEqual(expected, actual)
    
    
    @pytest.mark.test
    def testVerifyNotConnectGraph(self) -> None:
        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)

        expected = MutableSpanningTree(
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        
        actual = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        self.assertEqual(expected, actual)

    
    @pytest.mark.test
    def testVerifyNotConnectGraph2(self) -> None:
        input = UndirectedMutableGraph()

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

        expected = MutableSpanningTree(
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)

        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 4.0), e)

        actual = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        self.assertEqual(expected, actual)

    
    @pytest.mark.test
    def testVerifyNotConnectGraph3(self) -> None:
        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)
        input.addVertex(e)
        input.addVertex(f)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 21.0), c)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)

        input.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 7.0), e)
        input.addEdge(e, BaseLabeledWeightedEdge("e <-> f", 21.0), f)
        input.addEdge(f, BaseLabeledWeightedEdge("f <-> d", 4.0), d)

        expected = MutableSpanningTree(
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        for vertex in input.getVertices0():
            expected.addVertex(vertex)

        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> a", 4.0), a)

        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 4.0), e)
        expected.addEdge(f, BaseLabeledWeightedEdge("f <-> d", 4.0), d)

        actual = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .applyingReverseDeleteAlgorithm(DoubleWeightBaseOperations())
        self.assertEqual(expected, actual)
