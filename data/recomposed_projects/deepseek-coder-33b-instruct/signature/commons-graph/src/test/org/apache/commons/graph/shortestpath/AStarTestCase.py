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
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.Heuristic import *
from src.main.org.apache.commons.graph.shortestpath.HeuristicBuilder import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *


class AStarTestCase(unittest.TestCase):

    def testNullVertices(self) -> None:

        graph = UndirectedMutableGraph()

        with pytest.raises(RuntimeError):
            findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_vertex(None).to_vertex(None).applyingAStar(
                DoubleWeightBaseOperations()
            ).withHeuristic(
                None
            )

    def testNullMonoid(self) -> None:

        graph = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        heuristics = {}
        heuristic = None

        try:
            graph.addVertex(a)
            graph.addVertex(b)

            heuristic = Heuristic(lambda current, goal: heuristics.get(current))

        except RuntimeError as e:
            self.fail(e.getMessage())

        CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
            BaseWeightedEdge()
        ).from_(a).to(b).applyingAStar(None).withHeuristic(heuristic)

    def testNullHeuristic(self) -> None:

        graph = UndirectedMutableGraph()

        with pytest.raises(RuntimeError):
            findShortestPath(graph).whereEdgesHaveWeights(BaseWeightedEdge()).from_(
                BaseLabeledVertex("a")
            ).to_(BaseLabeledVertex("b")).applyingAStar(
                DoubleWeightBaseOperations()
            ).withHeuristic(
                None
            )

    def testNullGraph(self) -> None:

        with pytest.raises(TypeError):
            CommonsGraph.findShortestPath(None).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(None).to_(None).applyingAStar(
                DoubleWeightBaseOperations()
            ).withHeuristic(
                None
            )

    def testNotConnectGraph(self) -> None:

        graph = UndirectedMutableGraph()

        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        graph.addVertex(a)
        graph.addVertex(b)

        heuristics = {}

        def heuristic(current, goal):
            return heuristics.get(current)

        try:
            CommonsGraph.findShortestPath(graph).whereEdgesHaveWeights(
                BaseWeightedEdge()
            ).from_(a).to(b).applyingAStar(DoubleWeightBaseOperations()).withHeuristic(
                heuristic
            )
        except PathNotFoundException:
            pass

    def testFindShortestPathAndVerify(self) -> None:

        pass  # LLM could not translate this method
