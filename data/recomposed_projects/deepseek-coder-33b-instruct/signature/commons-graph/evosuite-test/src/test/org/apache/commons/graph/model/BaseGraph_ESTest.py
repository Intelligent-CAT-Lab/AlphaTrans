from __future__ import annotations
import time
import re
import mock
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.model.BaseGraph import *

# from src.test.org.apache.commons.graph.model.BaseGraph_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class BaseGraph_ESTest(unittest.TestCase):

    def test29(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[
            int, UndirectedMutableGraph[object, int]
        ]()
        integer0 = Integer(0)

        try:
            directedMutableGraph0.getConnectedVertices(integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test28(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        int0 = undirectedMutableGraph0.getOrder()
        self.assertEqual(0, int0)

    def test27(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = -2145857996
        directedMutableGraph0.addVertex(integer0)
        map0 = directedMutableGraph0.getAdjacencyList()
        self.assertFalse(map0)

    def test26(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        iterable0 = directedMutableGraph0.getVertices0()
        assert iterable0 is not None

    def test25(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        iterable0 = directedMutableGraph0.getEdges()
        assert iterable0 is not None

    def test24(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        int0 = undirectedMutableGraph0.getSize()
        self.assertEqual(0, int0)

    def test23(self) -> None:

        monoid0 = unittest.mock.Mock(spec=Monoid)
        monoid0.identity.return_value = None
        mapper0 = unittest.mock.Mock(spec=Mapper)
        mutableSpanningTree0 = MutableSpanningTree(monoid0, mapper0)
        boolean0 = mutableSpanningTree0.containsEdge(None)
        self.assertFalse(boolean0)

    def test22(self) -> None:

        object0 = object()
        directedMutableGraph0 = DirectedMutableGraph[
            int, UndirectedMutableGraph[int, int]
        ]()
        boolean0 = directedMutableGraph0.equals(object0)
        self.assertFalse(boolean0)

    def test21(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        boolean0 = directedMutableGraph0.equals(directedMutableGraph0)
        self.assertTrue(boolean0)

    def test20(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        boolean0 = directedMutableGraph0.equals(None)
        self.assertFalse(boolean0)

    def test19(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        directedMutableGraph1 = DirectedMutableGraph[
            int, UndirectedMutableGraph[int, int]
        ]()
        boolean0 = directedMutableGraph1.equals(directedMutableGraph0)
        self.assertTrue(boolean0)

    def test18(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, object]()
        string0 = str(directedMutableGraph0)
        self.assertEqual("{}", string0)

    def test17(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        undirectedMutableGraph0.hashCode()

    def test16(self) -> None:

        objectArray0 = []
        try:
            BaseGraph._checkGraphCondition(False, None, objectArray0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            pass

    def test15(self) -> None:

        objectArray0 = [None] * 5
        try:
            BaseGraph._checkGraphCondition(False, "WtINvQ>x%04BJ+", objectArray0)
            self.fail("Expecting exception: FormatFlagsConversionMismatchException")

        except GraphException as e:
            self.verifyException("java.util.Formatter$FormatSpecifier", e)

    def test14(self) -> None:

        objectArray0 = []
        try:
            BaseGraph._checkGraphCondition(
                False, "Head Vertex '%s' not present in the Graph", objectArray0
            )
            self.fail("Expecting exception: MissingFormatArgumentException")

        except GraphException as e:
            self.assertEqual(str(e), "Head Vertex '%s' not present in the Graph")

    def test13(self) -> None:

        objectArray0 = [None] * 9
        try:
            BaseGraph._checkGraphCondition(False, "HE%}R~;8I|2}vD", objectArray0)
            self.fail("Expecting exception: UnknownFormatConversionException")

        except GraphException as e:
            self.verifyException("java.util.Formatter", e)

    def test12(self) -> None:

        try:
            BaseGraph._checkGraphCondition(
                False, "org.apache.commons.graph.model.MutableSpanningTree", None
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test11(self) -> None:

        integer0 = Integer(-2862)
        vertexPair0 = VertexPair(integer0, integer0)
        undirectedMutableGraph0 = UndirectedMutableGraph()
        boolean0 = undirectedMutableGraph0.containsVertex(vertexPair0)
        self.assertFalse(boolean0)

    def test10(self) -> None:

        linkedHashSet0 = set()
        directedMutableGraph0 = DirectedMutableGraph()
        directedMutableGraph0.addVertex(linkedHashSet0)
        boolean0 = directedMutableGraph0.containsVertex(linkedHashSet0)
        self.assertTrue(boolean0)

    def test09(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        map0 = directedMutableGraph0.getAdjacencyList()
        self.assertEqual(0, len(map0))

    def test08(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[VertexPair[int], object]()
        set0 = undirectedMutableGraph0.getAllEdges()
        self.assertEqual(0, len(set0))

    def test07(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, Comparable[int]]()
        integer0 = int(1)
        undirectedMutableGraph0.addVertex(integer0)
        comparable0 = undirectedMutableGraph0.getEdge(integer0, integer0)
        self.assertIsNone(comparable0)

    def test06(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        map0 = undirectedMutableGraph0.getIndexedEdges()
        assert len(map0) == 0

    def test05(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        map0 = undirectedMutableGraph0.getIndexedVertices()
        assert len(map0) == 0

    def test04(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        integer0 = int(1630)
        undirectedMutableGraph0.addVertex(integer0)
        int0 = undirectedMutableGraph0.getOrder()
        self.assertEqual(1, int0)

    def test02(self) -> None:

        objectArray0 = [None] * 5
        BaseGraph._checkGraphCondition(True, "", objectArray0)
        self.assertEqual(5, len(objectArray0))

    def test01(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, new=ViolatedAssumptionAnswer())
        mutableSpanningTree0 = MutableSpanningTree(
            integerWeightBaseOperations0, mapper0
        )
        integer0 = Integer(-2862)
        vertexPair0 = VertexPair(integer0, integer0)

        with pytest.raises(RuntimeError) as e:
            mutableSpanningTree0.getEdge(vertexPair0, None)

        verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test00(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, Comparable[int]]()
        integer0 = int(1)
        undirectedMutableGraph0.addVertex(integer0)
        integer1 = int(1)
        undirectedMutableGraph0.addEdge(integer0, integer0, integer1)
        self.assertEqual(1, undirectedMutableGraph0.getOrder())
