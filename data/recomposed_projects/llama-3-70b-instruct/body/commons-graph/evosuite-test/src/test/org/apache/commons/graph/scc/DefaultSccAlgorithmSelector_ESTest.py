from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.scc.DefaultSccAlgorithmSelector import *

# from src.test.org.apache.commons.graph.scc.DefaultSccAlgorithmSelector_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DefaultSccAlgorithmSelector_ESTest(unittest.TestCase):

    def test12(self) -> None:

        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector[
            int, LinkedHashSet[int]
        ](None)

        try:
            defaultSccAlgorithmSelector0.applyingTarjan()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.scc.TarjanAlgorithm", e)

    def test11(self) -> None:

        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector[
            LinkedHashSet[int], int
        ](None)

        with self.assertRaises(RuntimeError):
            defaultSccAlgorithmSelector0.applyingKosarajuSharir0()
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.graph.scc.KosarajuSharirAlgorithm", e)

    def test10(self) -> None:

        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector[
            LinkedHashSet[int], LinkedHashSet[int]
        ](None)
        linkedHashSet0 = LinkedHashSet[int]()

        try:
            defaultSccAlgorithmSelector0.applyingKosarajuSharir1(linkedHashSet0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.scc.KosarajuSharirAlgorithm", e)

    def test09(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector[int, int](
            directedMutableGraph0
        )
        set0 = defaultSccAlgorithmSelector0.applyingCheriyanMehlhornGabow()
        self.assertTrue(len(set0) == 0)

    def test08(self) -> None:

        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector[
            LinkedHashSet[int], int
        ](None)

        with pytest.raises(RuntimeError):
            defaultSccAlgorithmSelector0.applyingCheriyanMehlhornGabow()
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.scc.CheriyanMehlhornGabowAlgorithm", e
        )

    def test07(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector(
            directedMutableGraph0
        )
        linkedHashSet0 = set()

        with self.assertRaises(RuntimeError):
            defaultSccAlgorithmSelector0.applyingKosarajuSharir1(linkedHashSet0)

        verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test06(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector(
            directedMutableGraph0
        )

        with pytest.raises(RuntimeError):
            defaultSccAlgorithmSelector0.applyingKosarajuSharir1(None)
            self.fail("Expecting exception: RuntimeError")

    def test05(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = -1
        directedMutableGraph0.addVertex(integer0)
        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector[int, int](
            directedMutableGraph0
        )
        set0 = defaultSccAlgorithmSelector0.applyingCheriyanMehlhornGabow()
        self.assertFalse(set0)

    def test04(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[
            LinkedHashSet[int], LinkedHashSet[int]
        ]()
        linkedHashSet0 = LinkedHashSet[int]()
        directedMutableGraph0.addVertex(linkedHashSet0)
        revertedGraph0 = RevertedGraph[LinkedHashSet[int], LinkedHashSet[int]](
            directedMutableGraph0
        )
        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector[
            LinkedHashSet[int], LinkedHashSet[int]
        ](revertedGraph0)
        set0 = defaultSccAlgorithmSelector0.applyingKosarajuSharir0()
        self.assertEqual(1, len(set0))

    def test03(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, LinkedHashSet[int]]()
        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector[
            int, LinkedHashSet[int]
        ](directedMutableGraph0)
        set0 = defaultSccAlgorithmSelector0.applyingKosarajuSharir0()
        self.assertEqual(0, len(set0))

    def test02(self) -> None:

        # Create a DirectedMutableGraph
        directedMutableGraph0 = DirectedMutableGraph()

        # Create a LinkedHashSet
        linkedHashSet0 = LinkedHashSet()

        # Add the LinkedHashSet to the DirectedMutableGraph
        directedMutableGraph0.addVertex(linkedHashSet0)

        # Create a RevertedGraph
        revertedGraph0 = RevertedGraph(directedMutableGraph0)

        # Create a DefaultSccAlgorithmSelector
        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector(revertedGraph0)

        # Apply the Kosaraju-Sharir algorithm
        set0 = defaultSccAlgorithmSelector0.applyingKosarajuSharir1(linkedHashSet0)

        # Assert that the set is not empty
        assert not set0.isEmpty()

    def test01(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        integer0 = -1473
        directedMutableGraph0.addVertex(integer0)
        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector[int, int](
            directedMutableGraph0
        )
        set0 = defaultSccAlgorithmSelector0.applyingTarjan()
        self.assertFalse(set0.isEmpty())

    def test00(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, LinkedHashSet[int]]()
        defaultSccAlgorithmSelector0 = DefaultSccAlgorithmSelector[
            int, LinkedHashSet[int]
        ](directedMutableGraph0)
        set0 = defaultSccAlgorithmSelector0.applyingTarjan()
        self.assertTrue(len(set0) == 0)
