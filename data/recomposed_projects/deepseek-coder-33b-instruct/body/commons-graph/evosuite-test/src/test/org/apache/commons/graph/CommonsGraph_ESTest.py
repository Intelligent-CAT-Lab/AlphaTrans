from __future__ import annotations
import time
import re
import mock
import os
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *

# from src.test.org.apache.commons.graph.CommonsGraph_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.SynchronizedDirectedGraph import *
from src.main.org.apache.commons.graph.SynchronizedMutableGraph import *
from src.main.org.apache.commons.graph.SynchronizedUndirectedGraph import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.builder.LinkedConnectionBuilder import *
from src.main.org.apache.commons.graph.coloring.ColorsBuilder import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityBuilder import *
from src.main.org.apache.commons.graph.elo.RankingSelector import *
from src.main.org.apache.commons.graph.export.NamedExportSelector import *
from src.main.org.apache.commons.graph.flow.FlowWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class CommonsGraph_ESTest(unittest.TestCase):

    def test24(self) -> None:

        try:
            CommonsGraph.newDirectedMutableGraph(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "org.apache.commons.graph.utils.Assertions")

    def test23(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        synchronizedMutableGraph0 = SynchronizedMutableGraph(directedMutableGraph0)
        pathWeightedEdgesBuilder0 = CommonsGraph.findShortestPath(
            synchronizedMutableGraph0
        )
        self.assertIsNotNone(pathWeightedEdgesBuilder0)

    def test22(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        rankingSelector0 = CommonsGraph.eloRate(directedMutableGraph0)
        self.assertIsNotNone(rankingSelector0)

    def test21(self) -> None:

        try:
            CommonsGraph.findMaxFlow(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Max flow can not be calculated on null graph
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test20(self) -> None:

        try:
            CommonsGraph.coloring(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test19(self) -> None:

        try:
            CommonsGraph.findConnectedComponent(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Connected Component cannot be calculated from a null graph
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test18(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        graph0 = CommonsGraph.synchronize1(directed_mutable_graph0)
        self.assertEqual(0, graph0.getOrder())

    def test17(self) -> None:

        try:
            CommonsGraph.minimumSpanningTree(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Minimum spanning tree can not be calculated on null graph
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test16(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        graph0 = CommonsGraph.synchronize0(directed_mutable_graph0)
        self.assertEqual(0, graph0.get_size())

    def test15(self) -> None:

        try:
            CommonsGraph.export(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test14(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        synchronized_directed_graph0 = SynchronizedDirectedGraph(
            directed_mutable_graph0
        )
        scc_algorithm_selector0 = CommonsGraph.findStronglyConnectedComponent(
            synchronized_directed_graph0
        )
        assert scc_algorithm_selector0 is not None

    def test13(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        graph0 = CommonsGraph.synchronize3(undirectedMutableGraph0)
        self.assertEqual(0, graph0.getOrder())

    def test12(self) -> None:

        try:
            CommonsGraph.visit(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test11(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        synchronized_mutable_graph0 = SynchronizedMutableGraph(directed_mutable_graph0)
        linked_connection_builder0 = CommonsGraph.populate(synchronized_mutable_graph0)
        assert linked_connection_builder0 is not None

    def test10(self) -> None:

        try:
            CommonsGraph.eloRate(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test09(self) -> None:

        try:
            CommonsGraph.findShortestPath(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Shortest path can not be calculated on null graph
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test08(self) -> None:

        try:
            CommonsGraph.findStronglyConnectedComponent(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Strongly Connected Component cannot be calculated from a null graph
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test07(self) -> None:

        try:
            CommonsGraph.newUndirectedMutableGraph(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test06(self) -> None:

        try:
            CommonsGraph.populate(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test05(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedMutableGraph0)
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(
            synchronizedDirectedGraph0
        )
        colorsBuilder0 = CommonsGraph.coloring(synchronizedUndirectedGraph0)
        assert colorsBuilder0 is not None

    def test04(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        named_export_selector0 = CommonsGraph.export(directed_mutable_graph0)
        self.assertIsNotNone(named_export_selector0)

    def test03(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        connectivity_builder0 = CommonsGraph.findConnectedComponent(
            directed_mutable_graph0
        )
        self.assertIsNotNone(connectivity_builder0)

    def test02(self) -> None:

        graphConnection0 = mock(GraphConnection, ViolatedAssumptionAnswer)
        directedMutableGraph0 = CommonsGraph.newDirectedMutableGraph(graphConnection0)
        object0 = Object()
        directedMutableGraph0.addVertex(object0)
        synchronizedDirectedGraph0 = SynchronizedDirectedGraph(directedMutableGraph0)
        graph0 = CommonsGraph.synchronize0(synchronizedDirectedGraph0)
        self.assertEqual(0, graph0.getSize())

    def test01(self) -> None:

        graphConnection0 = mock(GraphConnection, ViolatedAssumptionAnswer)
        directedMutableGraph0 = CommonsGraph.newDirectedMutableGraph(graphConnection0)
        object0 = Object()
        directedMutableGraph0.addVertex(object0)
        graph0 = CommonsGraph.synchronize1(directedMutableGraph0)
        self.assertEqual(1, graph0.getOrder())

    def test00(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        visit_source_selector0 = CommonsGraph.visit(directed_mutable_graph0)
        self.assertIsNotNone(visit_source_selector0)
