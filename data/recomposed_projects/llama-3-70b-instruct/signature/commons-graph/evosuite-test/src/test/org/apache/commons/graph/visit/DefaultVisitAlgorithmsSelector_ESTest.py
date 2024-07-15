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
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.visit.BaseGraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector import *

# from src.test.org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultVisitAlgorithmsSelector_ESTest(unittest.TestCase):

    def test11(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        reverted_graph0 = RevertedGraph(directed_mutable_graph0)
        default_visit_algorithms_selector0 = DefaultVisitAlgorithmsSelector(
            reverted_graph0, reverted_graph0
        )

        try:
            default_visit_algorithms_selector0.applyingDepthFirstSearch0()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector", e
            )

    def test10(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        reverted_graph0 = RevertedGraph(directed_mutable_graph0)
        default_visit_algorithms_selector0 = DefaultVisitAlgorithmsSelector(
            reverted_graph0, reverted_graph0
        )

        try:
            default_visit_algorithms_selector0.applying_breadth_first_search0()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector", e
            )

    def test09(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        reverted_graph0 = RevertedGraph(directed_mutable_graph0)
        directed_mutable_graph0.add_vertex(reverted_graph0)
        default_visit_algorithms_selector0 = DefaultVisitAlgorithmsSelector(
            reverted_graph0, reverted_graph0
        )
        graph0 = default_visit_algorithms_selector0.applying_breadth_first_search0()
        self.assertIsNotNone(graph0)

    def test08(self) -> None:

        comparable0 = unittest.mock.Mock(spec=Comparable)
        comparable0.configure_mock(**{"__str__.return_value": None})
        inMemoryPath0 = InMemoryPath(comparable0, comparable0)
        comparable1 = unittest.mock.Mock(spec=Comparable)
        comparable1.configure_mock(**{"__str__.return_value": None})
        defaultVisitAlgorithmsSelector0 = DefaultVisitAlgorithmsSelector(
            inMemoryPath0, comparable1
        )
        baseGraphVisitHandler0 = BaseGraphVisitHandler()

        with pytest.raises(ValueError):
            defaultVisitAlgorithmsSelector0.applyingBreadthFirstSearch1(
                baseGraphVisitHandler0
            )
            self.fail("Expecting exception: ValueError")

    def test07(self) -> None:

        baseGraphVisitHandler0 = BaseGraphVisitHandler()
        directedMutableGraph0 = DirectedMutableGraph()
        defaultVisitAlgorithmsSelector0 = DefaultVisitAlgorithmsSelector(
            directedMutableGraph0, directedMutableGraph0
        )

        try:
            defaultVisitAlgorithmsSelector0.applyingBreadthFirstSearch1(
                baseGraphVisitHandler0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector", e
            )

    def test06(self) -> None:

        undirected_mutable_graph0 = UndirectedMutableGraph()
        object0 = object()
        default_visit_algorithms_selector0 = DefaultVisitAlgorithmsSelector(
            undirected_mutable_graph0, object0
        )
        base_graph_visit_handler0 = BaseGraphVisitHandler()

        try:
            default_visit_algorithms_selector0.applying_breadth_first_search1(
                base_graph_visit_handler0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verify_exception("org.apache.commons.graph.model.BaseGraph", e)

    def test05(self) -> None:

        object0 = object()
        inMemoryPath0 = InMemoryPath(object0, object0)
        defaultVisitAlgorithmsSelector0 = DefaultVisitAlgorithmsSelector(
            inMemoryPath0, inMemoryPath0
        )
        baseGraphVisitHandler0 = BaseGraphVisitHandler()

        try:
            defaultVisitAlgorithmsSelector0.applyingDepthFirstSearch1(
                baseGraphVisitHandler0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Impossible to get the degree of input vertex; InMemoryPath [vertices=[], edges=[]] not contained in this path
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test04(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        defaultVisitAlgorithmsSelector0 = DefaultVisitAlgorithmsSelector(
            directedMutableGraph0, directedMutableGraph0
        )

        try:
            defaultVisitAlgorithmsSelector0.applyingDepthFirstSearch1(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test03(self) -> None:

        undirected_mutable_graph0 = UndirectedMutableGraph()
        integer0 = int(None)
        default_visit_algorithms_selector0 = DefaultVisitAlgorithmsSelector(
            undirected_mutable_graph0, integer0
        )
        base_graph_visit_handler0 = BaseGraphVisitHandler()

        try:
            default_visit_algorithms_selector0.applying_depth_first_search1(
                base_graph_visit_handler0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verify_exception("org.apache.commons.graph.model.BaseGraph", e)

    def test02(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        directedMutableGraph0.addVertex(revertedGraph0)
        defaultVisitAlgorithmsSelector0 = DefaultVisitAlgorithmsSelector(
            revertedGraph0, revertedGraph0
        )
        baseGraphVisitHandler0 = BaseGraphVisitHandler()
        vertexPair0 = defaultVisitAlgorithmsSelector0.applyingBreadthFirstSearch1(
            baseGraphVisitHandler0
        )
        self.assertIsNone(vertexPair0)

    def test01(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        reverted_graph0 = RevertedGraph(directed_mutable_graph0)
        directed_mutable_graph0.add_vertex(reverted_graph0)
        default_visit_algorithms_selector0 = DefaultVisitAlgorithmsSelector(
            reverted_graph0, reverted_graph0
        )
        graph0 = default_visit_algorithms_selector0.applying_depth_first_search0()
        self.assertIsNotNone(graph0)

    def test00(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        defaultVisitAlgorithmsSelector0 = DefaultVisitAlgorithmsSelector(
            directedMutableGraph0, directedMutableGraph0
        )
        baseGraphVisitHandler0 = BaseGraphVisitHandler()
        integer0 = Integer(-1809)
        directedMutableGraph1 = DirectedMutableGraph()
        directedMutableGraph2 = mock(DirectedMutableGraph, ViolatedAssumptionAnswer())
        doReturn(None).when(directedMutableGraph2).getOutbound(anyInt())
        defaultVisitAlgorithmsSelector1 = DefaultVisitAlgorithmsSelector(
            directedMutableGraph2, integer0
        )
        baseGraphVisitHandler1 = BaseGraphVisitHandler()

        try:
            defaultVisitAlgorithmsSelector1.applyingDepthFirstSearch1(
                baseGraphVisitHandler1
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.visit.DefaultVisitAlgorithmsSelector", e
            )
