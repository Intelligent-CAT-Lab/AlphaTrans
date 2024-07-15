from __future__ import annotations
import time
import re
import os
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.spanning.SuperVertex import *

# from src.test.org.apache.commons.graph.spanning.SuperVertex_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.spanning.WeightedEdgesComparator import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class SuperVertex_ESTest(unittest.TestCase):

    def test8(self) -> None:

        integer0 = Integer(-1)
        undirectedMutableGraph0 = UndirectedMutableGraph()
        undirectedMutableGraph0.addVertex(integer0)
        superVertex0 = SuperVertex(integer0, undirectedMutableGraph0, None)
        iterator0 = superVertex0.iterator()
        assert iterator0 is not None

    def test7(self) -> None:

        integer0 = Integer(-1)
        undirectedMutableGraph0 = UndirectedMutableGraph()
        undirectedMutableGraph0.addVertex(integer0)
        undirectedMutableGraph0.addEdge(integer0, integer0, integer0)
        superVertex0 = SuperVertex(integer0, undirectedMutableGraph0, None)
        integer1 = superVertex0.getMinimumWeightEdge()
        self.assertEqual(-1, integer1)

    def test6(self) -> None:

        integer0 = Integer(-1)
        undirectedMutableGraph0 = UndirectedMutableGraph()
        undirectedMutableGraph0.addVertex(integer0)
        superVertex0 = SuperVertex(integer0, undirectedMutableGraph0, None)
        integer1 = superVertex0.getMinimumWeightEdge()
        self.assertIsNone(integer1)

    def test5(self) -> None:

        integer0 = Integer(-1)
        undirectedMutableGraph0 = UndirectedMutableGraph()
        undirectedMutableGraph0.addVertex(integer0)
        superVertex0 = SuperVertex(integer0, undirectedMutableGraph0, None)
        undirectedMutableGraph0.addEdge(integer0, integer0, integer0)
        superVertex1 = SuperVertex(integer0, undirectedMutableGraph0, None)
        superVertex0.merge(superVertex1)
        assert superVertex1 != superVertex0

    def test4(self) -> None:

        integer0 = Integer(2170)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer1 = integerWeightBaseOperations0.identity()
        inMemoryPath0 = InMemoryPath(integer0, integer1)
        superVertex0 = None
        try:
            superVertex0 = SuperVertex(integer0, inMemoryPath0, None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Impossible to get the degree of input vertex; 2170 not contained in this path
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test3(self) -> None:

        integer0 = -3413
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        superVertex0 = None

        try:
            superVertex0 = SuperVertex(None, inMemoryPath0, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Impossible to get the degree of a null vertex
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test2(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        superVertex0 = None
        try:
            superVertex0 = SuperVertex(None, undirectedMutableGraph0, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test1(self) -> None:

        integer0 = Integer(-1)
        undirectedMutableGraph0 = UndirectedMutableGraph()
        undirectedMutableGraph0.addVertex(integer0)
        superVertex0 = SuperVertex(integer0, undirectedMutableGraph0, None)

        try:
            superVertex0.merge(None)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.apache.commons.graph.spanning.SuperVertex", e)

    def test0(self) -> None:

        integer0 = -1
        undirectedMutableGraph0 = UndirectedMutableGraph()
        undirectedMutableGraph0.addVertex(integer0)
        integer1 = -1
        undirectedMutableGraph0.addEdge(integer0, integer1, integer0)
        superVertex0 = None
        try:
            superVertex0 = SuperVertex(integer1, undirectedMutableGraph0, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("java.util.TreeMap", e)
