# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
# Imports End

class GraphBuilderTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testVerifyProducedGraphesAreEquals(self) -> None:

            expected = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[Double]]()
            start = BaseLabeledVertex("start")
            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            c = BaseLabeledVertex("c")
            d = BaseLabeledVertex("d")
            e = BaseLabeledVertex("e")
            goal = BaseLabeledVertex("goal")
            expected.add_vertex(start)
            expected.add_vertex(a)
            expected.add_vertex(b)
            expected.add_vertex(c)
            expected.add_vertex(d)
            expected.add_vertex(e)
            expected.add_vertex(goal)
            expected.add_edge(start, BaseLabeledWeightedEdge("start <-> a", 1.5), a)
            expected.add_edge(start, BaseLabeledWeightedEdge("start <-> d", 2), d)
            expected.add_edge(a, BaseLabeledWeightedEdge("a <-> b", 2), b)
            expected.add_edge(b, BaseLabeledWeightedEdge("b <-> c", 3), c)
            expected.add_edge(c, BaseLabeledWeightedEdge("c <-> goal", 3), goal)
            expected.add_edge(d, BaseLabeledWeightedEdge("d <-> e", 3), e)
            expected.add_edge(e, BaseLabeledWeightedEdge("e <-> goal", 2), goal)
            actual = self.newUndirectedMutableGraph(
                GraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[Double]]()
            )
            self.assertEqual(expected, actual)

    # Class Methods End


class new AbstractGraphConnection<BaseLabeledVertex,BaseLabeledWeightedEdge<Double>>(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def connect0(self) -> None:

        start = self.addVertex(BaseLabeledVertex("start"))
        a = self.addVertex(BaseLabeledVertex("a"))
        b = self.addVertex(BaseLabeledVertex("b"))
        c = self.addVertex(BaseLabeledVertex("c"))
        d = self.addVertex(BaseLabeledVertex("d"))
        e = self.addVertex(BaseLabeledVertex("e"))
        goal = self.addVertex(BaseLabeledVertex("goal"))
        self.addEdge(BaseLabeledWeightedEdge("start <-> a", 1.5)) \
            .from_(start) \
            .to(a)
        self.addEdge(BaseLabeledWeightedEdge("start <-> d", 2)) \
            .from_(start) \
            .to(d)
        self.addEdge(BaseLabeledWeightedEdge("a <-> b", 2)) \
            .from_(a) \
            .to(b)
        self.addEdge(BaseLabeledWeightedEdge("b <-> c", 3)) \
            .from_(b) \
            .to(c)
        self.addEdge(BaseLabeledWeightedEdge("c <-> goal", 3)) \
            .from_(c) \
            .to(goal)
        self.addEdge(BaseLabeledWeightedEdge("d <-> e", 3)) \
            .from_(d) \
            .to(e)
        self.addEdge(BaseLabeledWeightedEdge("e <-> goal", 2)) \
            .from_(e) \
            .to(goal)

    def (self) -> None:


        pass # LLM could not translate method body

    # Class Methods End


