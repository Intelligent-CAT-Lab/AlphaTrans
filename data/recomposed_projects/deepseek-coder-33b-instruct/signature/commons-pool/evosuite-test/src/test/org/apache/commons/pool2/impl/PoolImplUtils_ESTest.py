from __future__ import annotations
import time
import re
import os
import datetime
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *

# from src.test.org.apache.commons.pool2.impl.PoolImplUtils_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class PoolImplUtils_ESTest(unittest.TestCase):

    def test26(self) -> None:

        timeUnit0 = datetime.timedelta(minutes=1)
        duration0 = PoolImplUtils.toDuration(-700, timeUnit0)
        boolean0 = PoolImplUtils.isPositive(duration0)
        self.assertFalse(boolean0)

    def test25(self) -> None:
        poolImplUtils0 = PoolImplUtils()

    def test24(self) -> None:

        class0 = PooledObjectFactory
        class1 = PoolImplUtils.getFactoryType(class0)
        self.assertIsNone(class1)

    def test23(self) -> None:
        boolean0 = PoolImplUtils.isPositive(None)
        self.assertFalse(boolean0)

    def test22(self) -> None:

        duration0 = datetime.timedelta(hours=1001)
        boolean0 = PoolImplUtils.isPositive(duration0)
        self.assertTrue(boolean0)

    def test21(self) -> None:

        duration0 = datetime.timedelta(milliseconds=0)
        boolean0 = PoolImplUtils.isPositive(duration0)
        self.assertFalse(boolean0)

    def test20(self) -> None:

        instant0 = datetime.datetime.fromtimestamp(1022)
        instant1 = PoolImplUtils.max(instant0, instant0)
        self.assertIs(instant0, instant1)

    def test19(self) -> None:

        instant0 = datetime.datetime.fromtimestamp(1)
        instant1 = instant0 + datetime.timedelta(milliseconds=1)
        instant2 = PoolImplUtils.max(instant1, instant0)
        self.assertIsNot(instant2, instant0)

    def test18(self) -> None:

        instant0 = datetime.datetime.fromtimestamp(1022)
        instant1 = PoolImplUtils.min(instant0, instant0)
        self.assertIs(instant1, instant0)

    def test17(self) -> None:

        instant0 = datetime.datetime.fromtimestamp(1022)
        instant1 = datetime.datetime.fromtimestamp(instant0.timestamp() - 1022)
        instant2 = PoolImplUtils.min(instant1, instant0)
        self.assertIs(instant2, instant1)

    def test16(self) -> None:

        timeUnit0 = datetime.timedelta(microseconds=1)
        chronoUnit0 = PoolImplUtils.toChronoUnit(timeUnit0)
        self.assertEqual(datetime.timedelta(microseconds=1), chronoUnit0)

    def test15(self) -> None:

        timeUnit0 = datetime.timedelta(microseconds=1)
        chronoUnit0 = PoolImplUtils.toChronoUnit(timeUnit0)
        self.assertEqual(datetime.timedelta(microseconds=1), chronoUnit0)

    def test14(self) -> None:

        timeUnit0 = datetime.timedelta(milliseconds=1)
        chronoUnit0 = PoolImplUtils.toChronoUnit(timeUnit0)
        self.assertEqual(datetime.timedelta(milliseconds=1), chronoUnit0)

    def test13(self) -> None:

        timeUnit0 = datetime.timedelta(seconds=1)
        duration0 = PoolImplUtils.toDuration(-982, timeUnit0)
        self.assertIsNotNone(duration0)

    def test12(self) -> None:

        timeUnit0 = datetime.timedelta(hours=1)
        duration0 = PoolImplUtils.toDuration(-1069, timeUnit0)
        self.assertIsNotNone(duration0)

    def test11(self) -> None:

        timeUnit0 = datetime.timedelta(days=1)
        chronoUnit0 = PoolImplUtils.toChronoUnit(timeUnit0)
        self.assertEqual(datetime.timedelta(days=1), chronoUnit0)

    def test10(self) -> None:

        duration0 = datetime.timedelta(days=0)
        duration1 = PoolImplUtils.nonNull(None, duration0)
        self.assertIs(duration1, duration0)

    def test09(self) -> None:

        timeUnit0 = datetime.timedelta(minutes=1)
        duration0 = PoolImplUtils.toDuration(-700, timeUnit0)
        duration1 = PoolImplUtils.nonNull(duration0, duration0)
        self.assertIs(duration0, duration1)

    def test08(self) -> None:

        class0 = PoolImplUtils.getFactoryType(None)
        self.assertIsNone(class0)

    def test05(self) -> None:

        with pytest.raises(RuntimeError):
            PoolImplUtils.nonNull(None, None)

    def test04(self) -> None:

        # Undeclared exception
        try:
            PoolImplUtils.toChronoUnit(None)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            # no message in exception (getMessage() returned null)
            self.assertEqual(str(e), "timeUnit cannot be None")

    def test03(self) -> None:

        # Undeclared exception
        try:
            PoolImplUtils.toDuration(1555, None)
            self.fail("Expecting exception: RuntimeError")

        except ValueError as e:
            # no message in exception (getMessage() returned null)
            self.assertEqual(str(e), "timeUnit cannot be None")

    def test02(self) -> None:

        instant0 = datetime.datetime.fromtimestamp(1022)
        instant1 = instant0 - datetime.timedelta(seconds=700)
        instant2 = PoolImplUtils.max(instant0, instant1)
        self.assertEqual(instant2, instant1)

    def test01(self) -> None:

        instant0 = datetime.datetime.fromtimestamp(1022)
        instant1 = instant0 - datetime.timedelta(seconds=700)
        instant2 = PoolImplUtils.min(instant1, instant0)
        self.assertIsNot(instant2, instant1)

    def test00(self) -> None:

        chronoUnit0 = datetime.timedelta.max
        duration0 = chronoUnit0
        duration1 = datetime.timedelta(seconds=-1069)
        duration2 = PoolImplUtils.nonNull(duration1, duration0)
        self.assertIs(duration2, duration1)
