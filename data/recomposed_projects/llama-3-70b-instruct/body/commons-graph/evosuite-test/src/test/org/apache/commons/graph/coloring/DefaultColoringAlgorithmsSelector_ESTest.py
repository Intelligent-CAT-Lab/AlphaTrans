from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector import *

# from src.test.org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.Monoid import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class DefaultColoringAlgorithmsSelector_ESTest(unittest.TestCase):

    def test14(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        linkedHashSet0 = set()
        defaultColoringAlgorithmsSelector0 = DefaultColoringAlgorithmsSelector(
            undirectedMutableGraph0, linkedHashSet0
        )
        coloredVertices0 = (
            defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0()
        )
        self.assertEqual(0, coloredVertices0.getRequiredColors())

    def test13(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        linkedHashSet0 = set()
        integer0 = -1862
        linkedHashSet0.add(integer0)
        undirectedMutableGraph0.addVertex(integer0)
        defaultColoringAlgorithmsSelector0 = DefaultColoringAlgorithmsSelector(
            undirectedMutableGraph0, linkedHashSet0
        )
        coloredVertices0 = (
            defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0()
        )
        coloredVertices1 = (
            defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm1(
                coloredVertices0
            )
        )
        self.assertEqual(1, coloredVertices1.getRequiredColors())

    def test12(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        linkedHashSet0 = set()
        defaultColoringAlgorithmsSelector0 = DefaultColoringAlgorithmsSelector(
            undirectedMutableGraph0, linkedHashSet0
        )
        coloredVertices0 = defaultColoringAlgorithmsSelector0.applyingGreedyAlgorithm()
        self.assertEqual(0, coloredVertices0.getRequiredColors())

    def test11(self) -> None:

        undirected_mutable_graph0 = UndirectedMutableGraph()
        linked_hash_set0 = set()
        integer0 = -1862
        undirected_mutable_graph0.add_vertex(integer0)
        default_coloring_algorithms_selector0 = DefaultColoringAlgorithmsSelector(
            undirected_mutable_graph0, linked_hash_set0
        )

        try:
            default_coloring_algorithms_selector0.applying_greedy_algorithm()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verify_exception(
                "org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e
            )

    def test10(self) -> None:

        undirected_mutable_graph0 = UndirectedMutableGraph()
        linked_hash_set0 = set()
        integer0 = -1862
        linked_hash_set0.add(None)
        undirected_mutable_graph0.add_vertex(integer0)
        default_coloring_algorithms_selector0 = DefaultColoringAlgorithmsSelector(
            undirected_mutable_graph0, linked_hash_set0
        )
        colored_vertices0 = (
            default_coloring_algorithms_selector0.applying_back_tracking_algorithm0()
        )
        self.assertEqual(1, colored_vertices0.get_required_colors())

    def test09(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integer0 = Integer(340)
        undirectedMutableGraph0.addVertex(integer0)
        linkedHashSet0 = LinkedHashSet()
        integer1 = Integer(1)
        undirectedMutableGraph0.addVertex(integer1)
        coloredVertices0 = ColoredVertices()
        undirectedMutableGraph0.addEdge(integer0, coloredVertices0, integer1)
        linkedHashSet0.add(integer1)
        defaultColoringAlgorithmsSelector0 = DefaultColoringAlgorithmsSelector(
            undirectedMutableGraph0, linkedHashSet0
        )

        try:
            defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e
            )

    def test08(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integer0 = Integer(-212)
        undirectedMutableGraph0.addVertex(integer0)
        linkedHashSet0 = LinkedHashSet()
        defaultColoringAlgorithmsSelector0 = DefaultColoringAlgorithmsSelector(
            undirectedMutableGraph0, linkedHashSet0
        )
        coloredVertices0 = ColoredVertices()

        with pytest.raises(RuntimeError):
            defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm1(
                coloredVertices0
            )
            verifyException(
                "org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector",
                RuntimeError,
            )

    def test07(self) -> None:

        linkedHashSet0 = set()
        defaultColoringAlgorithmsSelector0 = DefaultColoringAlgorithmsSelector(
            None, linkedHashSet0
        )

        with pytest.raises(RuntimeError):
            defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0()
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e
        )

    def test06(self) -> None:

        monoid0 = unittest.mock.Mock(spec=Monoid)
        monoid0.identity.return_value = None

        mapper0 = unittest.mock.Mock(spec=Mapper)

        mutableSpanningTree0 = MutableSpanningTree(monoid0, mapper0)

        linkedHashSet0 = set()
        mutableSpanningTree0.addVertex(linkedHashSet0)

        comparable0 = unittest.mock.Mock(spec=Comparable)
        comparable0.toString.return_value = None
        linkedHashSet0.add(comparable0)

        defaultColoringAlgorithmsSelector0 = DefaultColoringAlgorithmsSelector(
            mutableSpanningTree0, linkedHashSet0
        )

        with pytest.raises(RuntimeError):
            defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0()

        assert "org.apache.commons.graph.model.BaseGraph" in str(e.value)

    def test05(self) -> None:

        undirected_mutable_graph0 = UndirectedMutableGraph()
        linked_hash_set0 = set()
        default_coloring_algorithms_selector0 = DefaultColoringAlgorithmsSelector(
            undirected_mutable_graph0, linked_hash_set0
        )

        with pytest.raises(RuntimeError):
            default_coloring_algorithms_selector0.applyingBackTrackingAlgorithm1(None)
            assert False, "Expecting exception: RuntimeError"

    def test04(self) -> None:

        linkedHashSet0 = set()
        defaultColoringAlgorithmsSelector0 = DefaultColoringAlgorithmsSelector(
            None, linkedHashSet0
        )
        coloredVertices0 = ColoredVertices()

        with pytest.raises(RuntimeError):
            defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm1(
                coloredVertices0
            )
            self.fail("Expecting exception: RuntimeError")

        self.verifyException(
            "org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e
        )

    def test02(self) -> None:

        linkedHashSet0 = set()
        monoid0 = Mock(Monoid)
        monoid0.identity.return_value = None
        mapper0 = Mock(Mapper)
        mutableSpanningTree0 = MutableSpanningTree(monoid0, mapper0)
        defaultColoringAlgorithmsSelector0 = DefaultColoringAlgorithmsSelector(
            mutableSpanningTree0, linkedHashSet0
        )
        coloredVertices0 = ColoredVertices()
        coloredVertices1 = (
            defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm1(
                coloredVertices0
            )
        )
        self.assertIs(coloredVertices1, coloredVertices0)

    def test01(self) -> None:

        undirected_mutable_graph0 = UndirectedMutableGraph()
        integer0 = Integer(-212)
        undirected_mutable_graph0.add_vertex(integer0)
        linked_hash_set0 = LinkedHashSet()
        integer1 = Integer(-1246)
        linked_hash_set0.add(integer1)
        integer2 = Integer(-3954)
        undirected_mutable_graph0.add_vertex(integer2)
        default_coloring_algorithms_selector0 = DefaultColoringAlgorithmsSelector(
            undirected_mutable_graph0, linked_hash_set0
        )
        colored_vertices0 = (
            default_coloring_algorithms_selector0.applying_greedy_algorithm()
        )
        self.assertEqual(1, colored_vertices0.get_required_colors())

    def test00(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        linkedHashSet0 = set()
        integer0 = Integer(2238)
        undirectedMutableGraph0.addVertex(integer0)
        coloredVertices0 = ColoredVertices()
        integer1 = Integer(2238)
        undirectedMutableGraph0.addEdge(integer0, coloredVertices0, integer1)
        linkedHashSet0.add(integer0)
        defaultColoringAlgorithmsSelector0 = DefaultColoringAlgorithmsSelector(
            undirectedMutableGraph0, linkedHashSet0
        )

        try:
            defaultColoringAlgorithmsSelector0.applyingBackTrackingAlgorithm0()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector", e
            )
