import pytest

# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityBuilder import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
# Imports End

class FindConnectedComponetTestCase(unittest.TestCase):

    @pytest.mark.test
    def testVerifyConnectedComponents(self) -> None:
        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionFindConnectedComponetTestCaseTestVerifyConnectedComponents(a)
        )

        c = CommonsGraph.findConnectedComponent(graph)\
            .includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
        
        self.assertIsNotNone(c)
        self.assertFalse(len(c) == 0)
        self.assertEqual(8, len(c))
    

    @pytest.mark.test
    def testVerifyConnectedComponents2(self) -> None:
        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionFindConnectedComponetTestCaseTestVerifyConnectedComponents2(a)
        )

        c = CommonsGraph.findConnectedComponent(graph)\
            .includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
        
        self.assertIsNotNone(c)
        self.assertFalse(len(c) == 0)
        self.assertEqual(2, len(c))


    @pytest.mark.test
    def testVerifyConnectedComponents3(self) -> None:
        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionFindConnectedComponetTestCaseTestVerifyConnectedComponents3(a)
        )

        c = CommonsGraph.findConnectedComponent(graph)\
            .includingAllVertices().applyingMinimumSpanningTreeAlgorithm()

        self.assertIsNotNone(c)
        self.assertFalse(len(c) == 0)
        self.assertEqual(1, len(c))
    
    
    @pytest.mark.test
    def testVerifyConnectedComponentsIncludingVertices(self) -> None:
        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionFindConnectedComponetTestCaseTestVerifyConnectedComponentsIncludingVertices(a)
        )

        coll = CommonsGraph.findConnectedComponent(graph)\
            .includingVertices(a).applyingMinimumSpanningTreeAlgorithm()
        
        self.assertIsNotNone(coll)
        self.assertFalse(len(coll) == 0)
        self.assertEqual(1, len(coll))

    
    @pytest.mark.test
    def testVerifyConnectedComponentsIncludingVertices2(self) -> None:
        a = BaseLabeledVertex("A")
        e = BaseLabeledVertex("E")

        graph = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionFindConnectedComponetTestCaseTestVerifyConnectedComponentsIncludingVertices2(a, e)
        )

        coll = CommonsGraph.findConnectedComponent(graph)\
            .includingVertices(a, e).applyingMinimumSpanningTreeAlgorithm()
        
        self.assertIsNotNone(coll)
        self.assertFalse(len(coll) == 0)
        self.assertEqual(2, len(coll))


    @pytest.mark.test
    def testVerifyEmptyGraph(self) -> None:
        graph = UndirectedMutableGraph()

        c = CommonsGraph.findConnectedComponent(graph)\
            .includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
        self.assertIsNotNone(c)
        self.assertEqual(0, len(c))


    @pytest.mark.test
    def testVerifyNullVerticesGraph(self) -> None:
        graph = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionFindConnectedComponetTestCaseTestVerifyNullVerticesGraph()
        )
        c = CommonsGraph.findConnectedComponent(graph)\
            .includingVertices().applyingMinimumSpanningTreeAlgorithm()
        self.assertIsNotNone(c)
        self.assertEqual(0, len(c))

    
    @pytest.mark.test
    def testverifyNullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            CommonsGraph.findConnectedComponent(None)\
                .includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
    
    # Class Methods End


class GraphConnectionFindConnectedComponetTestCaseTestVerifyConnectedComponents(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a)
        self.addVertex(BaseLabeledVertex("B"))
        self.addVertex(BaseLabeledVertex("C"))
        self.addVertex(BaseLabeledVertex("D"))
        self.addVertex(BaseLabeledVertex("E"))
        self.addVertex(BaseLabeledVertex("F"))
        self.addVertex(BaseLabeledVertex("G"))
        self.addVertex(BaseLabeledVertex("H"))
    

    def __init__(self, a, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a


class GraphConnectionFindConnectedComponetTestCaseTestVerifyConnectedComponents2(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a)
        b = self.addVertex(BaseLabeledVertex("B"))
        c = self.addVertex(BaseLabeledVertex("C"))
        d = self.addVertex(BaseLabeledVertex("D"))
        e = self.addVertex(BaseLabeledVertex("E"))
        f = self.addVertex(BaseLabeledVertex("F"))
        g = self.addVertex(BaseLabeledVertex("G"))
        h = self.addVertex(BaseLabeledVertex("H"))

        self.addEdge(BaseLabeledEdge("A -> F")).from_(self.a).to(f)
        self.addEdge(BaseLabeledEdge("A -> B")).from_(self.a).to(b)
        self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f)
        self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
        self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
        self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
        self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)
    

    def __init__(self, a, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a


class GraphConnectionFindConnectedComponetTestCaseTestVerifyConnectedComponents3(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a)
        b = self.addVertex(BaseLabeledVertex("B"))
        c = self.addVertex(BaseLabeledVertex("C"))

        self.addEdge(BaseLabeledEdge("A -> B")).from_(self.a).to(b)
        self.addEdge(BaseLabeledEdge("B -> C")).from_(b).to(c)
        self.addEdge(BaseLabeledEdge("C -> A")).from_(c).to(self.a)
    

    def __init__(self, a, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a


class GraphConnectionFindConnectedComponetTestCaseTestVerifyConnectedComponentsIncludingVertices(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a)
        b = self.addVertex(BaseLabeledVertex("B"))
        c = self.addVertex(BaseLabeledVertex("C"))
        d = self.addVertex(BaseLabeledVertex("D"))
        e = self.addVertex(BaseLabeledVertex("E"))
        f = self.addVertex(BaseLabeledVertex("F"))
        g = self.addVertex(BaseLabeledVertex("G"))
        h = self.addVertex(BaseLabeledVertex("H"))
        
        self.addEdge(BaseLabeledEdge("A -> F")).from_(self.a).to(f)
        self.addEdge(BaseLabeledEdge("A -> B")).from_(self.a).to(b)
        self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f)
        self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
        self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
        self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
        self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)
    

    def __init__(self, a, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a


class GraphConnectionFindConnectedComponetTestCaseTestVerifyConnectedComponentsIncludingVertices2(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a),
        self.addVertex(BaseLabeledVertex("B"))
        self.addVertex(BaseLabeledVertex("C"))
        self.addVertex(BaseLabeledVertex("D"))
        self.addVertex(self.e),
        self.addVertex(BaseLabeledVertex("F"))
        self.addVertex(BaseLabeledVertex("G"))
        self.addVertex(BaseLabeledVertex("H"))
    

    def __init__(self, a, e, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a
        self.e = e


class GraphConnectionFindConnectedComponetTestCaseTestVerifyNullVerticesGraph(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(BaseLabeledVertex("B"))
        self.addVertex(BaseLabeledVertex("C"))
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
