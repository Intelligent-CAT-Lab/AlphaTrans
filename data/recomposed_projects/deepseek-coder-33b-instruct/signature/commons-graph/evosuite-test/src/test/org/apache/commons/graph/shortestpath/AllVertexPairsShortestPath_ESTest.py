from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import pathlib
import io
import unittest
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *

# from src.test.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class AllVertexPairsShortestPath_ESTest(unittest.TestCase):

    def test15(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(
            integerWeightBaseOperations0
        )
        string0 = str(allVertexPairsShortestPath0)
        self.assertIsNotNone(string0)

    def test14(self) -> None:

        integer_weight_base_operations0 = IntegerWeightBaseOperations()
        object0 = object()
        all_vertex_pairs_shortest_path0 = AllVertexPairsShortestPath(
            integer_weight_base_operations0
        )
        integer0 = -1
        all_vertex_pairs_shortest_path0.add_shortest_distance(
            integer_weight_base_operations0, object0, integer0
        )
        boolean0 = all_vertex_pairs_shortest_path0.has_shortest_distance(
            integer_weight_base_operations0, object0
        )
        self.assertTrue(boolean0)

    def test13(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(
            integerWeightBaseOperations0
        )
        integer0 = 1304
        mapper0 = Mock(spec=Mapper)
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0,
            integerWeightBaseOperations0,
            integerWeightBaseOperations0,
            mapper0,
        )
        allVertexPairsShortestPath0.addShortestPath(
            integerWeightBaseOperations0,
            integerWeightBaseOperations0,
            inMemoryWeightedPath0,
        )
        weightedPath0 = allVertexPairsShortestPath0.findShortestPath(
            integerWeightBaseOperations0, integerWeightBaseOperations0
        )
        self.assertEqual(0, weightedPath0.getOrder())

    def test12(self) -> None:

        integer0 = Integer(0)
        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer)
        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(orderedMonoid0)
        integer1 = Integer(2946)
        inMemoryWeightedPath0 = allVertexPairsShortestPath0.getShortestDistance(
            integer1, integer0
        )
        self.assertIsNone(inMemoryWeightedPath0)

    def test11(self) -> None:

        ordered_monoid0 = unittest.mock.Mock(spec=OrderedMonoid)
        ordered_monoid0.identity.return_value = None

        all_vertex_pairs_shortest_path0 = AllVertexPairsShortestPath(ordered_monoid0)

        integer0 = Integer(0)
        in_memory_weighted_path0 = (
            all_vertex_pairs_shortest_path0.get_shortest_distance(integer0, integer0)
        )

        self.assertIsNone(in_memory_weighted_path0)

    def test10(self) -> None:

        integer0 = Integer(0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(
            integerWeightBaseOperations0
        )
        integer1 = Integer(2946)
        boolean0 = allVertexPairsShortestPath0.hasShortest_distance(integer0, integer1)
        self.assertFalse(boolean0)

    def test09(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(
            integerWeightBaseOperations0
        )
        boolean0 = allVertexPairsShortestPath0.hasShortestDistance(
            integerWeightBaseOperations0, integerWeightBaseOperations0
        )
        self.assertTrue(boolean0)

    def test08(self) -> None:

        ordered_monoid0 = unittest.mock.Mock(spec=OrderedMonoid)
        all_vertex_pairs_shortest_path0 = AllVertexPairsShortestPath(ordered_monoid0)

        with self.assertRaises(RuntimeError):
            all_vertex_pairs_shortest_path0.add_shortest_distance(None, None, None)
            self.fail("Expecting exception: RuntimeError")

    def test07(self) -> None:

        integer0 = Integer(0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, new=ViolatedAssumptionAnswer())
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, mapper0
        )
        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(
            integerWeightBaseOperations0
        )

        # Undeclared exception
        try:
            allVertexPairsShortestPath0.addShortestPath(
                None, integer0, inMemoryWeightedPath0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Impossible to add a shortest path from a null source
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test06(self) -> None:

        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(None)
        try:
            allVertexPairsShortestPath0.findShortestPath(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test05(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(
            integerWeightBaseOperations0
        )

        with pytest.raises(RuntimeError):
            allVertexPairsShortestPath0.getShortestDistance(None, None)
            pytest.fail("Expecting exception: RuntimeError")

    def test04(self) -> None:

        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(None)
        integer0 = 693

        with self.assertRaises(RuntimeError):
            allVertexPairsShortestPath0.getShortestDistance(integer0, integer0)
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath", e
        )

    def test03(self) -> None:

        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(None)
        try:
            allVertexPairsShortestPath0.hasShortestDistance(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test02(self) -> None:

        inMemoryWeightedPath0 = unittest.mock.Mock(spec=InMemoryWeightedPath)
        inMemoryWeightedPath0.toString.return_value = None

        orderedMonoid0 = unittest.mock.Mock(spec=OrderedMonoid)
        orderedMonoid0.identity.return_value = inMemoryWeightedPath0

        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(orderedMonoid0)

        integer0 = Integer(0)
        inMemoryWeightedPath1 = allVertexPairsShortestPath0.getShortestDistance(
            integer0, integer0
        )

        self.assertEqual(0, inMemoryWeightedPath1.getSize())

    def test01(self) -> None:

        integer0 = Integer(0)
        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer)
        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(orderedMonoid0)
        integer1 = Integer(2946)
        monoid0 = mock(Monoid, ViolatedAssumptionAnswer)
        monoid0.identity.return_value = None
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer)
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer1, integer1, monoid0, mapper0
        )
        allVertexPairsShortestPath0.addShortestPath(
            integer0, integer1, inMemoryWeightedPath0
        )
        assert not integer1.equals(integer0)

    def test00(self) -> None:

        integer0 = Integer(3102)
        integer1 = Integer(3102)
        orderedMonoid0 = mock(OrderedMonoid, ViolatedAssumptionAnswer)
        allVertexPairsShortestPath0 = AllVertexPairsShortestPath(orderedMonoid0)

        with pytest.raises(RuntimeError):
            allVertexPairsShortestPath0.findShortestPath(integer1, integer0)
            verifyException(
                "org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath",
                RuntimeError,
            )
