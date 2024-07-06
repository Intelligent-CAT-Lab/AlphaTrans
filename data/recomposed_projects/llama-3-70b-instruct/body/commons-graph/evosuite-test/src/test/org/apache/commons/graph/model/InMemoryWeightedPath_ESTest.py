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
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *

# from src.test.org.apache.commons.graph.model.InMemoryWeightedPath_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class InMemoryWeightedPath_ESTest(unittest.TestCase):

    def test16(self) -> None:

        integer0 = Integer(0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, None
        )
        inMemoryWeightedPath1 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, None
        )
        boolean0 = inMemoryWeightedPath0.equals(inMemoryWeightedPath1)
        self.assertTrue(boolean0)

    def test15(self) -> None:

        integer0 = Integer(8)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, None
        )

        try:
            inMemoryWeightedPath0.addConnectionInTail(integer0, integer0, integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.InMemoryWeightedPath", e)

    def test14(self) -> None:

        integer0 = Integer(-1764)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, None
        )
        string0 = inMemoryWeightedPath0.to_string()
        self.assertEqual("InMemoryPath [weigth=0, vertices=[], edges=[]]", string0)

    def test13(self) -> None:

        integer0 = Integer(-1764)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, None
        )

        with self.assertRaises(RuntimeError):
            inMemoryWeightedPath0.addConnectionInHead(integer0, integer0, integer0)

    def test12(self) -> None:

        integer0 = Integer(0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, None
        )
        boolean0 = inMemoryWeightedPath0.equals(inMemoryWeightedPath0)
        self.assertTrue(boolean0)

    def test11(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = Integer(31)
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, None
        )
        boolean0 = inMemoryWeightedPath0.equals(integerWeightBaseOperations0)
        self.assertFalse(boolean0)

    def test10(self) -> None:

        integer0 = Integer(8)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, None
        )
        inMemoryWeightedPath0.hashCode()

    def test09(self) -> None:

        comparable0 = unittest.mock.Mock(spec=Comparable)
        monoid0 = unittest.mock.Mock(spec=Monoid)
        monoid0.identity.return_value = None
        mapper0 = unittest.mock.Mock(spec=Mapper)

        inMemoryWeightedPath0 = InMemoryWeightedPath(
            comparable0, comparable0, monoid0, mapper0
        )
        inMemoryWeightedPath0.hashCode()

    def test08(self) -> None:

        integer0 = Integer(31)
        monoid0 = mock(Monoid, ViolatedAssumptionAnswer())
        monoid0.identity.return_value = None
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, monoid0, mapper0
        )
        inMemoryWeightedPath1 = inMemoryWeightedPath0.getWeight()
        self.assertIsNone(inMemoryWeightedPath1)

    def test07(self) -> None:

        integer0 = Integer(0)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        inMemoryWeightedPath0 = None

        try:
            inMemoryWeightedPath0 = InMemoryWeightedPath(
                None, integer0, integerWeightBaseOperations0, None
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Path source cannot be null
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test06(self) -> None:

        integer0 = -27
        inMemoryWeightedPath0 = None

        try:
            inMemoryWeightedPath0 = InMemoryWeightedPath(integer0, integer0, None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.InMemoryWeightedPath", e)

    def test05(self) -> None:

        integer0 = Integer(8)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, None
        )

        with pytest.raises(RuntimeError):
            inMemoryWeightedPath0.addConnectionInHead(None, integer0, None)

    def test04(self) -> None:

        integer0 = Integer(8)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, None
        )

        with pytest.raises(RuntimeError):
            inMemoryWeightedPath0.addConnectionInTail(integer0, integer0, None)
            verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test03(self) -> None:

        object0 = object()
        monoid0 = mock(Monoid, ViolatedAssumptionAnswer)
        monoid0.identity.return_value = None
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer)
        inMemoryWeightedPath0 = InMemoryWeightedPath(object0, object0, monoid0, mapper0)
        iterable0 = inMemoryWeightedPath0.getVertices0()
        integer0 = Integer(1)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper1 = mock(Mapper, ViolatedAssumptionAnswer)
        inMemoryWeightedPath1 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, mapper1
        )

        with pytest.raises(StackOverflowError):
            inMemoryWeightedPath0.addConnectionInTail(
                iterable0, object0, inMemoryWeightedPath1
            )

    def test02(self) -> None:

        integer0 = Integer(31)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, new=ViolatedAssumptionAnswer())
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer0, integerWeightBaseOperations0, mapper0
        )
        monoid0 = mock(Monoid, new=ViolatedAssumptionAnswer())
        monoid0.identity.return_value = inMemoryWeightedPath0
        mapper1 = mock(Mapper, new=ViolatedAssumptionAnswer())
        inMemoryWeightedPath1 = InMemoryWeightedPath(
            integer0, integer0, monoid0, mapper1
        )
        inMemoryWeightedPath2 = inMemoryWeightedPath1.getWeight()
        self.assertEqual(0, inMemoryWeightedPath2.getSize())

    def test01(self) -> None:

        integer0 = Integer(1264)
        integer1 = Integer.getInteger("", 1264)
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map = Mock(return_value=None)
        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer0, integer1, integerWeightBaseOperations0, mapper0
        )
        mapper1 = mock(Mapper, ViolatedAssumptionAnswer())
        inMemoryWeightedPath1 = InMemoryWeightedPath(
            integer1, integer0, integerWeightBaseOperations0, mapper1
        )
        inMemoryWeightedPath0.addConnectionInHead(
            integer0, inMemoryWeightedPath1, integer1
        )
        self.assertEqual(2, inMemoryWeightedPath0.getOrder())

    def test00(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = -1463
        integer1 = integerWeightBaseOperations0.inverse(integer0)

        mapper0 = Mock(spec=Mapper)
        mapper0.map.return_value = None

        inMemoryWeightedPath0 = InMemoryWeightedPath(
            integer1, integer1, integerWeightBaseOperations0, mapper0
        )
        inMemoryWeightedPath0.addConnectionInTail(integer1, integer0, integer1)

        self.assertEqual(2, inMemoryWeightedPath0.getOrder())
