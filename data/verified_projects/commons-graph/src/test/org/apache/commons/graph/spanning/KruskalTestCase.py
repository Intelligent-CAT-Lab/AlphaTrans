import pytest

from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
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



class KruskalTestCase(unittest.TestCase):

    @pytest.mark.test
    def testDisconnectedMinimumSpanningTree(self) -> None:
        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 4.0), b)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 2.0), d)

        expected = MutableSpanningTree(
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 4.0), b)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 2.0), d)

        actual = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .fromArbitrarySource()\
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())

        self.assertEqual(expected, actual)
    
    
    @pytest.mark.test
    def testEmptyGraph(self) -> None:
        with self.assertRaises(RuntimeError):
            input = UndirectedMutableGraph()

            CommonsGraph.minimumSpanningTree(input)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromArbitrarySource()\
                .applyingKruskalAlgorithm(DoubleWeightBaseOperations())

    
    @pytest.mark.test
    def testNotExistVertex(self) -> None:
        with self.assertRaises(RuntimeError):
            input = UndirectedMutableGraph()

            CommonsGraph.minimumSpanningTree(input)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromSource(BaseLabeledVertex("NOT EXIST"))

    
    @pytest.mark.test
    def testNullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            CommonsGraph.minimumSpanningTree(None)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromArbitrarySource()\
                .applyingKruskalAlgorithm(DoubleWeightBaseOperations())

    
    @pytest.mark.test
    def testNullMonoid(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            input = None
            a = None
            try:
                input = UndirectedMutableGraph()
                a = BaseLabeledVertex("A")
                input.addVertex(a)
            except (TypeError, AttributeError) as e:
                self.fail(str(e))
            
            CommonsGraph.minimumSpanningTree(input)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromSource(a)\
                .applyingKruskalAlgorithm(None)

    
    @pytest.mark.test
    def testNullVertex(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            input = UndirectedMutableGraph()
            CommonsGraph.minimumSpanningTree(input)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromSource(None)\
                .applyingKruskalAlgorithm(DoubleWeightBaseOperations())

    
    @pytest.mark.test
    def testP4NonUniformWeightsMinimumSpanningTree(self) -> None:
        input = UndirectedMutableGraph()

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

        expected = MutableSpanningTree(
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 4.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 2.0), d)

        actual = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .fromArbitrarySource()\
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        
        self.assertEqual(expected, actual)

    
    @pytest.mark.test
    def testP4UniformWeightsMinimumSpanningTree(self) -> None:
        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 1.0), b)
        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 1.0), c)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 1.0), d)

        expected = MutableSpanningTree(
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 1.0), b)
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 1.0), c)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 1.0), d)

        actual = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .fromArbitrarySource()\
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())

        self.assertEqual(expected, actual)
    
    
    @pytest.mark.test
    def testVerifyNotConnectedMinimumSpanningTree(self) -> None:
        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)

        expected = MutableSpanningTree(
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)

        actual = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .fromArbitrarySource()\
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())

        self.assertEqual(expected, actual)

    
    @pytest.mark.test
    def testVerifyWikipediaMinimumSpanningTree(self) -> None:
        input = UndirectedMutableGraph()

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

        expected = MutableSpanningTree(
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> d", 5.0), d)
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> e", 9.0), e)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> e", 5.0), e)
        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> f", 6.0), f)
        expected.addEdge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)

        actual = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .fromArbitrarySource()\
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())

        self.assertEqual(expected, actual)
