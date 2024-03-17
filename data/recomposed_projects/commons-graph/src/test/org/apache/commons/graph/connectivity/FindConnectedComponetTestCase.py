# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityBuilder import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
# Imports End

class FindConnectedComponetTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def verifyNullGraph(self) -> None:

            self.findConnectedComponent(None) \
                .includingAllVertices() \
                .applyingMinimumSpanningTreeAlgorithm()

    def testVerifyNullVerticesGraph(self) -> None:


        pass # LLM could not translate method body

    def testVerifyEmptyGraph(self) -> None:

            graph = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()
            c = self.findConnectedComponent(graph).includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
            assertNotNull(c)
            self.assertEqual(0, len(c))

    def testVerifyConnectedComponentsIncludingVertices2(self) -> None:

            a = BaseLabeledVertex("A")
            e = BaseLabeledVertex("E")
            graph = self.newUndirectedMutableGraph(
                GraphConnection(
                    connect0=lambda: [
                        self.addVertex(a),
                        self.addVertex(BaseLabeledVertex("B")),
                        self.addVertex(BaseLabeledVertex("C")),
                        self.addVertex(BaseLabeledVertex("D")),
                        self.addVertex(e),
                        self.addVertex(BaseLabeledVertex("F")),
                        self.addVertex(BaseLabeledVertex("G")),
                        self.addVertex(BaseLabeledVertex("H")),
                    ]
                )
            )
            coll = self.findConnectedComponent(graph).includingVertices(a, e).applyingMinimumSpanningTreeAlgorithm()
            self.assertNotNull(coll)
            self.assertFalse(coll.isEmpty())
            self.assertEqual(2, coll.size())

    def testVerifyConnectedComponentsIncludingVertices(self) -> None:

            a = BaseLabeledVertex("A")
            graph = self.newUndirectedMutableGraph(
                GraphConnection[BaseLabeledVertex, BaseLabeledEdge]()
            )
            b = graph.addVertex(BaseLabeledVertex("B"))
            c = graph.addVertex(BaseLabeledVertex("C"))
            d = graph.addVertex(BaseLabeledVertex("D"))
            e = graph.addVertex(BaseLabeledVertex("E"))
            f = graph.addVertex(BaseLabeledVertex("F"))
            g = graph.addVertex(BaseLabeledVertex("G"))
            h = graph.addVertex(BaseLabeledVertex("H"))
            graph.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            graph.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            graph.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f)
            graph.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            graph.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            graph.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            graph.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)
            coll = self.findConnectedComponent(graph).includingVertices(a).applyingMinimumSpanningTreeAlgorithm()
            assertNotNull(coll)
            self.assertFalse(coll.isEmpty())
            self.assertEqual(1, coll.size())

    def testVerifyConnectedComponents3(self) -> None:


        pass # LLM could not translate method body

    def testVerifyConnectedComponents2(self) -> None:


        pass # LLM could not translate method body

    def testVerifyConnectedComponents(self) -> None:

            a = BaseLabeledVertex("A")
            graph = self.newUndirectedMutableGraph(
                GraphConnection(
                    connect0=lambda: [
                        self.addVertex(a),
                        self.addVertex(BaseLabeledVertex("B")),
                        self.addVertex(BaseLabeledVertex("C")),
                        self.addVertex(BaseLabeledVertex("D")),
                        self.addVertex(BaseLabeledVertex("E")),
                        self.addVertex(BaseLabeledVertex("F")),
                        self.addVertex(BaseLabeledVertex("G")),
                        self.addVertex(BaseLabeledVertex("H"))
                    ]
                )
            )
            c = self.findConnectedComponent(graph).includingAllVertices().applyingMinimumSpanningTreeAlgorithm()
            self.assertIsNotNone(c)
            self.assertFalse(c.isEmpty())
            self.assertEqual(8, len(c))

    # Class Methods End


class new AbstractGraphConnection<BaseLabeledVertex,BaseLabeledEdge>(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def connect0(self) -> None:

        self.addVertex(a)
        self.addVertex(BaseLabeledVertex("B"))
        self.addVertex(BaseLabeledVertex("C"))
        self.addVertex(BaseLabeledVertex("D"))
        self.addVertex(BaseLabeledVertex("E"))
        self.addVertex(BaseLabeledVertex("F"))
        self.addVertex(BaseLabeledVertex("G"))
        self.addVertex(BaseLabeledVertex("H"))

    def connect0(self) -> None:

            a = self.addVertex(a)
            b = self.addVertex(BaseLabeledVertex("B"))
            c = self.addVertex(BaseLabeledVertex("C"))
            d = self.addVertex(BaseLabeledVertex("D"))
            e = self.addVertex(BaseLabeledVertex("E"))
            f = self.addVertex(BaseLabeledVertex("F"))
            g = self.addVertex(BaseLabeledVertex("G"))
            h = self.addVertex(BaseLabeledVertex("H"))
            self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f)
            self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

    def connect0(self) -> None:


        pass # LLM could not translate method body

    def connect0(self) -> None:

            a = self.addVertex(a)
            b = self.addVertex(BaseLabeledVertex("B"))
            c = self.addVertex(BaseLabeledVertex("C"))
            d = self.addVertex(BaseLabeledVertex("D"))
            e = self.addVertex(BaseLabeledVertex("E"))
            f = self.addVertex(BaseLabeledVertex("F"))
            g = self.addVertex(BaseLabeledVertex("G"))
            h = self.addVertex(BaseLabeledVertex("H"))
            self.addEdge(BaseLabeledEdge("A -> F")).from_(a).to(f)
            self.addEdge(BaseLabeledEdge("A -> B")).from_(a).to(b)
            self.addEdge(BaseLabeledEdge("B -> F")).from_(b).to(f)
            self.addEdge(BaseLabeledEdge("C -> G")).from_(c).to(g)
            self.addEdge(BaseLabeledEdge("D -> G")).from_(d).to(g)
            self.addEdge(BaseLabeledEdge("E -> F")).from_(e).to(f)
            self.addEdge(BaseLabeledEdge("H -> C")).from_(h).to(c)

    def connect0(self) -> None:

            self.addVertex(a)
            self.addVertex(BaseLabeledVertex("B"))
            self.addVertex(BaseLabeledVertex("C"))
            self.addVertex(BaseLabeledVertex("D"))
            self.addVertex(e)
            self.addVertex(BaseLabeledVertex("F"))
            self.addVertex(BaseLabeledVertex("G"))
            self.addVertex(BaseLabeledVertex("H"))

    def connect0(self) -> None:

            self.addVertex(BaseLabeledVertex("B"))
            self.addVertex(BaseLabeledVertex("C"))

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


