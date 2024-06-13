# Imports Begin
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.flow.ToTailBuilder import *
from src.main.org.apache.commons.graph.flow.MaxFlowAlgorithmSelector import *
from src.main.org.apache.commons.graph.flow.FromHeadBuilder import *
from src.main.org.apache.commons.graph.flow.FlowWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
# Imports End

class FordFulkersonTestCase(unittest.TestCase):

    def testFindMaxFlowAndVerify(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        graph = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionFordFulkersonTestCaseTestFindMaxFlowAndVerify(a, d)
        )

        expected = 2000
        
        actual = CommonsGraph.findMaxFlow(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .from_(a)\
            .to(d)\
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        
        self.assertEqual(expected, actual)
    

    def testNotConnected(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        graph = CommonsGraph.newDirectedMutableGraph(
            GraphConnectionFordFulkersonTestCaseTestNotConnected(a, d)
        )

        expected = 0

        actual = CommonsGraph.findMaxFlow(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .from_(a)\
            .to(d)\
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        
        self.assertEqual(actual, expected)
    
    
    def testNotConnected_2(self) -> None:
        a = BaseLabeledVertex("A")
        d = BaseLabeledVertex("D")

        graph = CommonsGraph.newDirectedMutableGraph(
            GraphConnectionFordFulkersonTestCaseTestNotConnected_2(a, d)
        )

        expected = 0
        
        actual = CommonsGraph.findMaxFlow(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .from_(a)\
            .to(d)\
            .applyingFordFulkerson(IntegerWeightBaseOperations())
        
        self.assertEqual(actual, expected)

    
    def testNullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            a = BaseLabeledVertex("A")
            d = BaseLabeledVertex("D")

            CommonsGraph.findMaxFlow(None)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(a)\
                .to(d)\
                .applyingFordFulkerson(IntegerWeightBaseOperations())

    
    def testNullGraphAndVertices(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            CommonsGraph.findMaxFlow(None)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(None)\
                .to(None)\
                .applyingFordFulkerson(IntegerWeightBaseOperations())

    
    def testNullVertices(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            graph = DirectedMutableGraph()
            CommonsGraph.findMaxFlow(graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(None)\
                .to(None)\
                .applyingFordFulkerson(IntegerWeightBaseOperations())

    # Class Methods End


class GraphConnectionFordFulkersonTestCaseTestFindMaxFlowAndVerify(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a)
        b = self.addVertex(BaseLabeledVertex("B"))
        c = self.addVertex(BaseLabeledVertex("C"))
        self.addVertex(self.d)

        self.addEdge(BaseLabeledWeightedEdge("A -> B", 1000))\
            .from_(self.a)\
            .to(b)
        self.addEdge(BaseLabeledWeightedEdge("A -> C", 1000))\
            .from_(self.a)\
            .to(c)
        self.addEdge(BaseLabeledWeightedEdge("B -> C", 1))\
            .from_(b)\
            .to(c)
        self.addEdge(BaseLabeledWeightedEdge("B -> D", 1000))\
            .from_(b)\
            .to(self.d)
        self.addEdge(BaseLabeledWeightedEdge("C -> D", 1000))\
            .from_(c)\
            .to(self.d)
    

    def __init__(self, a, d, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a
        self.d = d


class GraphConnectionFordFulkersonTestCaseTestNotConnected(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a)
        self.addVertex(BaseLabeledVertex("B"))
        self.addVertex(BaseLabeledVertex("C"))
        self.addVertex(self.d)
    

    def __init__(self, a, d, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a
        self.d = d


class GraphConnectionFordFulkersonTestCaseTestNotConnected_2(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a)
        b = self.addVertex(BaseLabeledVertex("B"))
        self.addVertex(BaseLabeledVertex("C"))
        self.addVertex(self.d)

        self.addEdge(BaseLabeledWeightedEdge("A -> B", 1000))\
            .from_(self.a)\
            .to(b)
    

    def __init__(self, a, d, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a
        self.d = d


