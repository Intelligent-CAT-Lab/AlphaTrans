from __future__ import annotations
import time
import re
import unittest
import pytest
import io
import os
import unittest
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.scc.KosarajuSharirAlgorithm import *

# from src.test.org.apache.commons.graph.scc.KosarajuSharirAlgorithm_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class KosarajuSharirAlgorithm_ESTest(unittest.TestCase):

    def test9(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, LinkedHashSet[int]]()
        kosarajuSharirAlgorithm0 = KosarajuSharirAlgorithm[int, LinkedHashSet[int]](
            directedMutableGraph0
        )
        set0 = kosarajuSharirAlgorithm0.perform()
        self.assertTrue(set0.isEmpty())

    def test8(self) -> None:

        integer0 = -99
        directedMutableGraph0 = DirectedMutableGraph()
        kosarajuSharirAlgorithm0 = KosarajuSharirAlgorithm(directedMutableGraph0)

        with pytest.raises(RuntimeError):
            kosarajuSharirAlgorithm0.perform1(integer0)
            # Vertex -99 does not exist in the Graph
            verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test7(self) -> None:

        integer0 = Integer(-99)
        directedMutableGraph0 = DirectedMutableGraph[Integer, LinkedHashSet[Integer]]()
        directedMutableGraph0.addVertex(integer0)
        integer1 = Integer(-1428)
        directedMutableGraph0.addVertex(integer1)
        linkedHashSet0 = LinkedHashSet[Integer]()
        directedMutableGraph0.addEdge(integer0, linkedHashSet0, integer1)
        kosarajuSharirAlgorithm0 = KosarajuSharirAlgorithm[
            Integer, LinkedHashSet[Integer]
        ](directedMutableGraph0)
        set0 = kosarajuSharirAlgorithm0.perform0()
        self.assertEqual(2, len(set0))

    def test6(self) -> None:

        kosarajuSharirAlgorithm0 = KosarajuSharirAlgorithm(None)

        with pytest.raises(RuntimeError):
            kosarajuSharirAlgorithm0.perform()
            self.fail("Expecting exception: RuntimeError")

    def test5(self) -> None:

        kosarajuSharirAlgorithm0 = KosarajuSharirAlgorithm(None)

        with pytest.raises(RuntimeError):
            kosarajuSharirAlgorithm0.perform0()
            self.fail("Expecting exception: RuntimeError")

    def test4(self) -> None:

        kosarajuSharirAlgorithm0 = KosarajuSharirAlgorithm(None)

        with pytest.raises(RuntimeError):
            kosarajuSharirAlgorithm0.perform1(None)
            # Kosaraju Sharir algorithm cannot be calculated without expressing the source vertex
            verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test3(self) -> None:

        kosarajuSharirAlgorithm0 = KosarajuSharirAlgorithm(None)
        linkedHashSet0 = set()

        with pytest.raises(RuntimeError):
            kosarajuSharirAlgorithm0.perform1(linkedHashSet0)
            self.fail("Expecting exception: RuntimeError")

    def test2(self) -> None:

        integer0 = -1
        directedMutableGraph0 = DirectedMutableGraph[int, LinkedHashSet[int]]()
        directedMutableGraph0.addVertex(integer0)
        kosarajuSharirAlgorithm0 = KosarajuSharirAlgorithm[int, LinkedHashSet[int]](
            directedMutableGraph0
        )
        set0 = kosarajuSharirAlgorithm0.perform()
        self.assertFalse(set0.isEmpty())

    def test1(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        kosarajuSharirAlgorithm0 = KosarajuSharirAlgorithm(revertedGraph0)
        set0 = kosarajuSharirAlgorithm0.perform0()
        self.assertEqual(0, len(set0))

    def test0(self) -> None:

        integer0 = Integer(-99)
        directedMutableGraph0 = DirectedMutableGraph[Integer, LinkedHashSet[Integer]]()
        directedMutableGraph0.addVertex(integer0)
        integer1 = Integer(-1428)
        directedMutableGraph0.addVertex(integer1)
        linkedHashSet0 = LinkedHashSet[Integer]()
        directedMutableGraph0.addEdge(integer0, linkedHashSet0, integer1)
        kosarajuSharirAlgorithm0 = KosarajuSharirAlgorithm[
            Integer, LinkedHashSet[Integer]
        ](directedMutableGraph0)
        directedMutableGraph0.addEdge(integer1, linkedHashSet0, integer0)
        set0 = kosarajuSharirAlgorithm0.perform1(integer0)
        self.assertTrue(set0.contains(-1428))
