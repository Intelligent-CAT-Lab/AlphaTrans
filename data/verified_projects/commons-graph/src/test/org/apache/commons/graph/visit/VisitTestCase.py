import pytest

from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.test.org.apache.commons.graph.visit.NodeSequenceVisitor import NodeSequenceVisitor
import unittest


class VisitTestCase(unittest.TestCase):

    @pytest.mark.test
    def testNotExistVertex(self) -> None:
        with self.assertRaises(RuntimeError):
            input = CommonsGraph.newDirectedMutableGraph(
                GraphConnectionVisitTestCaseTestNotExistVertex()
            )

            CommonsGraph.visit(input)\
                .from_(BaseLabeledVertex("NOT EXIST"))

    
    @pytest.mark.test
    def testVerifyBreadthFirstSearch(self) -> None:
        input = CommonsGraph.newDirectedMutableGraph(
            GraphConnectionVisitTestCaseTestVerifyBreadthFirstSearchInput()
        )

        expected = CommonsGraph.newDirectedMutableGraph(
            GraphConnectionVisitTestCaseTestVerifyBreadthFirstSearchExpected()
        )

        actual = CommonsGraph.visit(input)\
            .from_(BaseLabeledVertex("s"))\
            .applyingBreadthFirstSearch0()
        
        self.assertEqual(expected, actual)

    
    @pytest.mark.test
    def testVerifyDepthFirstSearch(self) -> None:
        expected = []

        input = CommonsGraph.newDirectedMutableGraph(
            GraphConnectionVisitTestCaseTestVerifyDepthFirstSearch(expected)
        )

        actual = CommonsGraph.visit(input)\
            .from_(BaseLabeledVertex("S"))\
            .applyingDepthFirstSearch1(NodeSequenceVisitor())
        
        self.assertEqual(expected, actual)


class GraphConnectionVisitTestCaseTestNotExistVertex(AbstractGraphConnection):

    def connect0(self) -> None:
        pass


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GraphConnectionVisitTestCaseTestVerifyBreadthFirstSearchInput(AbstractGraphConnection):

    def connect0(self) -> None:
        r = self.addVertex(BaseLabeledVertex("r"))
        s = self.addVertex(BaseLabeledVertex("s"))
        t = self.addVertex(BaseLabeledVertex("t"))
        u = self.addVertex(BaseLabeledVertex("u"))
        v = self.addVertex(BaseLabeledVertex("v"))
        w = self.addVertex(BaseLabeledVertex("w"))
        x = self.addVertex(BaseLabeledVertex("x"))
        y = self.addVertex(BaseLabeledVertex("y"))

        self.addEdge(BaseLabeledEdge("s <-> r")).from_(s).to(r)
        self.addEdge(BaseLabeledEdge("s <-> w")).from_(s).to(w)

        self.addEdge(BaseLabeledEdge("r <-> v")).from_(r).to(v)

        self.addEdge(BaseLabeledEdge("w <-> t")).from_(w).to(t)
        self.addEdge(BaseLabeledEdge("w <-> x")).from_(w).to(x)

        self.addEdge(BaseLabeledEdge("t <-> u")).from_(t).to(u)
        self.addEdge(BaseLabeledEdge("t <-> x")).from_(t).to(x)

        self.addEdge(BaseLabeledEdge("y <-> u")).from_(y).to(u)
        self.addEdge(BaseLabeledEdge("x <-> y")).from_(x).to(y)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GraphConnectionVisitTestCaseTestVerifyBreadthFirstSearchExpected(AbstractGraphConnection):

    def connect0(self) -> None:
        r = self.addVertex(BaseLabeledVertex("r"))
        s = self.addVertex(BaseLabeledVertex("s"))
        t = self.addVertex(BaseLabeledVertex("t"))
        u = self.addVertex(BaseLabeledVertex("u"))
        v = self.addVertex(BaseLabeledVertex("v"))
        w = self.addVertex(BaseLabeledVertex("w"))
        x = self.addVertex(BaseLabeledVertex("x"))
        y = self.addVertex(BaseLabeledVertex("y"))

        self.addEdge(BaseLabeledEdge("s <-> r")).from_(s).to(r)
        self.addEdge(BaseLabeledEdge("s <-> w")).from_(s).to(w)

        self.addEdge(BaseLabeledEdge("r <-> v")).from_(r).to(v)

        self.addEdge(BaseLabeledEdge("w <-> t")).from_(w).to(t)
        self.addEdge(BaseLabeledEdge("w <-> x")).from_(w).to(x)

        self.addEdge(BaseLabeledEdge("t <-> u")).from_(t).to(u)

        self.addEdge(BaseLabeledEdge("x <-> y")).from_(x).to(y)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GraphConnectionVisitTestCaseTestVerifyDepthFirstSearch(AbstractGraphConnection):

    def connect0(self) -> None:
        a = self.addVertex(BaseLabeledVertex("A"))
        b = self.addVertex(BaseLabeledVertex("B"))
        c = self.addVertex(BaseLabeledVertex("C"))
        d = self.addVertex(BaseLabeledVertex("D"))
        e = self.addVertex(BaseLabeledVertex("E"))
        f = self.addVertex(BaseLabeledVertex("F"))
        g = self.addVertex(BaseLabeledVertex("G"))
        h = self.addVertex(BaseLabeledVertex("H"))
        s = self.addVertex(BaseLabeledVertex("S"))

        self.addEdge(BaseLabeledEdge("S <-> A")).from_(s).to(a)
        self.addEdge(BaseLabeledEdge("S <-> B")).from_(s).to(b)

        self.addEdge(BaseLabeledEdge("A <-> C")).from_(a).to(c)
        self.addEdge(BaseLabeledEdge("A <-> D")).from_(a).to(d)

        self.addEdge(BaseLabeledEdge("B <-> E")).from_(b).to(e)
        self.addEdge(BaseLabeledEdge("B <-> F")).from_(b).to(f)

        self.addEdge(BaseLabeledEdge("E <-> H")).from_(e).to(h)
        self.addEdge(BaseLabeledEdge("E <-> G")).from_(e).to(g)

        self.expected.append(s)
        self.expected.append(b)
        self.expected.append(f)
        self.expected.append(e)
        self.expected.append(g)
        self.expected.append(h)
        self.expected.append(a)
        self.expected.append(d)
        self.expected.append(c)
    

    def __init__(self, expected, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.expected = expected
