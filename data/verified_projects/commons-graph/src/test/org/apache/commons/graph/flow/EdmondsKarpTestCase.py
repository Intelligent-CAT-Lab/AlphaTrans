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

class EdmondsKarpTestCase(unittest.TestCase):

    def testFindMaxFlowAndVerify(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        graph = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionEdmondsKarpTestCaseTestFindMaxFlowAndVerify(a, g)
        )

        expected = 5

        actual = CommonsGraph.findMaxFlow(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .from_(a)\
            .to(g)\
            .applyingEdmondsKarp(IntegerWeightBaseOperations())
        
        self.assertEqual(expected, actual)
    
    
    def testNullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            a = BaseLabeledVertex("A")
            g = BaseLabeledVertex("G")

            CommonsGraph.findMaxFlow(None)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(a)\
                .to(g)\
                .applyingEdmondsKarp(IntegerWeightBaseOperations())

    
    def testNullVertices(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):

            a = None
            g = None

            graph = DirectedMutableGraph()

            CommonsGraph.findMaxFlow(graph)\
                .whereEdgesHaveWeights(BaseWeightedEdge())\
                .from_(a)\
                .to(g)\
                .applyingEdmondsKarp(IntegerWeightBaseOperations())

    
    def testSparse(self) -> None:
        a = BaseLabeledVertex("A")
        g = BaseLabeledVertex("G")

        graph = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionEdmondsKarpTestCaseTestSparse(a, g)
        )

        expected = 0

        actual = CommonsGraph.findMaxFlow(graph)\
            .whereEdgesHaveWeights(BaseWeightedEdge())\
            .from_(a)\
            .to(g)\
            .applyingEdmondsKarp(IntegerWeightBaseOperations())
        
        self.assertEqual(expected, actual)


    # Class Methods End


class GraphConnectionEdmondsKarpTestCaseTestFindMaxFlowAndVerify(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a)
        b = self.addVertex(BaseLabeledVertex("B"))
        c = self.addVertex(BaseLabeledVertex("C"))
        d = self.addVertex(BaseLabeledVertex("D"))
        e = self.addVertex(BaseLabeledVertex("E"))
        f = self.addVertex(BaseLabeledVertex("F"))
        self.addVertex(self.g)

        self.addEdge(BaseLabeledWeightedEdge("A -> B", 3))\
            .from_(self.a)\
            .to(b)
        self.addEdge(BaseLabeledWeightedEdge("A -> D", 3))\
            .from_(self.a)\
            .to(d)
        self.addEdge(BaseLabeledWeightedEdge("B -> C", 4))\
            .from_(b)\
            .to(c)
        self.addEdge(BaseLabeledWeightedEdge("C -> A", 3))\
            .from_(c)\
            .to(self.a)
        self.addEdge(BaseLabeledWeightedEdge("C -> D", 1))\
            .from_(c)\
            .to(d)
        self.addEdge(BaseLabeledWeightedEdge("C -> E", 2))\
            .from_(c)\
            .to(e)
        self.addEdge(BaseLabeledWeightedEdge("D -> E", 2))\
            .from_(d)\
            .to(e)
        self.addEdge(BaseLabeledWeightedEdge("D -> F", 6))\
            .from_(d)\
            .to(f)
        self.addEdge(BaseLabeledWeightedEdge("E -> B", 1))\
            .from_(e)\
            .to(b)
        self.addEdge(BaseLabeledWeightedEdge("E -> G", 1))\
            .from_(e)\
            .to(self.g)
        self.addEdge(BaseLabeledWeightedEdge("F -> G", 9))\
            .from_(f)\
            .to(self.g)
    

    def __init__(self, a, g, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a
        self.g = g


class GraphConnectionEdmondsKarpTestCaseTestSparse(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a)
        b = self.addVertex(BaseLabeledVertex("B"))
        c = self.addVertex(BaseLabeledVertex("C"))
        self.addVertex(BaseLabeledVertex("D"))
        self.addVertex(BaseLabeledVertex("E"))
        self.addVertex(BaseLabeledVertex("F"))
        self.addVertex(self.g)

        self.addEdge(BaseLabeledWeightedEdge("A -> B", 3))\
            .from_(self.a)\
            .to(b)
        self.addEdge(BaseLabeledWeightedEdge("B -> C", 4))\
            .from_(b)\
            .to(c)
    

    def __init__(self, a, g, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a
        self.g = g



