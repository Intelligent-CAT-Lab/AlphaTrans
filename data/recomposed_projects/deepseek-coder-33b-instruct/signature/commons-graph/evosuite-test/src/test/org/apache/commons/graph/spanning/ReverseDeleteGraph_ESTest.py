from __future__ import annotations
import time
import re
import mock
import os
import typing
from typing import *
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.spanning.ReverseDeleteGraph import *

# from src.test.org.apache.commons.graph.spanning.ReverseDeleteGraph_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class ReverseDeleteGraph_ESTest(unittest.TestCase):

    def test28(self) -> None:

        integer0 = Integer(-87)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        boolean0 = reverseDeleteGraph0.containsEdge(integer0)
        self.assertFalse(boolean0)

    def test27(self) -> None:

        integer0 = Integer(-87)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        boolean0 = reverseDeleteGraph0.containsVertex(integer0)
        self.assertFalse(boolean0)

    def test26(self) -> None:

        integer0 = Integer(-78)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        int0 = reverseDeleteGraph0.getSize()
        self.assertEqual(0, int0)

    def test25(self) -> None:

        linkedList0 = []
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = 1
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, mapper0
        )
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryWeightedPath0, linkedList0, linkedList0
        )

        with pytest.raises(RuntimeError):
            reverseDeleteGraph0.getDegree(integer0)
            verifyException(
                "org.apache.commons.graph.spanning.ReverseDeleteGraph", RuntimeError
            )

    def test24(self) -> None:

        integer0 = Integer(-87)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        int0 = reverseDeleteGraph0.getOrder()
        self.assertFalse(linkedList0.contains(int0))

    def test23(self) -> None:

        integer0 = IntegerWeightBaseOperations().identity()
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = []
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer1 = integerWeightBaseOperations0.identity()
        linkedList0.append(integer1)
        vertexPair0 = reverseDeleteGraph0.getVertices1(integer0)
        self.assertIsNone(vertexPair0)

    def test22(self) -> None:

        integer0 = Integer(-78)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        list0 = [integer0, integer0, integer0, integer0, integer0, integer0]
        reverseDeleteGraph0 = ReverseDeleteGraph(inMemoryPath0, linkedList0, list0)
        vertexPair0 = reverseDeleteGraph0.getVertices1(integer0)
        self.assertIsNone(vertexPair0)

    def test21(self) -> None:

        integer0 = Integer(-88)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        linkedList0.add(None)
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        integer1 = reverseDeleteGraph0.getEdge(integer0, integer0)
        self.assertIsNone(integer1)

    def test20(self) -> None:

        integer0 = Integer(-87)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        integer1 = reverseDeleteGraph0.getEdge(integer0, integer0)
        self.assertIsNone(integer1)

    def test19(self) -> None:

        linkedList0 = []
        reverseDeleteGraph0 = ReverseDeleteGraph(None, linkedList0, linkedList0)

        with self.assertRaises(RuntimeError):
            reverseDeleteGraph0.containsEdge(None)

    def test18(self) -> None:

        linkedList0 = LinkedList[int]()
        reverseDeleteGraph0 = ReverseDeleteGraph[int, int](
            None, linkedList0, linkedList0
        )
        integer0 = -55

        with pytest.raises(RuntimeError):
            reverseDeleteGraph0.containsVertex(integer0)
            verifyException(
                "org.apache.commons.graph.spanning.ReverseDeleteGraph", RuntimeError
            )

    def test17(self) -> None:

        integer0 = Integer(-1)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer1 = integerWeightBaseOperations0.inverse(integer0)

        # Undeclared exception in Java is translated to Python's unittest.TestCase.assertRaises
        with self.assertRaises(ValueError):
            reverseDeleteGraph0.getConnectedVertices(integer1)

    def test16(self) -> None:

        integer0 = Integer(-87)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )

        # Undeclared exception in Java code
        try:
            reverseDeleteGraph0.getConnectedVertices(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Impossible to get the degree of a null vertex
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test15(self) -> None:

        linkedList0 = []
        reverseDeleteGraph0 = ReverseDeleteGraph(None, linkedList0, linkedList0)

        with pytest.raises(RuntimeError):
            reverseDeleteGraph0.getConnectedVertices(None)

    def test14(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            directedMutableGraph0, linkedList0, linkedList0
        )

        with pytest.raises(RuntimeError):
            reverseDeleteGraph0.getConnectedVertices(None)

    def test13(self) -> None:

        integer0 = -110
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = []
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )

        # Undeclared exception in Java code
        try:
            reverseDeleteGraph0.getEdge(integer0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # Impossible to construct a Vertex with a null tail
            self.assertIsInstance(e, RuntimeError)

    def test12(self) -> None:

        linkedList0 = []
        reverseDeleteGraph0 = ReverseDeleteGraph(None, linkedList0, linkedList0)

        with pytest.raises(RuntimeError):
            reverseDeleteGraph0.getEdge(None, None)
            verifyException(
                "org.apache.commons.graph.spanning.ReverseDeleteGraph", RuntimeError
            )

    def test11(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        list0 = []
        reverseDeleteGraph0 = ReverseDeleteGraph(directedMutableGraph0, list0, list0)

        with pytest.raises(RuntimeError):
            reverseDeleteGraph0.getEdge(None, None)

    def test10(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        reverseDeleteGraph0 = ReverseDeleteGraph(undirectedMutableGraph0, None, None)

        try:
            reverseDeleteGraph0.getEdges()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("java.util.ArrayList", e)

    def test09(self) -> None:

        linkedList0 = []
        reverseDeleteGraph0 = ReverseDeleteGraph(None, linkedList0, linkedList0)

        with self.assertRaises(RuntimeError):
            reverseDeleteGraph0.getOrder()
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e)

    def test08(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        reverseDeleteGraph0 = ReverseDeleteGraph(undirectedMutableGraph0, None, None)

        try:
            reverseDeleteGraph0.getSize()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e)

    def test07(self) -> None:

        linkedList0 = []
        reverseDeleteGraph0 = ReverseDeleteGraph(None, linkedList0, linkedList0)

        with self.assertRaises(RuntimeError):
            reverseDeleteGraph0.getVertices0()
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.graph.spanning.ReverseDeleteGraph", e)

    def test06(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        reverseDeleteGraph0 = ReverseDeleteGraph(directedMutableGraph0, None, None)

        with pytest.raises(RuntimeError):
            reverseDeleteGraph0.getVertices1(None)
            verifyException(
                "org.apache.commons.graph.spanning.ReverseDeleteGraph", RuntimeError
            )

    def test05(self) -> None:

        integer0 = Integer(-87)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        inMemoryPath0.addConnectionInTail(integer0, integer0, integer0)
        boolean0 = reverseDeleteGraph0.containsEdge(integer0)
        self.assertTrue(boolean0)

    def test04(self) -> None:

        integer0 = Integer(-87)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        inMemoryPath0.addConnectionInTail(integer0, integer0, integer0)
        boolean0 = reverseDeleteGraph0.containsVertex(integer0)
        self.assertTrue(boolean0)

    def test03(self) -> None:

        integer0 = Integer(-87)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        inMemoryPath0.addConnectionInTail(integer0, integer0, integer0)
        int0 = reverseDeleteGraph0.getOrder()
        self.assertEqual(2, int0)

    def test02(self) -> None:

        integer0 = Integer(-87)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        linkedList0.add(integer0)
        int0 = reverseDeleteGraph0.getSize()
        self.assertEqual(2, int0)

    def test01(self) -> None:

        integer0 = Integer(-87)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        linkedList0.add(integer0)
        inMemoryPath0.addConnectionInTail(integer0, integer0, integer0)
        vertexPair0 = reverseDeleteGraph0.getVertices1(integer0)
        self.assertIsNotNone(vertexPair0)

    def test00(self) -> None:

        integer0 = Integer(-87)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        linkedList0 = LinkedList()
        reverseDeleteGraph0 = ReverseDeleteGraph(
            inMemoryPath0, linkedList0, linkedList0
        )
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer1 = integerWeightBaseOperations0.identity()
        linkedList0.add(integer1)
        integer2 = Integer(0)
        vertexPair0 = reverseDeleteGraph0.getVertices1(integer2)
        self.assertIsNone(vertexPair0)
