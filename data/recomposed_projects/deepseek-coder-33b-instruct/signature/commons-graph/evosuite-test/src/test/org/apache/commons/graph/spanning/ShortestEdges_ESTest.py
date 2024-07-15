from __future__ import annotations
import time
import re
import mock
import os
import pathlib
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.spanning.ReverseDeleteGraph import *
from src.main.org.apache.commons.graph.spanning.ShortestEdges import *

# from src.test.org.apache.commons.graph.spanning.ShortestEdges_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class ShortestEdges_ESTest(unittest.TestCase):

    def test15(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        integer0 = int(0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = Mapper[int, int]()
        shortestEdges0 = ShortestEdges[int, int, int](
            undirectedMutableGraph0, integer0, integerWeightBaseOperations0, mapper0
        )
        string0 = str(shortestEdges0)
        self.assertIsNotNone(string0)

    def test14(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        integer0 = int(0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = Mapper[int, int]()
        shortestEdges0 = ShortestEdges[int, int, int](
            undirectedMutableGraph0, integer0, integerWeightBaseOperations0, mapper0
        )
        assert shortestEdges0.isEmpty()

        shortestEdges0.addPredecessor(integer0, integer0)
        boolean0 = shortestEdges0.isEmpty()
        assert not boolean0

    def test13(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        shortestEdges0 = ShortestEdges(
            undirectedMutableGraph0, None, integerWeightBaseOperations0, None
        )
        shortestEdges0.addPredecessor(None, None)

        with pytest.raises(RuntimeError):
            shortestEdges0.compare(None, None)
            verifyException(
                "org.apache.commons.graph.spanning.ShortestEdges", RuntimeError
            )

    def test12(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = integerWeightBaseOperations0.identity()
        shortestEdges0 = ShortestEdges(
            undirectedMutableGraph0, integer0, integerWeightBaseOperations0, None
        )
        int0 = shortestEdges0.compare(None, integer0)
        self.assertEqual(0, int0)

    def test11(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = integerWeightBaseOperations0.identity()
        shortestEdges0 = ShortestEdges(
            undirectedMutableGraph0, integer0, integerWeightBaseOperations0, None
        )
        shortestEdges0.addPredecessor(integer0, integer0)
        int0 = shortestEdges0.compare(None, integer0)
        self.assertEqual(1, int0)

    def test10(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = integerWeightBaseOperations0.identity()
        shortestEdges0 = ShortestEdges(
            undirectedMutableGraph0, integer0, integerWeightBaseOperations0, None
        )
        shortestEdges0.addPredecessor(integer0, integer0)
        integer1 = -1610612734
        int0 = shortestEdges0.compare(integer0, integer1)
        self.assertEqual(-1, int0)

    def test09(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        integer0 = int(0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = Mapper[int, int]()
        shortestEdges0 = ShortestEdges[int, int, int](
            undirectedMutableGraph0, integer0, integerWeightBaseOperations0, mapper0
        )
        spanningTree0 = shortestEdges0.createSpanningTree()
        self.assertIsNotNone(spanningTree0)

    def test08(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        shortestEdges0 = ShortestEdges(
            undirectedMutableGraph0, None, integerWeightBaseOperations0, None
        )
        shortestEdges0.addPredecessor(None, None)

        try:
            shortestEdges0.createSpanningTree()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.spanning.ShortestEdges", e)

    def test07(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = integerWeightBaseOperations0.identity()
        shortestEdges0 = ShortestEdges(
            undirectedMutableGraph0, integer0, integerWeightBaseOperations0, None
        )
        integer1 = -2001
        integer2 = shortestEdges0.getWeight(integer1)
        self.assertIsNone(integer2)

    def test06(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        integer0 = int(0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = Mapper[int, int]()
        shortestEdges0 = ShortestEdges[int, int, int](
            undirectedMutableGraph0, integer0, integerWeightBaseOperations0, mapper0
        )
        integer1 = shortestEdges0.getWeight(integer0)
        self.assertEqual(0, integer1)

    def test05(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = integerWeightBaseOperations0.identity()
        shortestEdges0 = ShortestEdges(
            undirectedMutableGraph0, integer0, integerWeightBaseOperations0, None
        )
        integer1 = -2001
        shortestEdges0.addPredecessor(integer1, integer1)

        try:
            shortestEdges0.getWeight(integer1)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            self.verifyException("org.apache.commons.graph.spanning.ShortestEdges", e)

    def test03(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        shortestEdges0 = ShortestEdges(
            undirectedMutableGraph0, None, integerWeightBaseOperations0, None
        )
        shortestEdges0.addPredecessor(None, None)
        boolean0 = shortestEdges0.hasWeight(None)
        self.assertTrue(boolean0)

    def test02(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        shortestEdges0 = ShortestEdges(
            undirectedMutableGraph0, None, integerWeightBaseOperations0, None
        )
        boolean0 = shortestEdges0.hasWeight(None)
        self.assertFalse(boolean0)

    def test00(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        integer0 = 0
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = Mock(spec=Mapper)
        mapper0.map.return_value = None
        shortestEdges0 = ShortestEdges(
            undirectedMutableGraph0, integer0, integerWeightBaseOperations0, mapper0
        )
        shortestEdges0.addPredecessor(None, integer0)
        integer1 = shortestEdges0.getWeight(None)
        self.assertIsNone(integer1)
