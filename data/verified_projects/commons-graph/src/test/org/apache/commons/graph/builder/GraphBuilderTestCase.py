# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
# Imports End

class GraphBuilderTestCase(unittest.TestCase):

    def testVerifyProducedGraphesAreEquals(self) -> None:
        expected = UndirectedMutableGraph()
        
        start = BaseLabeledVertex("start")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")
        d = BaseLabeledVertex("d")
        e = BaseLabeledVertex("e")
        goal = BaseLabeledVertex("goal")

        expected.addVertex(start)
        expected.addVertex(a)
        expected.addVertex(b)
        expected.addVertex(c)
        expected.addVertex(d)
        expected.addVertex(e)
        expected.addVertex(goal)

        expected.addEdge(start, BaseLabeledWeightedEdge("start <-> a", 1.5), a)
        expected.addEdge(start, BaseLabeledWeightedEdge("start <-> d", 2), d)

        expected.addEdge(a, BaseLabeledWeightedEdge("a <-> b", 2), b)
        expected.addEdge(b, BaseLabeledWeightedEdge("b <-> c", 3), c)
        expected.addEdge(c, BaseLabeledWeightedEdge("c <-> goal", 3), goal)

        expected.addEdge(d, BaseLabeledWeightedEdge("d <-> e", 3), e)
        expected.addEedge(e, BaseLabeledWeightedEdge("e <-> goal", 2), goal)

        actual = CommonsGraph.newUndirectedMutableGraph(
            GraphConnectionGraphBuilderTestCase()
        )
        self.assertEqual(expected, actual)



class GraphConnectionGraphBuilderTestCase(AbstractGraphConnection):
    def connect0(self) -> None:
        start = self.addVertex(BaseLabeledVertex("start"))
        a = self.addVertex(BaseLabeledVertex("a"))
        b = self.addVertex(BaseLabeledVertex("b"))
        c = self.addVertex(BaseLabeledVertex("c"))
        d = self.addVertex(BaseLabeledVertex("d"))
        e = self.addVertex(BaseLabeledVertex("e"))
        goal = self.addVertex(BaseLabeledVertex("goal"))

        self.addEdge(BaseLabeledWeightedEdge("start <-> a", 1.5))\
            .from_(start)\
            .to(a)
        self.addEdge(BaseLabeledWeightedEdge("start <-> d", 2))\
            .from_(start)\
            .to(d)
        
        self.addEdge(BaseLabeledWeightedEdge("a <-> b", 2))\
            .from_(a)\
            .to(b)
        self.addEdge(BaseLabeledWeightedEdge("b <-> c", 3))\
            .from_(b)\
            .to(c)
        self.addEdge(BaseLabeledWeightedEdge("c <-> goal", 3))\
            .from_(c)\
            .to(goal)
        
        self.addEdge(BaseLabeledWeightedEdge("d <-> e", 3))\
            .from_(d)\
            .to(e)
        self.addEdge(BaseLabeledWeightedEdge("e <-> goal", 2))\
            .from_(e)\
            .to(goal)
