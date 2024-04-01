# Imports Begin
from src.main.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
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

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testNullVertices(self) -> None:


        pass # LLM could not translate method body

    def testNullGraphAndVertices(self) -> None:

            self.findMaxFlow(
                graph=None,
                vertices=None,
                edge_weights=BaseWeightedEdge(),
                source_vertex=None,
                sink_vertex=None,
                weight_operations=IntegerWeightBaseOperations()
            )

    def testNullGraph(self) -> None:


        pass # LLM could not translate method body

    def testNotConnected_2(self) -> None:

            a = BaseLabeledVertex("A")
            d = BaseLabeledVertex("D")
            graph = self.newDirectedMutableGraph(
                GraphConnection(
                    lambda: [
                        self.addVertex(a),
                        self.addVertex(BaseLabeledVertex("B")),
                        self.addVertex(BaseLabeledVertex("C")),
                        self.addVertex(d),
                        self.addEdge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)
                    ]
                )
            )
            expected = 0
            actual = self.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(a).to(d).applyingFordFulkerson(IntegerWeightBaseOperations())
            self.assertEqual(actual, expected)

    def testNotConnected(self) -> None:

            a = BaseLabeledVertex("A")
            d = BaseLabeledVertex("D")
            graph = self.newDirectedMutableGraph(
                GraphConnection(
                    connect0=lambda: [
                        self.addVertex(a),
                        self.addVertex(BaseLabeledVertex("B")),
                        self.addVertex(BaseLabeledVertex("C")),
                        self.addVertex(d),
                    ]
                )
            )
            expected = 0
            actual = self.findMaxFlow(graph).whereEdgesHaveWeights(
                BaseLabeledWeightedEdge()
            ).from_(a).to_(d).applyingFordFulkerson(IntegerWeightBaseOperations())
            self.assertEqual(actual, expected)

    def testFindMaxFlowAndVerify(self) -> None:

            a = BaseLabeledVertex("A")
            d = BaseLabeledVertex("D")
            graph = self.newDirectedMutableGraph(
                GraphConnection(
                    lambda: [
                        a,
                        BaseLabeledVertex("B"),
                        BaseLabeledVertex("C"),
                        d,
                    ],
                    lambda: [
                        BaseLabeledWeightedEdge("A -> B", 1000).from_(a).to(BaseLabeledVertex("B")),
                        BaseLabeledWeightedEdge("A -> C", 1000).from_(a).to(BaseLabeledVertex("C")),
                        BaseLabeledWeightedEdge("B -> C", 1).from_(BaseLabeledVertex("B")).to(BaseLabeledVertex("C")),
                        BaseLabeledWeightedEdge("B -> D", 1000).from_(BaseLabeledVertex("B")).to(d),
                        BaseLabeledWeightedEdge("C -> D", 1000).from_(BaseLabeledVertex("C")).to(d),
                    ],
                )
            )
            expected = 2000
            actual = self.findMaxFlow(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(a).to(d).applyingFordFulkerson(IntegerWeightBaseOperations())
            self.assertEqual(expected, actual)

    # Class Methods End


class new AbstractGraphConnection<BaseLabeledVertex,BaseLabeledWeightedEdge<Integer>>(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def connect0(self) -> None:

        self.add_vertex(a)
        b = self.add_vertex(BaseLabeledVertex("B"))
        c = self.add_vertex(BaseLabeledVertex("C"))
        self.add_vertex(d)
        self.add_edge(BaseLabeledWeightedEdge("A -> B", 1000)).from_(a).to(b)
        self.add_edge(BaseLabeledWeightedEdge("A -> C", 1000)).from_(a).to(c)
        self.add_edge(BaseLabeledWeightedEdge("B -> C", 1)).from_(b).to(c)
        self.add_edge(BaseLabeledWeightedEdge("B -> D", 1000)).from_(b).to(d)
        self.add_edge(BaseLabeledWeightedEdge("C -> D", 1000)).from_(c).to(d)

    def connect0(self) -> None:

            self.addVertex(a)
            self.addVertex(BaseLabeledVertex("B"))
            self.addVertex(BaseLabeledVertex("C"))
            self.addVertex(d)

    def connect0(self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    def (self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


