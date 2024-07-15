from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityBuilder import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class FindConnectedComponetTestCase(unittest.TestCase):

    def testverifyNullGraph(self) -> None:

        with pytest.raises(RuntimeError):
            CommonsGraph.findConnectedComponent(
                None
            ).includingAllVertices().applyingMinimumSpanningTreeAlgorithm()

    def testVerifyNullVerticesGraph(self) -> None:

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection()
            .addVertex(BaseLabeledVertex("B"))
            .addVertex(BaseLabeledVertex("C"))
        )

        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )

        assert c is not None
        assert len(c) == 0

    def testVerifyEmptyGraph(self) -> None:

        graph = UndirectedMutableGraph()

        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingAllVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )
        assert c is not None
        self.assertEqual(0, len(c))

    def testVerifyConnectedComponentsIncludingVertices2(self) -> None:

        a = BaseLabeledVertex("A")
        e = BaseLabeledVertex("E")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection()
            .addVertex(a)
            .addVertex(BaseLabeledVertex("B"))
            .addVertex(BaseLabeledVertex("C"))
            .addVertex(BaseLabeledVertex("D"))
            .addVertex(e)
            .addVertex(BaseLabeledVertex("F"))
            .addVertex(BaseLabeledVertex("G"))
            .addVertex(BaseLabeledVertex("H"))
        )

        coll = (
            CommonsGraph.findConnectedComponent(graph)
            .includingVertices(a, e)
            .applyingMinimumSpanningTreeAlgorithm()
        )

        assert coll is not None
        assert len(coll) != 0
        assert len(coll) == 2

    def testVerifyConnectedComponentsIncludingVertices(self) -> None:

        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection()
            .addVertex(a)
            .addVertex(BaseLabeledVertex("B"))
            .addVertex(BaseLabeledVertex("C"))
            .addVertex(BaseLabeledVertex("D"))
            .addVertex(BaseLabeledVertex("E"))
            .addVertex(BaseLabeledVertex("F"))
            .addVertex(BaseLabeledVertex("G"))
            .addVertex(BaseLabeledVertex("H"))
            .addEdge(BaseLabeledEdge("A -> F"))
            .from_(a)
            .to(BaseLabeledVertex("F"))
            .addEdge(BaseLabeledEdge("A -> B"))
            .from_(a)
            .to(BaseLabeledVertex("B"))
            .addEdge(BaseLabeledEdge("B -> F"))
            .from_(BaseLabeledVertex("B"))
            .to(BaseLabeledVertex("F"))
            .addEdge(BaseLabeledEdge("C -> G"))
            .from_(BaseLabeledVertex("C"))
            .to(BaseLabeledVertex("G"))
            .addEdge(BaseLabeledEdge("D -> G"))
            .from_(BaseLabeledVertex("D"))
            .to(BaseLabeledVertex("G"))
            .addEdge(BaseLabeledEdge("E -> F"))
            .from_(BaseLabeledVertex("E"))
            .to(BaseLabeledVertex("F"))
            .addEdge(BaseLabeledEdge("H -> C"))
            .from_(BaseLabeledVertex("H"))
            .to(BaseLabeledVertex("C"))
        )

        coll = (
            CommonsGraph.findConnectedComponent(graph)
            .includingVertices(a)
            .applyingMinimumSpanningTreeAlgorithm()
        )

        assert coll is not None
        assert len(coll) != 0
        assert len(coll) == 1

    def testVerifyConnectedComponents3(self) -> None:

        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection()
            .addVertex(a)
            .addVertex(BaseLabeledVertex("B"))
            .addVertex(BaseLabeledVertex("C"))
            .addEdge(BaseLabeledEdge("A -> B"))
            .from_(a)
            .to(b)
            .addEdge(BaseLabeledEdge("B -> C"))
            .from_(b)
            .to(c)
            .addEdge(BaseLabeledEdge("C -> A"))
            .from_(c)
            .to(a)
        )

        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingAllVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )

        assert c is not None
        assert len(c) != 0
        assert len(c) == 1

    def testVerifyConnectedComponents2(self) -> None:

        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection()
            .addVertex(a)
            .addVertex(BaseLabeledVertex("B"))
            .addVertex(BaseLabeledVertex("C"))
            .addVertex(BaseLabeledVertex("D"))
            .addVertex(BaseLabeledVertex("E"))
            .addVertex(BaseLabeledVertex("F"))
            .addVertex(BaseLabeledVertex("G"))
            .addVertex(BaseLabeledVertex("H"))
            .addEdge(BaseLabeledEdge("A -> F"))
            .from_(a)
            .to(f)
            .addEdge(BaseLabeledEdge("A -> B"))
            .from_(a)
            .to(b)
            .addEdge(BaseLabeledEdge("B -> F"))
            .from_(b)
            .to(f)
            .addEdge(BaseLabeledEdge("C -> G"))
            .from_(c)
            .to(g)
            .addEdge(BaseLabeledEdge("D -> G"))
            .from_(d)
            .to(g)
            .addEdge(BaseLabeledEdge("E -> F"))
            .from_(e)
            .to(f)
            .addEdge(BaseLabeledEdge("H -> C"))
            .from_(h)
            .to(c)
        )

        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingAllVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )

        assert c is not None
        assert len(c) != 0
        assert len(c) == 2

    def testVerifyConnectedComponents(self) -> None:

        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: [
                    addVertex(a),
                    addVertex(BaseLabeledVertex("B")),
                    addVertex(BaseLabeledVertex("C")),
                    addVertex(BaseLabeledVertex("D")),
                    addVertex(BaseLabeledVertex("E")),
                    addVertex(BaseLabeledVertex("F")),
                    addVertex(BaseLabeledVertex("G")),
                    addVertex(BaseLabeledVertex("H")),
                ]
            )
        )

        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingAllVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )

        assert c is not None
        assert len(c) != 0
        assert len(c) == 8
