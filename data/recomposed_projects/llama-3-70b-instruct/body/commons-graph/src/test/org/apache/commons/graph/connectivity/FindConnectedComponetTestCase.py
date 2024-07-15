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
        with self.assertRaises(RuntimeError):
            CommonsGraph.findConnectedComponent(
                None
            ).includingAllVertices().applyingMinimumSpanningTreeAlgorithm()

    def testVerifyNullVerticesGraph(self) -> None:
        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge]().connect0(
                lambda: [
                    graph.addVertex(BaseLabeledVertex("B")),
                    graph.addVertex(BaseLabeledVertex("C")),
                ]
            )
        )
        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )
        self.assertIsNotNone(c)
        self.assertEqual(0, len(c))

    def testVerifyEmptyGraph(self) -> None:
        graph: UndirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            UndirectedMutableGraph()
        )
        c: Collection[List[BaseLabeledVertex]] = (
            CommonsGraph.findConnectedComponent(graph)
            .includingAllVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )
        self.assertIsNotNone(c)
        self.assertEqual(0, c.size())

    def testVerifyConnectedComponentsIncludingVertices2(self) -> None:
        a = BaseLabeledVertex("A")
        e = BaseLabeledVertex("E")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge]().connect0(
                lambda: [
                    graph.addVertex(a),
                    graph.addVertex(BaseLabeledVertex("B")),
                    graph.addVertex(BaseLabeledVertex("C")),
                    graph.addVertex(BaseLabeledVertex("D")),
                    graph.addVertex(e),
                    graph.addVertex(BaseLabeledVertex("F")),
                    graph.addVertex(BaseLabeledVertex("G")),
                    graph.addVertex(BaseLabeledVertex("H")),
                ]
            )
        )

        coll = (
            CommonsGraph.findConnectedComponent(graph)
            .includingVertices(a, e)
            .applyingMinimumSpanningTreeAlgorithm()
        )

        self.assertIsNotNone(coll)
        self.assertFalse(coll.isEmpty())
        self.assertEqual(2, coll.size())

    def testVerifyConnectedComponentsIncludingVertices(self) -> None:

        pass  # LLM could not translate this method

    def testVerifyConnectedComponents3(self) -> None:

        pass  # LLM could not translate this method

    def testVerifyConnectedComponents2(self) -> None:

        pass  # LLM could not translate this method

    def testVerifyConnectedComponents(self) -> None:
        a = BaseLabeledVertex("A")

        graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge]().connect0(
                lambda: [
                    graph.addVertex(a),
                    graph.addVertex(BaseLabeledVertex("B")),
                    graph.addVertex(BaseLabeledVertex("C")),
                    graph.addVertex(BaseLabeledVertex("D")),
                    graph.addVertex(BaseLabeledVertex("E")),
                    graph.addVertex(BaseLabeledVertex("F")),
                    graph.addVertex(BaseLabeledVertex("G")),
                    graph.addVertex(BaseLabeledVertex("H")),
                ]
            )
        )

        c = (
            CommonsGraph.findConnectedComponent(graph)
            .includingAllVertices()
            .applyingMinimumSpanningTreeAlgorithm()
        )

        self.assertIsNotNone(c)
        self.assertFalse(c.isEmpty())
        self.assertEqual(8, c.size())
