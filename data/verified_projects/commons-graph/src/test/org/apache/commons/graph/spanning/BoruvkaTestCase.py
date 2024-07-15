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


class BoruvkaTestCase(unittest.TestCase):

    @pytest.mark.test
    def testEmptyGraph(self) -> None:
        with self.assertRaises(RuntimeError):
            input = UndirectedMutableGraph()

            CommonsGraph.minimumSpanningTree(input)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromArbitrarySource()\
                .applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())

    
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
                .applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())
    
    
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
                .applyingBoruvkaAlgorithm(None)

    
    @pytest.mark.test
    def testNullVertex(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            input = UndirectedMutableGraph()
            CommonsGraph.minimumSpanningTree(input)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromSource(None)\
                .applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())

    
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
        expected.addEdge(f, BaseLabeledWeightedEdge("e <-> g", 9.0), g)

        actual = CommonsGraph.minimumSpanningTree(input)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .fromArbitrarySource()\
            .applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())
        
        self.assertEqual(expected, actual)

    
    @pytest.mark.test
    def testverifySparseGraphMinimumSpanningTree(self) -> None:
        with self.assertRaises(RuntimeError):
            input = UndirectedMutableGraph()

            input.addVertex(BaseLabeledVertex("A"))
            input.addVertex(BaseLabeledVertex("B"))
            input.addVertex(BaseLabeledVertex("C"))
            input.addVertex(BaseLabeledVertex("D"))
            input.addVertex(BaseLabeledVertex("E"))
            input.addVertex(BaseLabeledVertex("F"))
            input.addVertex(BaseLabeledVertex("G"))

            CommonsGraph.minimumSpanningTree(input)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .fromArbitrarySource()\
                .applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())
