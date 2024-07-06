from __future__ import annotations
import time
import re
import mock
import os
import pathlib
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.model.InMemoryPath import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.PredecessorsList import *

# from src.test.org.apache.commons.graph.shortestpath.PredecessorsList_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class PredecessorsList_ESTest(unittest.TestCase):

    def test17(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = integerWeightBaseOperations0.identity()
        undirectedMutableGraph0 = UndirectedMutableGraph()
        predecessorsList0 = PredecessorsList(
            undirectedMutableGraph0, integerWeightBaseOperations0, None
        )
        predecessorsList0.addPredecessor(integer0, integer0)
        integer1 = -1
        with pytest.raises(RuntimeError):
            predecessorsList0.buildPath0(integer1, integer0)

    def test16(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = integerWeightBaseOperations0.identity()
        undirectedMutableGraph0 = UndirectedMutableGraph()
        predecessorsList0 = PredecessorsList(
            undirectedMutableGraph0, integerWeightBaseOperations0, None
        )
        integer1 = -1

        with pytest.raises(RuntimeError):
            predecessorsList0.buildPath1(
                integer1, integer0, integer0, predecessorsList0
            )

    def test15(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = integerWeightBaseOperations0.identity()
        undirectedMutableGraph0 = UndirectedMutableGraph()
        predecessorsList0 = PredecessorsList(
            undirectedMutableGraph0, integerWeightBaseOperations0, None
        )
        predecessorsList0.addPredecessor(integer0, integer0)
        integer1 = -1
        with pytest.raises(RuntimeError):
            predecessorsList0.buildPath1(
                integer1, integer0, integer0, predecessorsList0
            )

    def test14(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = integerWeightBaseOperations0.identity()
        undirectedMutableGraph0 = UndirectedMutableGraph()
        predecessorsList0 = PredecessorsList(
            undirectedMutableGraph0, integerWeightBaseOperations0, None
        )
        self.assertTrue(predecessorsList0.isEmpty())

        predecessorsList0.addPredecessor(integer0, integer0)
        boolean0 = predecessorsList0.isEmpty()
        self.assertFalse(boolean0)

    def test13(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        predecessorsList0 = PredecessorsList(undirectedMutableGraph0, None, None)
        boolean0 = predecessorsList0.isEmpty()
        self.assertTrue(boolean0)

    def test12(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        predecessorsList0 = PredecessorsList(None, integerWeightBaseOperations0, None)

        with self.assertRaises(RuntimeError):
            predecessorsList0.buildPath0(None, None)

    def test11(self) -> None:

        integer0 = -1
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        predecessorsList0 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, None
        )
        predecessorsList0.addPredecessor(integer0, integer0)
        integer1 = integerWeightBaseOperations0.append(integer0, integer0)

        try:
            predecessorsList0.buildPath0(integer1, integer0)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.assertEqual(str(e), "")

    def test10(self) -> None:

        integer0 = Integer(2427)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, mapper0
        )
        mapper1 = mock(Mapper, ViolatedAssumptionAnswer())
        predecessorsList0 = PredecessorsList(
            inMemoryWeightedPath0, integerWeightBaseOperations0, mapper1
        )

        with pytest.raises(RuntimeError):
            predecessorsList0.buildPath1(None, None, integer0, predecessorsList0)
            verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test09(self) -> None:

        integer0 = -1
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        predecessorsList0 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, None
        )
        predecessorsList0.addPredecessor(integer0, integer0)
        integer1 = integerWeightBaseOperations0.append(integer0, integer0)

        try:
            predecessorsList0.buildPath1(
                integer0, integer0, integer1, predecessorsList0
            )
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.assertEqual(str(e), "")

    def test08(self) -> None:

        integer0 = -2
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = Mock(Mapper)
        mapper0.map.return_value = integer0
        predecessorsList0 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, mapper0
        )
        integer1 = 1
        predecessorsList0.addPredecessor(integer1, integer0)
        weightedPath0 = predecessorsList0.buildPath0(integer0, integer1)
        self.assertIsNotNone(weightedPath0)

    def test07(self) -> None:

        integer0 = Integer(-2)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer)
        mapper0.map = Mock(side_effect=mapper0.map)
        predecessorsList0 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, mapper0
        )
        integer1 = Integer(1)
        integer2 = Integer(1)
        predecessorsList0.addPredecessor(integer2, integer0)
        integer3 = Integer(-3)

        with pytest.raises(RuntimeError):
            predecessorsList0.buildPath0(integer3, integer1)

    def test06(self) -> None:

        integer0 = -2
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = Mock(spec=Mapper)
        mapper0.map.side_effect = [integer0, None, None, None, None]
        predecessorsList0 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, mapper0
        )
        integer1 = -2
        predecessorsList0.addPredecessor(integer1, integer0)
        integer2 = -3
        # Undeclared exception
        predecessorsList0.buildPath0(integer2, integer1)

    def test05(self) -> None:

        integer0 = -2
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = Mock(Mapper)
        mapper0.map.side_effect = [integer0, None, None, None, None]
        predecessorsList0 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, mapper0
        )
        integer1 = -2
        predecessorsList0.addPredecessor(integer0, integer0)
        integer2 = 2
        # Undeclared exception handling is not necessary in Python, as it doesn't have checked exceptions
        predecessorsList0.buildPath1(integer2, integer1, integer1, predecessorsList0)

    def test04(self) -> None:

        integer0 = -2
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, new=ViolatedAssumptionAnswer())
        predecessorsList0 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, mapper0
        )
        integer1 = 1

        with pytest.raises(RuntimeError):
            predecessorsList0.buildPath1(integer0, integer1, integer0, None)
            verifyException(
                "org.apache.commons.graph.shortestpath.PredecessorsList", RuntimeError
            )

    def test03(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = Integer(2)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        predecessorsList0 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, mapper0
        )
        mapper1 = mock(Mapper, ViolatedAssumptionAnswer())
        predecessorsList1 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, mapper1
        )
        integer1 = Integer(1)

        try:
            predecessorsList1.buildPath1(
                integer0, integer0, integer1, predecessorsList0
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.shortestpath.PredecessorsList", e)

    def test02(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = Integer(2)
        integer1 = Integer(2)
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        mapper0 = Mock(Mapper)
        mapper0.map.side_effect = [integer1, integer1, integer1, integer1, integer0]
        predecessorsList0 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, mapper0
        )
        predecessorsList0.addPredecessor(integer0, integer1)
        integer2 = Integer(1)
        predecessorsList0.buildPath1(integer1, integer0, integer2, predecessorsList0)

    def test01(self) -> None:

        integer0 = -2
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map = Mock(return_value=None)
        predecessorsList0 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, mapper0
        )
        integer1 = 1
        predecessorsList0.addPredecessor(integer1, integer0)
        mapper1 = mock(Mapper, ViolatedAssumptionAnswer())
        predecessorsList1 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, mapper1
        )

        with pytest.raises(RuntimeError):
            predecessorsList0.buildPath1(
                integer0, integer1, integer0, predecessorsList1
            )

    def test00(self) -> None:

        integer0 = -2
        inMemoryPath0 = InMemoryPath(integer0, integer0)
        integer1 = 1
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = Mock(spec=Mapper)
        mapper0.map.return_value = None
        predecessorsList0 = PredecessorsList(
            inMemoryPath0, integerWeightBaseOperations0, mapper0
        )
        predecessorsList0.addPredecessor(integer1, integer0)
        weightedPath0 = predecessorsList0.buildPath1(
            integer1, integer1, integer0, predecessorsList0
        )
        self.assertIsNotNone(weightedPath0)
