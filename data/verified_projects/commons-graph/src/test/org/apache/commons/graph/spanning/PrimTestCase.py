# Imports Begin
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

# Imports End


class PrimTestCase(unittest.TestCase):

    @staticmethod
    def __internalPrimAssertion(input, source, expected) -> None:
        actual = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .fromSource(source)\
            .applyingPrimAlgorithm(DoubleWeightBaseOperations())

        PrimTestCase.assertEquals(expected, actual)
    
    
    def test_EmptyGraph(self) -> None:
        with self.assertRaises(RuntimeError):
            input = UndirectedMutableGraph()

            CommonsGraph.minimumSpanningTree(input)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromArbitrarySource()\
                .applyingPrimAlgorithm(DoubleWeightBaseOperations())

    
    def test_NotExistVertex(self) -> None:
        with self.assertRaises(RuntimeError):
            input = UndirectedMutableGraph()

            CommonsGraph.minimumSpanningTree(input)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromSource(BaseLabeledVertex("NOT EXIST"))
    

    def test_NullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            CommonsGraph.minimumSpanningTree(None)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromArbitrarySource()\
                .applyingPrimAlgorithm(DoubleWeightBaseOperations())

    
    def test_NullMonoid(self) -> None:
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
                .applyingBoruvkaAlgorithm(None)
    

    def test_NullVertex(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            input = UndirectedMutableGraph()

            CommonsGraph.minimumSpanningTree(input)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromSource(None)\
                .applyingPrimAlgorithm(DoubleWeightBaseOperations())

    
    def test_VerifyMinimumSpanningTree2(self) -> None:
        input = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        f = BaseLabeledVertex("f")
        g = BaseLabeledVertex("g")

        input.addVertex(a)
        input.addVertex(b)
        input.addVertex(c)
        input.addVertex(d)
        input.addVertex(e)
        input.addVertex(f)
        input.addVertex(g)

        input.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        input.addEdge(a, BaseLabeledWeightedEdge("a <-> c", 14.0), c)
        input.addEdge(a, BaseLabeledWeightedEdge("a <-> d", 30.0), d)

        input.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 21.0), c)

        input.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 10.0), d)
        input.addEdge(c, BaseLabeledWeightedEdge("c <-> e", 1.0), e)

        input.addEdge(e, BaseLabeledWeightedEdge("e <-> f", 6.0), f)
        input.addEdge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)

        input.addEdge(f, BaseLabeledWeightedEdge("f <-> g", 4.0), g)

        expected = MutableSpanningTree(
            DoubleWeightBaseOperations(),
            BaseWeightedEdge()
        )

        for vertex in input.getVertices0():
            expected.addVertex(vertex)
        
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 7.0), b)
        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> c", 14.0), c)

        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> d", 10.0), d)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> e", 1.0), e)

        expected.addEdge(e, BaseLabeledWeightedEdge("e <-> f", 6.0), f)

        expected.addEdge(f, BaseLabeledWeightedEdge("f <-> g", 4.0), g)

        PrimTestCase.__internalPrimAssertion(input, a, expected)

    
    def test_VerifyWikipediaMinimumSpanningTree(self) -> None:
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
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> e", 7.0), e)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> e", 5.0), e)
        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> f", 6.0), f)
        expected.addEdge(e, BaseLabeledWeightedEdge("e <-> g", 9.0), g)

        PrimTestCase.__internalPrimAssertion(input, d, expected)
