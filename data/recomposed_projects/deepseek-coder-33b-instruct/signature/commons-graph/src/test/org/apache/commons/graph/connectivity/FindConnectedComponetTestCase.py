from __future__ import annotations
import re
import typing
from typing import *
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

        with pytest.raises(TypeError):
            findConnectedComponent(
                None
            ).includingAllVertices().applyingMinimumSpanningTreeAlgorithm()

    def testVerifyNullVerticesGraph(self) -> None:

        class GraphConnection(AbstractGraphConnection):
            def connect0(self):
                self.addVertex(BaseLabeledVertex("B"))
                self.addVertex(BaseLabeledVertex("C"))

        graph = CommonsGraph.newUndirectedMutableGraph(GraphConnection())
        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )
        assert c is not None
        assert len(c) == 0

    def testVerifyEmptyGraph(self) -> None:

        graph = UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge]()

        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingAllVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )

        assert c is not None
        assert len(c) == 0

    def testVerifyConnectedComponentsIncludingVertices2(self) -> None:

        a = BaseLabeledVertex("A")
        e = BaseLabeledVertex("E")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: None,
                lambda: [
                    a,
                    BaseLabeledVertex("B"),
                    BaseLabeledVertex("C"),
                    BaseLabeledVertex("D"),
                    e,
                    BaseLabeledVertex("F"),
                    BaseLabeledVertex("G"),
                    BaseLabeledVertex("H"),
                ],
            )
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

        pass  # LLM could not translate this method

    def testVerifyConnectedComponents3(self) -> None:

        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: None,
                lambda v: v,
                lambda e: e,
                lambda e, f, t: e.from_(f).to(t),
                lambda: [a, BaseLabeledVertex("B"), BaseLabeledVertex("C")],
                lambda e, f, t: [
                    BaseLabeledEdge("A -> B"),
                    BaseLabeledEdge("B -> C"),
                    BaseLabeledEdge("C -> A"),
                ],
            )
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

        pass  # LLM could not translate this method

    def testVerifyConnectedComponents(self) -> None:

        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: None,
                lambda: [
                    a,
                    BaseLabeledVertex("B"),
                    BaseLabeledVertex("C"),
                    BaseLabeledVertex("D"),
                    BaseLabeledVertex("E"),
                    BaseLabeledVertex("F"),
                    BaseLabeledVertex("G"),
                    BaseLabeledVertex("H"),
                ],
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
