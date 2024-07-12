from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import pathlib
import io
import unittest
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *

# from src.test.org.apache.commons.graph.model.InMemoryPath_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class InMemoryPath_ESTest(unittest.TestCase):

    def test37(self) -> None:

        integer0 = Integer(2299)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        string0 = inMemoryPath0.toString()
        self.assertEqual("InMemoryPath [vertices=[], edges=[]]", string0)

    def test36(self) -> None:

        integer0 = -2838
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        inMemoryPath0.addConnectionInTail(integer0, integer0, integer0)
        int0 = inMemoryPath0.getDegree(integer0)
        self.assertEqual(2, inMemoryPath0.getOrder())
        self.assertEqual(1, int0)

    def test35(self) -> None:

        integer0 = Integer(-2838)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        inMemoryPath1 = InMemoryPath(integer0, integer0)
        boolean0 = inMemoryPath1.equals(inMemoryPath0)
        self.assertTrue(boolean0)

    def test34(self) -> None:

        integer0 = Integer(-540)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        vertexPair0 = inMemoryPath0.getVertices1(integer0)
        self.assertIsNone(vertexPair0)

    def test33(self) -> None:

        integer0 = -40
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        boolean0 = inMemoryPath0.containsVertex(integer0)
        self.assertFalse(boolean0)

    def test32(self) -> None:

        integer0 = Integer(0)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        int0 = inMemoryPath0.getSize()
        self.assertEqual(0, int0)

    def test31(self) -> None:

        integer0 = Integer(-2838)
        vertexPair0 = VertexPair(integer0, integer0)
        inMemoryPath0 = InMemoryPath(vertexPair0, vertexPair0)
        boolean0 = inMemoryPath0.containsEdge(vertexPair0)
        self.assertFalse(boolean0)

    def test30(self) -> None:

        integer0 = Integer(-2838)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        int0 = inMemoryPath0.getOrder()
        self.assertEqual(0, int0)

    def test29(self) -> None:

        integer0 = Integer(2299)
        vertexPair0 = VertexPair(integer0, integer0)
        inMemoryPath0 = InMemoryPath(vertexPair0, vertexPair0)
        inMemoryPath1 = inMemoryPath0.getEdge(vertexPair0, vertexPair0)
        self.assertIsNone(inMemoryPath1)

    def test28(self) -> None:

        integer0 = -2146245189
        integer1 = 1034
        inMemoryPath0 = InMemoryPath(integer1, integer0)
        inMemoryPath0.addConnectionInHead(integer1, integer1, integer1)
        inMemoryPath0.getConnectedVertices(integer1)
        self.assertEqual(1, inMemoryPath0.getOrder())

    def test27(self) -> None:

        integer0 = -2838
        vertexPair0 = VertexPair(integer0, integer0)
        inMemoryPath0 = InMemoryPath(vertexPair0, vertexPair0)
        inMemoryPath0.addConnectionInHead(vertexPair0, vertexPair0, vertexPair0)
        inMemoryPath0.containsEdge(vertexPair0)
        self.assertEqual(2, inMemoryPath0.getOrder())

    def test26(self) -> None:

        integer0 = -2838
        inMemoryPath0 = InMemoryPath(integer0, integer0)

        with pytest.raises(RuntimeError):
            inMemoryPath0.addConnectionInTail(integer0, integer0, None)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test25(self) -> None:

        integer0 = Integer(2299)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        inMemoryPath1 = InMemoryPath(inMemoryPath0, inMemoryPath0)
        iterable0 = inMemoryPath1.getConnectedVertices(inMemoryPath0)
        self.assertIsNone(iterable0)

    def test24(self) -> None:

        integer0 = Integer(-540)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        boolean0 = inMemoryPath0.equals(None)
        self.assertFalse(boolean0)

    def test23(self) -> None:

        integer0 = Integer(373)
        vertexPair0 = VertexPair(integer0, integer0)
        inMemoryPath0 = InMemoryPath(vertexPair0, vertexPair0)
        inMemoryPath1 = InMemoryPath(vertexPair0, vertexPair0)
        object0 = inMemoryPath1.getSource()
        boolean0 = inMemoryPath0.equals(object0)
        self.assertFalse(boolean0)

    def test22(self) -> None:

        integer0 = Integer(-2136799647)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        inMemoryPath1 = InMemoryPath(inMemoryPath0, inMemoryPath0)
        boolean0 = inMemoryPath1.equals(inMemoryPath0)
        self.assertFalse(boolean0)

    def test21(self) -> None:

        integer0 = Integer(2881)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integer1 = Integer(257)
        inMemoryPath1 = InMemoryPath(integer0, integer1)
        boolean0 = inMemoryPath0.equals(inMemoryPath1)
        self.assertFalse(boolean0)

    def test20(self) -> None:

        integer0 = Integer(1)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        inMemoryPath1 = InMemoryPath(integer0, integer0)
        inMemoryPath1.addConnectionInHead(integer0, integer0, integer0)
        boolean0 = inMemoryPath0.equals(inMemoryPath1)
        self.assertEqual(2, inMemoryPath1.getOrder())
        self.assertFalse(boolean0)

    def test19(self) -> None:

        integer0 = Integer(296)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        vertexPair0 = VertexPair(integer0, integer0)
        inMemoryPath0.addConnectionInTail(integer0, vertexPair0, integer0)
        inMemoryPath1 = InMemoryPath(integer0, integer0)
        inMemoryPath1.addConnectionInTail(integer0, integer0, integer0)
        boolean0 = inMemoryPath1.equals(inMemoryPath0)
        self.assertEqual(2, inMemoryPath1.getOrder())
        self.assertFalse(boolean0)

    def test18(self) -> None:

        integer0 = -2146245189
        integer1 = 1034
        inMemoryPath0 = InMemoryPath(integer1, integer0)

        with pytest.raises(ValueError):
            inMemoryPath0.getConnectedVertices(integer1)
            # Impossible to get the degree of input vertex; 1034 not contained in this path
            verifyException("org.apache.commons.graph.utils.Assertions")

    def test17(self) -> None:

        integer0 = -540
        inMemoryPath0 = InMemoryPath(integer0, integer0)

        with pytest.raises(ValueError):
            inMemoryPath0.getDegree(integer0)
            self.fail("Expecting exception: ValueError")

        verifyException("org.apache.commons.graph.utils.Assertions", ValueError)

    def test16(self) -> None:

        integer0 = Integer(373)
        vertexPair0 = VertexPair(integer0, integer0)
        integer1 = Integer(-2147018722)
        vertexPair1 = VertexPair(integer1, integer0)
        inMemoryPath0 = InMemoryPath(vertexPair0, vertexPair1)
        inMemoryPath0.addConnectionInTail(vertexPair1, None, vertexPair1)
        int0 = inMemoryPath0.getDegree(vertexPair1)
        self.assertEqual(2, inMemoryPath0.getOrder())
        self.assertEqual(1, int0)

    def test15(self) -> None:

        integer0 = Integer((-2145645046))
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integer1 = Integer((-296))
        inMemoryPath1 = InMemoryPath(integer1, integer1)
        inMemoryPath1.addConnectionInTail(integer0, inMemoryPath0, integer1)
        int0 = inMemoryPath1.getDegree(integer0)
        self.assertEqual(2, inMemoryPath1.getOrder())
        self.assertEqual(2, int0)

    def test14(self) -> None:

        integer0 = Integer(4762)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        inMemoryPath0.hashCode()

    def test13(self) -> None:

        integer0 = Integer(0)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        iterable0 = inMemoryPath0.getEdges()
        assert iterable0 is not None

    def test12(self) -> None:

        integer0 = -18
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        boolean0 = inMemoryPath0.equals(inMemoryPath0)
        self.assertTrue(boolean0)

    def test11(self) -> None:

        inMemoryPath0 = None
        try:
            inMemoryPath0 = InMemoryPath(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Path source cannot be null
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test10(self) -> None:

        integer0 = -513
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        vertexPair0 = VertexPair(integer0, integer0)

        try:
            inMemoryPath0.addConnectionInHead(integer0, vertexPair0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            # Impossible to construct a Vertex with a null tail
            self.assertTrue("org.apache.commons.graph.utils.Assertions" in str(e))

    def test09(self) -> None:

        integer0 = -533
        inMemoryPath0 = InMemoryPath(integer0, integer0)

        with pytest.raises(RuntimeError):
            inMemoryPath0.getConnectedVertices(None)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test08(self) -> None:

        integer0 = -529
        inMemoryPath0 = InMemoryPath(integer0, integer0)

        with pytest.raises(RuntimeError):
            inMemoryPath0.getDegree(None)

    def test07(self) -> None:

        integer0 = -1783
        inMemoryPath0 = InMemoryPath(integer0, integer0)

        with pytest.raises(RuntimeError):
            inMemoryPath0.getEdge(integer0, None)

        # Impossible to construct a Vertex with a null tail
        verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test06(self) -> None:

        integer0 = Integer(0)
        vertexPair0 = VertexPair(integer0, integer0)
        inMemoryPath0 = InMemoryPath(vertexPair0, vertexPair0)
        inMemoryPath0.addConnectionInHead(vertexPair0, integer0, vertexPair0)
        inMemoryPath0.containsVertex(vertexPair0)
        self.assertEqual(2, inMemoryPath0.getOrder())

    def test05(self) -> None:

        integer0 = Integer(2299)
        vertexPair0 = VertexPair(integer0, integer0)
        inMemoryPath0 = InMemoryPath(vertexPair0, vertexPair0)
        inMemoryPath1 = InMemoryPath(integer0, integer0)
        inMemoryPath0.addConnectionInTail(vertexPair0, inMemoryPath1, vertexPair0)
        inMemoryPath0.getEdge(vertexPair0, vertexPair0)
        self.assertEqual(2, inMemoryPath0.getOrder())

    def test04(self) -> None:

        integer0 = -2838
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        inMemoryPath0.addConnectionInTail(integer0, integer0, integer0)
        int0 = inMemoryPath0.getOrder()
        self.assertEqual(2, int0)

    def test03(self) -> None:

        integer0 = -2838
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        inMemoryPath0.addConnectionInTail(integer0, integer0, integer0)
        inMemoryPath0.getSize()
        self.assertEqual(2, inMemoryPath0.getOrder())

    def test02(self) -> None:

        integer0 = Integer(0)
        vertexPair0 = VertexPair(integer0, integer0)
        inMemoryPath0 = InMemoryPath(vertexPair0, vertexPair0)
        vertexPair1 = inMemoryPath0.getTarget()
        self.assertIs(vertexPair1, vertexPair0)

    def test01(self) -> None:

        integer0 = -1
        vertexPair0 = VertexPair(integer0, integer0)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        inMemoryPath0.addConnectionInHead(integer0, vertexPair0, integer0)
        inMemoryPath0.getVertices1(vertexPair0)
        self.assertEqual(2, inMemoryPath0.getOrder())

    def test00(self) -> None:

        integer0 = Integer(1312)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integer1 = Integer(1312)
        inMemoryPath0.addConnectionInHead(integer0, integer0, integer1)
        self.assertEqual(2, inMemoryPath0.getOrder())
