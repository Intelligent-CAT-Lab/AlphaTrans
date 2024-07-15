from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.VertexPair import *

# from src.test.org.apache.commons.graph.VertexPair_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class VertexPair_ESTest(unittest.TestCase):

    def test9(self) -> None:

        vertexPair0 = None
        try:
            vertexPair0 = VertexPair(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Impossible to construct a Vertex with a null head
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test8(self) -> None:

        object0 = object()
        vertexPair0 = VertexPair(object0, object0)
        string0 = vertexPair0.to_string()
        self.assertIsNotNone(string0)

    def test7(self) -> None:

        integer0 = -1
        vertexPair0 = VertexPair(integer0, integer0)
        vertexPair0.hashCode()

    def test6(self) -> None:

        integer0 = -1
        vertexPair0 = VertexPair(integer0, integer0)
        boolean0 = vertexPair0.equals(integer0)
        self.assertFalse(boolean0)

    def test5(self) -> None:

        integer0 = -997
        object0 = object()
        vertexPair0 = VertexPair(integer0, object0)
        boolean0 = vertexPair0.equals(vertexPair0)
        self.assertTrue(boolean0)

    def test4(self) -> None:

        integer0 = Integer(-1291)
        vertexPair0 = VertexPair(integer0, integer0)
        boolean0 = vertexPair0.equals(None)
        self.assertFalse(boolean0)

    def test3(self) -> None:

        integer0 = -1
        vertexPair0 = VertexPair(integer0, integer0)
        vertexPair1 = VertexPair(integer0, integer0)
        boolean0 = vertexPair0.equals(vertexPair1)
        self.assertTrue(boolean0)

    def test2(self) -> None:

        object0 = object()
        vertexPair0 = VertexPair(object0, object0)
        vertexPair1 = VertexPair(vertexPair0, vertexPair0)
        boolean0 = vertexPair1.equals(vertexPair0)
        self.assertFalse(boolean0)

    def test1(self) -> None:

        integer0 = Integer(-1291)
        vertexPair0 = VertexPair(integer0, integer0)
        object0 = Object()
        vertexPair1 = VertexPair(integer0, object0)
        vertexPair2 = VertexPair(vertexPair0, vertexPair0)
        object1 = vertexPair2.getHead()
        boolean0 = vertexPair1.equals(object1)
        self.assertFalse(boolean0)

    def test0(self) -> None:

        integer0 = -1291
        object0 = object()
        vertexPair0 = VertexPair(integer0, object0)
        object1 = vertexPair0.getTail()
        self.assertIs(object1, object0)
