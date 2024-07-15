from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *

# from src.test.org.apache.commons.graph.model.UndirectedMutableGraph_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class UndirectedMutableGraph_ESTest(unittest.TestCase):

    def test8(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        linkedHashSet0 = LinkedHashSet()

        with pytest.raises(RuntimeError):
            undirectedMutableGraph0.decorateRemoveEdge(linkedHashSet0)
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.model.UndirectedMutableGraph", RuntimeError
        )

    def test7(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        linkedHashSet0 = LinkedHashSet()
        undirectedMutableGraph0.addVertex(linkedHashSet0)
        undirectedMutableGraph0.decorateAddEdge(
            linkedHashSet0, linkedHashSet0, linkedHashSet0
        )
        undirectedMutableGraph0.decorateRemoveEdge(linkedHashSet0)
        self.assertTrue(linkedHashSet0.isEmpty())

    def test6(self) -> None:

        integer0 = -1923
        undirectedMutableGraph0 = UndirectedMutableGraph()

        with self.assertRaises(RuntimeError):
            undirectedMutableGraph0.getDegree(integer0)
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.model.UndirectedMutableGraph", RuntimeError
        )

    def test5(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, LinkedHashSet[int]]()
        integer0 = -1485
        undirectedMutableGraph0.decorateRemoveVertex(integer0)
        self.assertEqual(0, undirectedMutableGraph0.getSize())

    def test4(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        integer0 = int(0)
        undirectedMutableGraph0.addVertex(integer0)

        try:
            undirectedMutableGraph0.decorateAddEdge(None, None, integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test3(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[LinkedHashSet[int], int]()
        linkedHashSet0 = LinkedHashSet[int]()
        undirectedMutableGraph0.addVertex(linkedHashSet0)
        integer0 = int(3)
        undirectedMutableGraph0.internalAddEdge(
            linkedHashSet0, integer0, linkedHashSet0
        )
        int0 = undirectedMutableGraph0.getDegree(linkedHashSet0)
        self.assertEqual(1, int0)

    def test2(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        integer0 = int((-2158))
        undirectedMutableGraph0.addVertex(integer0)
        int0 = undirectedMutableGraph0.getDegree(integer0)
        self.assertEqual(0, int0)

    def test1(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, LinkedHashSet[int]]()
        integer0 = int((-3966))
        undirectedMutableGraph0.decorateAddVertex(integer0)
        self.assertEqual(0, undirectedMutableGraph0.getOrder())

    def test0(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        linkedHashSet0 = LinkedHashSet()
        integer0 = Integer(3920)

        with pytest.raises(RuntimeError):
            undirectedMutableGraph0.decorateAddEdge(
                linkedHashSet0, integer0, linkedHashSet0
            )
            verifyException(
                "org.apache.commons.graph.model.BaseMutableGraph", RuntimeError
            )
