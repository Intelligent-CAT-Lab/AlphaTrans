from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *

# from src.test.org.apache.commons.graph.model.RevertedGraph_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class RevertedGraph_ESTest(unittest.TestCase):

    def test23(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        directed_mutable_graph1 = DirectedMutableGraph()
        reverted_graph0 = RevertedGraph(directed_mutable_graph1)
        reverted_graph1 = RevertedGraph(directed_mutable_graph0)

        try:
            reverted_graph1.get_degree(reverted_graph0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e)

    def test22(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        revertedGraph0 = RevertedGraph[int, int](directedMutableGraph0)
        boolean0 = revertedGraph0.containsEdge(None)
        self.assertFalse(boolean0)

    def test21(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        directed_mutable_graph1 = DirectedMutableGraph()
        reverted_graph0 = RevertedGraph(directed_mutable_graph1)
        reverted_graph1 = RevertedGraph(directed_mutable_graph0)

        try:
            reverted_graph1.getOutDegree(reverted_graph0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e)

    def test20(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[
            RevertedGraph[Integer, Integer], RevertedGraph[Integer, Integer]
        ]()
        directedMutableGraph1 = DirectedMutableGraph[Integer, Integer]()
        revertedGraph0 = RevertedGraph[Integer, Integer](directedMutableGraph1)
        revertedGraph1 = RevertedGraph[
            RevertedGraph[Integer, Integer], RevertedGraph[Integer, Integer]
        ](directedMutableGraph0)
        iterable0 = revertedGraph1.getInbound(revertedGraph0)
        self.assertIsNone(iterable0)

    def test19(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        revertedGraph0 = RevertedGraph[int, int](directedMutableGraph0)
        int0 = revertedGraph0.getSize()
        self.assertEqual(0, int0)

    def test18(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        revertedGraph0 = RevertedGraph[int, int](directedMutableGraph0)
        iterable0 = revertedGraph0.getEdges()
        assert iterable0 is not None

    def test17(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        directedMutableGraph1 = DirectedMutableGraph()
        revertedGraph1 = RevertedGraph(directedMutableGraph1)

        # Undeclared exception in Python is replaced with a try-except block
        try:
            revertedGraph0.getConnectedVertices(revertedGraph1)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            # verifyException("org.apache.commons.graph.model.BaseGraph", e)
            # In Python, we can use assert to verify the exception
            assert isinstance(e, RuntimeError), "Expecting exception: RuntimeError"

    def test16(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        iterable0 = revertedGraph0.getVertices0()
        assert iterable0 is not None

    def test15(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        integer0 = 2

        with self.assertRaises(RuntimeError):
            revertedGraph0.getVertices1(integer0)

    def test14(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph[
            RevertedGraph[Integer, Integer], Integer
        ]()
        directed_mutable_graph1 = DirectedMutableGraph[Integer, Integer]()
        reverted_graph0 = RevertedGraph[Integer, Integer](directed_mutable_graph1)
        reverted_graph1 = RevertedGraph[RevertedGraph[Integer, Integer], Integer](
            directed_mutable_graph0
        )
        boolean0 = reverted_graph1.contains_vertex(reverted_graph0)
        self.assertFalse(boolean0)

    def test13(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        directed_mutable_graph1 = DirectedMutableGraph()
        reverted_graph0 = RevertedGraph(directed_mutable_graph1)
        reverted_graph1 = RevertedGraph(directed_mutable_graph0)

        try:
            reverted_graph1.get_in_degree(reverted_graph0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.DirectedMutableGraph", e)

    def test12(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = int(0)
        revertedGraph0 = RevertedGraph[int, int](directedMutableGraph0)
        iterable0 = revertedGraph0.getOutbound(integer0)
        self.assertIsNone(iterable0)

    def test11(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        int0 = revertedGraph0.getOrder()
        self.assertEqual(0, int0)

    def test10(self) -> None:

        reverted_graph0 = None
        try:
            reverted_graph0 = RevertedGraph(DirectedGraph(None))
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Adapted DirectedGraph must be not null
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test09(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph1 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph1)
        directedMutableGraph0.addVertex(revertedGraph0)
        revertedGraph1 = RevertedGraph(directedMutableGraph0)
        boolean0 = revertedGraph1.containsVertex(revertedGraph0)
        self.assertTrue(boolean0)

    def test08(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph1 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph1)
        directedMutableGraph0.addVertex(revertedGraph0)
        revertedGraph1 = RevertedGraph(directedMutableGraph0)
        int0 = revertedGraph1.getDegree(revertedGraph0)
        self.assertEqual(0, int0)

    def test07(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        revertedGraph0 = RevertedGraph[int, int](directedMutableGraph0)
        directedMutableGraph1 = DirectedMutableGraph[
            RevertedGraph[int, int], RevertedGraph[int, int]
        ]()
        directedMutableGraph1.addVertex(revertedGraph0)
        directedMutableGraph1.addEdge(revertedGraph0, revertedGraph0, revertedGraph0)
        revertedGraph1 = RevertedGraph[
            RevertedGraph[int, int], RevertedGraph[int, int]
        ](directedMutableGraph1)
        revertedGraph2 = revertedGraph1.getEdge(revertedGraph0, revertedGraph0)
        self.assertIs(revertedGraph0, revertedGraph2)

    def test06(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph1 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph1)
        directedMutableGraph0.addVertex(revertedGraph0)
        revertedGraph1 = RevertedGraph(directedMutableGraph0)
        integer0 = revertedGraph1.getEdge(revertedGraph0, revertedGraph0)
        self.assertIsNone(integer0)

    def test05(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph1 = DirectedMutableGraph()
        integer0 = Integer(1)
        revertedGraph0 = RevertedGraph(directedMutableGraph1)
        directedMutableGraph0.addVertex(revertedGraph0)
        revertedGraph1 = RevertedGraph(directedMutableGraph0)
        directedMutableGraph0.addEdge(revertedGraph0, integer0, revertedGraph0)
        int0 = revertedGraph1.getInDegree(revertedGraph0)
        self.assertEqual(1, int0)

    def test04(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph1 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph1)
        directedMutableGraph0.addVertex(revertedGraph0)
        revertedGraph1 = RevertedGraph(directedMutableGraph0)
        int0 = revertedGraph1.getInDegree(revertedGraph0)
        self.assertEqual(0, int0)

    def test03(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph1 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph1)
        directedMutableGraph0.addVertex(revertedGraph0)
        revertedGraph1 = RevertedGraph(directedMutableGraph0)
        int0 = revertedGraph1.getOrder()
        self.assertEqual(1, int0)

    def test02(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph1 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph1)
        directedMutableGraph0.decorateAddVertex(revertedGraph0)
        revertedGraph1 = RevertedGraph(directedMutableGraph0)
        int0 = revertedGraph1.getOutDegree(revertedGraph0)
        self.assertEqual(0, int0)

    def test01(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph1 = DirectedMutableGraph()
        integer0 = 1
        revertedGraph0 = RevertedGraph(directedMutableGraph1)
        directedMutableGraph0.addVertex(revertedGraph0)
        revertedGraph1 = RevertedGraph(directedMutableGraph0)
        directedMutableGraph0.addEdge(revertedGraph0, integer0, revertedGraph0)
        int0 = revertedGraph1.getSize()
        self.assertEqual(1, int0)

    def test00(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        revertedGraph0 = RevertedGraph[int, int](directedMutableGraph0)
        directedMutableGraph1 = DirectedMutableGraph[
            RevertedGraph[int, int], RevertedGraph[int, int]
        ]()
        revertedGraph1 = RevertedGraph[
            RevertedGraph[int, int], RevertedGraph[int, int]
        ](directedMutableGraph1)
        revertedGraph2 = RevertedGraph[int, int](revertedGraph0)

        try:
            revertedGraph1.getEdge(revertedGraph0, revertedGraph2)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.BaseGraph", e)
