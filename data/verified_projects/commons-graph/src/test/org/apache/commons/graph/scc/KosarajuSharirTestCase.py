import pytest

from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import unittest
from typing import *


class KosarajuSharirTestCase(unittest.TestCase):

    @pytest.mark.test
    def testNotExistVertex(self) -> None:
        with self.assertRaises(RuntimeError):
            graph = DirectedMutableGraph()

            CommonsGraph.findStronglyConnectedComponent(graph)\
                .applyingKosarajuSharir1(BaseLabeledVertex("NOT EXISTS"))
    
    
    @pytest.mark.test
    def testNullGraph(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            graph = None
            CommonsGraph.findStronglyConnectedComponent(graph)\
                .applyingKosarajuSharir0()

    
    @pytest.mark.test
    def testNullVertices(self) -> None:
        with self.assertRaises((TypeError, AttributeError)):
            a = None
            graph = DirectedMutableGraph()
            CommonsGraph.findStronglyConnectedComponent(graph)\
                .applyingKosarajuSharir1(a)

    
    @pytest.mark.test
    def testUnconnectedGraph(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            GraphConnectionKosarajuSharirTestCaseTestUnconnectedGraph(
                a,
                b,
                c,
                d,
                e,
                f,
                g,
                h
            )
        )

        expected = set([frozenset([a, b, d]), frozenset([e, f]), frozenset([g, h, c])])

        actual = CommonsGraph.findStronglyConnectedComponent(graph)\
            .applyingKosarajuSharir0()
        
        self.assertFalse(len(actual) == 0)
        self.assertEqual(expected, actual)

        actualA = CommonsGraph.findStronglyConnectedComponent(graph)\
            .applyingKosarajuSharir1(a)
        
        self.assertFalse(len(actualA) == 0)
        self.assertEqual({a, b, d}, actualA)

        actualE = CommonsGraph.findStronglyConnectedComponent(graph)\
            .applyingKosarajuSharir1(e)
        
        self.assertFalse(len(actualE) == 0)
        self.assertEqual({e, f}, actualE)

        actualG = CommonsGraph.findStronglyConnectedComponent(graph)\
            .applyingKosarajuSharir1(g)
        
        self.assertFalse(len(actualG) == 0)
        self.assertEqual({g, h, c}, actualG)

    
    @pytest.mark.test
    def testVerifyHasStronglyConnectedComponents(self) -> None:
        a = BaseLabeledVertex("A")
        b = BaseLabeledVertex("B")
        c = BaseLabeledVertex("C")
        d = BaseLabeledVertex("D")
        e = BaseLabeledVertex("E")
        f = BaseLabeledVertex("F")
        g = BaseLabeledVertex("G")
        h = BaseLabeledVertex("H")

        graph = CommonsGraph.newDirectedMutableGraph(
            GraphConnectionKosarajuSharirTestVerifyHasStronglyConnectedComponents(
                a,
                b,
                c,
                d,
                e,
                f,
                g,
                h
            )
        )

        expected = set([frozenset([a, b, d]), frozenset([e, f]), frozenset([g, h, c])])

        actual = CommonsGraph.findStronglyConnectedComponent(graph)\
            .applyingKosarajuSharir0()
        
        self.assertFalse(len(actual) == 0)
        self.assertEqual(expected, actual)

        actualA = CommonsGraph.findStronglyConnectedComponent(graph)\
            .applyingKosarajuSharir1(a)
        
        self.assertFalse(len(actualA) == 0)
        self.assertEqual({a, b, d}, actualA)

        actualE = CommonsGraph.findStronglyConnectedComponent(graph)\
            .applyingKosarajuSharir1(e)
        
        self.assertFalse(len(actualE) == 0)
        self.assertEqual({e, f}, actualE)

        actualG = CommonsGraph.findStronglyConnectedComponent(graph)\
            .applyingKosarajuSharir1(g)
        
        self.assertFalse(len(actualG) == 0)
        self.assertEqual({g, h, c}, actualG)


class GraphConnectionKosarajuSharirTestCaseTestUnconnectedGraph(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a)
        self.addVertex(self.b)
        self.addVertex(self.c)
        self.addVertex(self.d)
        self.addVertex(self.e)
        self.addVertex(self.f)
        self.addVertex(self.g)
        self.addVertex(self.h)

        self.addEdge(BaseLabeledEdge("A -> B")).from_(self.a).to(self.b)
        self.addEdge(BaseLabeledEdge("B -> D")).from_(self.b).to(self.d)
        self.addEdge(BaseLabeledEdge("C -> G")).from_(self.c).to(self.g)
        self.addEdge(BaseLabeledEdge("D -> A")).from_(self.d).to(self.a)
        self.addEdge(BaseLabeledEdge("E -> C")).from_(self.e).to(self.c)
        self.addEdge(BaseLabeledEdge("E -> F")).from_(self.e).to(self.f)
        self.addEdge(BaseLabeledEdge("F -> E")).from_(self.f).to(self.e)
        self.addEdge(BaseLabeledEdge("G -> H")).from_(self.g).to(self.h)
        self.addEdge(BaseLabeledEdge("H -> C")).from_(self.h).to(self.c)
    

    def __init__(self, a, b, c, d, e, f, g, h, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h


class GraphConnectionKosarajuSharirTestVerifyHasStronglyConnectedComponents(AbstractGraphConnection):

    def connect0(self) -> None:
        self.addVertex(self.a)
        self.addVertex(self.b)
        self.addVertex(self.c)
        self.addVertex(self.d)
        self.addVertex(self.e)
        self.addVertex(self.f)
        self.addVertex(self.g)
        self.addVertex(self.h)

        self.addEdge(BaseLabeledEdge("A -> F")).from_(self.a).to(self.f)
        self.addEdge(BaseLabeledEdge("A -> B")).from_(self.a).to(self.b)
        self.addEdge(BaseLabeledEdge("B -> D")).from_(self.b).to(self.d)
        self.addEdge(BaseLabeledEdge("C -> G")).from_(self.c).to(self.g)
        self.addEdge(BaseLabeledEdge("D -> A")).from_(self.d).to(self.a)
        self.addEdge(BaseLabeledEdge("D -> G")).from_(self.d).to(self.g)
        self.addEdge(BaseLabeledEdge("E -> C")).from_(self.e).to(self.c)
        self.addEdge(BaseLabeledEdge("E -> F")).from_(self.e).to(self.f)
        self.addEdge(BaseLabeledEdge("F -> E")).from_(self.f).to(self.e)
        self.addEdge(BaseLabeledEdge("G -> H")).from_(self.g).to(self.h)
        self.addEdge(BaseLabeledEdge("H -> C")).from_(self.h).to(self.c)
    

    def __init__(self, a, b, c, d, e, f, g, h, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
