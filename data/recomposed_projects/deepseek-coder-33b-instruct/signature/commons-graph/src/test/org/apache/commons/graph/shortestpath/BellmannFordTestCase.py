from __future__ import annotations
import re
import typing
from typing import *
import unittest
import pytest
import pathlib
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *


class BellmannFordTestCase(unittest.TestCase):

    def testNullVertices(self) -> None:

        graph = UndirectedMutableGraph()

        with pytest.raises(NullPointerException):
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_vertex(None).applyingBelmannFord(DoubleWeightBaseOperations())

    def testNullMonoid(self) -> None:

        graph = None
        a = None
        try:
            graph = UndirectedMutableGraph()

            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.addVertex(a)
            graph.addVertex(b)
        except Exception as e:
            self.fail(str(e))

        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).from_(a).applyingBelmannFord(None)

    def testNullGraph(self) -> None:

        with pytest.raises(TypeError):
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None).applyingBelmannFord(DoubleWeightBaseOperations())

    def testNotConnectGraph(self) -> None:

        a = None
        b = None
        allVertexPairsShortestPath = None
        try:
            graph = UndirectedMutableGraph()

            a = BaseLabeledVertex("a")
            b = BaseLabeledVertex("b")
            graph.addVertex(a)
            graph.addVertex(b)

            allVertexPairsShortestPath = (
                CommonsGraph.findShortestPath(graph)
                .whereEdgesHaveWeights(BaseLabeledWeightedEdge())
                .from_(a)
                .applyingBelmannFord(DoubleWeightBaseOperations())
            )
        except PathNotFoundException as e:
            self.fail(e.getMessage())
        allVertexPairsShortestPath.findShortestPath(a, b)

    def testFindShortestPathAndVerify(self) -> None:

        pass  # LLM could not translate this method
