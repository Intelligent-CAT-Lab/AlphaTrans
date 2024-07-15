from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest

# from src.test.org.apache.commons.graph.model.BaseMutableGraph_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BaseMutableGraph_ESTest(unittest.TestCase):

    def test21(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph1 = DirectedMutableGraph()
        integer0 = 2595

        with self.assertRaises(RuntimeError):
            directedMutableGraph1.internalRemoveEdge(
                directedMutableGraph0, integer0, directedMutableGraph0
            )

    def test20(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()

        try:
            directedMutableGraph0.addEdge(None, None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test19(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = int(161)

        try:
            directedMutableGraph0.addEdge(integer0, None, integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test18(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph[int, int]()
        integer0 = -2

        with pytest.raises(RuntimeError):
            directed_mutable_graph0.add_edge(integer0, integer0, None)

    def test17(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = -1836
        directedMutableGraph0.addVertex(integer0)
        directedMutableGraph0.addEdge(integer0, integer0, integer0)

        # Undeclared exception in Java code, so we'll use a try-except block to catch the exception
        try:
            directedMutableGraph0.addEdge(integer0, integer0, integer0)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test16(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()

        try:
            directedMutableGraph0.addVertex(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test15(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = -418
        directedMutableGraph0.add_vertex(integer0)

        with pytest.raises(RuntimeError):
            directedMutableGraph0.add_vertex(integer0)

    def test14(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = -418
        directedMutableGraph0.addVertex(integer0)
        directedMutableGraph0.addEdge(integer0, integer0, integer0)
        integer1 = -418
        directedMutableGraph0.addEdge(integer1, integer1, integer1)
        self.assertEqual(1, directedMutableGraph0.getOrder())

    def test13(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()

        try:
            directedMutableGraph0.remove_edge(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test12(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph[int, int]()
        integer0 = int(3)

        try:
            directed_mutable_graph0.remove_edge(integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verify_exception("org.apache.commons.graph.model.BaseGraph", e)

    def test11(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()

        with pytest.raises(RuntimeError) as excinfo:
            directed_mutable_graph0.remove_vertex(None)

        assert str(excinfo.value) == "Expecting exception: RuntimeError"
        # verifyException("org.apache.commons.graph.model.BaseGraph", excinfo.value)

    def test10(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph[int, int]()
        integer0 = -418

        try:
            directed_mutable_graph0.remove_vertex(integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verify_exception("org.apache.commons.graph.model.BaseGraph", e)

    def test09(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = -2142346125
        directedMutableGraph0.addVertex(integer0)
        directedMutableGraph0.decorateRemoveVertex(integer0)

        # Undeclared exception handling
        try:
            directedMutableGraph0.addEdge(integer0, integer0, integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.graph.model.DirectedMutableGraph", e
            )

    def test08(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = int(0)
        directedMutableGraph0.addVertex(integer0)

        try:
            directedMutableGraph0.internalAddEdge(integer0, None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test07(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()

        with self.assertRaises(RuntimeError):
            undirectedMutableGraph0.internalAddEdge(None, None, None)

        verifyException("org.apache.commons.graph.model.BaseMutableGraph", RuntimeError)

    def test06(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()

        with pytest.raises(RuntimeError):
            directedMutableGraph0.internalRemoveEdge(None, None, None)

        # Impossible to construct a Vertex with a null head
        verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test05(self) -> None:

        linkedHashSet0 = set()
        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph0.addVertex(linkedHashSet0)
        directedMutableGraph0.internalRemoveEdge(
            linkedHashSet0, linkedHashSet0, linkedHashSet0
        )
        assert linkedHashSet0 == set()

    def test04(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = -437
        integer1 = -437

        try:
            directedMutableGraph0.add_edge(integer0, integer1, integer1)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verify_exception("org.apache.commons.graph.model.BaseGraph", e)

    def test03(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = -437
        directedMutableGraph0.addVertex(integer0)
        integer1 = -437
        directedMutableGraph0.addEdge(integer0, integer1, integer1)
        self.assertEqual(1, directedMutableGraph0.getOrder())

    def test02(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = -1836
        directedMutableGraph0.addVertex(integer0)
        integer1 = -1836
        directedMutableGraph0.addEdge(integer0, integer1, integer0)
        self.assertEqual(1, directedMutableGraph0.getSize())

    def test01(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = int(3)
        directedMutableGraph0.addVertex(integer0)
        integer1 = int(3)
        directedMutableGraph0.internalAddEdge(integer1, integer0, integer0)
        directedMutableGraph0.removeEdge(integer0)
        self.assertEqual(0, directedMutableGraph0.getSize())

    def test00(self) -> None:

        linkedHashSet0 = set()
        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph0.addVertex(linkedHashSet0)
        directedMutableGraph0.addEdge(linkedHashSet0, linkedHashSet0, linkedHashSet0)
        linkedHashSet1 = set()
        directedMutableGraph0.removeVertex(linkedHashSet1)
        self.assertEqual(0, len(linkedHashSet1))
