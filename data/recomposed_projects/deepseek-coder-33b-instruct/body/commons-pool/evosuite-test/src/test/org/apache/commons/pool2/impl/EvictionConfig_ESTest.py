from __future__ import annotations
import time
import re
import os
import datetime
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.EvictionConfig import *

# from src.test.org.apache.commons.pool2.impl.EvictionConfig_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class EvictionConfig_ESTest(unittest.TestCase):

    def test13(self) -> None:

        evictionConfig0 = EvictionConfig.EvictionConfig0(14, 14, 14)
        int0 = evictionConfig0.getMinIdle()
        self.assertEqual(14, int0)

    def test12(self) -> None:

        chronoUnit0 = datetime.timedelta(days=1000000000)
        duration0 = chronoUnit0
        evictionConfig0 = EvictionConfig(duration0, duration0, 1)

        try:
            evictionConfig0.getIdleSoftEvictTime()
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticError as e:
            self.verifyException("java.lang.Math", e)

    def test11(self) -> None:

        chronoUnit0 = datetime.timedelta(microseconds=1)
        duration0 = chronoUnit0
        evictionConfig0 = EvictionConfig(duration0, duration0, 0)
        string0 = evictionConfig0.toString()
        self.assertEqual(
            "EvictionConfig [idleEvictDuration=PT0.000001S, idleSoftEvictDuration=PT0.000001S, minIdle=0]",
            string0,
        )

    def test10(self) -> None:

        chronoUnit0 = datetime.timedelta(microseconds=1)
        duration0 = chronoUnit0
        evictionConfig0 = EvictionConfig(duration0, duration0, 0)
        duration1 = evictionConfig0.getIdleEvictDuration()
        self.assertEqual(duration1, duration0)
        self.assertEqual(evictionConfig0.getMinIdle(), 0)

    def test09(self) -> None:

        evictionConfig0 = EvictionConfig(None, None, -2632)
        duration0 = evictionConfig0.getIdleEvictTimeDuration()
        self.assertIsNotNone(duration0)
        self.assertEqual(-2632, evictionConfig0.getMinIdle())

    def test08(self) -> None:

        chronoUnit0 = datetime.timedelta(microseconds=1)
        duration0 = chronoUnit0
        evictionConfig0 = EvictionConfig(duration0, duration0, 0)
        duration1 = evictionConfig0.getIdleSoftEvictTimeDuration()
        self.assertEqual(0, evictionConfig0.getMinIdle())
        self.assertIs(duration1, duration0)

    def test07(self) -> None:

        chronoUnit0 = datetime.timedelta(microseconds=1)
        duration0 = chronoUnit0
        evictionConfig0 = EvictionConfig(duration0, duration0, 0)
        long0 = evictionConfig0.getIdleEvictTime()
        self.assertEqual(0, long0)
        self.assertEqual(0, evictionConfig0.getMinIdle())

    def test06(self) -> None:

        chronoUnit0 = datetime.timedelta(microseconds=1)
        duration0 = chronoUnit0
        evictionConfig0 = EvictionConfig(duration0, duration0, 0)
        duration1 = evictionConfig0.getIdleSoftEvictDuration()
        self.assertIs(duration1, duration0)
        self.assertEqual(0, evictionConfig0.getMinIdle())

    def test05(self) -> None:

        chronoUnit0 = datetime.timedelta(eras=1)
        duration0 = chronoUnit0
        evictionConfig0 = EvictionConfig(duration0, duration0, -14)

        try:
            evictionConfig0.getIdleEvictTime()
            self.fail("Expecting exception: ArithmeticException")

        except ArithmeticError as e:
            self.verifyException("java.lang.Math", e)

    def test04(self) -> None:

        evictionConfig0 = EvictionConfig.EvictionConfig0(-3075, 0, 0)
        long0 = evictionConfig0.getIdleEvictTime()
        self.assertEqual(0, evictionConfig0.getMinIdle())
        self.assertEqual(9223372036854775807, long0)

    def test03(self) -> None:

        evictionConfig0 = EvictionConfig.EvictionConfig0(-3075, 0, 0)
        long0 = evictionConfig0.getIdleSoftEvictTime()
        self.assertEqual(9223372036854775807, long0)
        self.assertEqual(0, evictionConfig0.getMinIdle())

    def test02(self) -> None:

        chronoUnit0 = datetime.timedelta(microseconds=1)
        duration0 = chronoUnit0
        evictionConfig0 = EvictionConfig(duration0, duration0, 0)
        long0 = evictionConfig0.getIdleSoftEvictTime()
        self.assertEqual(0, long0)
        self.assertEqual(0, evictionConfig0.getMinIdle())

    def test01(self) -> None:

        evictionConfig0 = EvictionConfig.EvictionConfig0(5, 1371, -1)
        int0 = evictionConfig0.getMinIdle()
        self.assertEqual(-1, int0)

    def test00(self) -> None:

        evictionConfig0 = EvictionConfig.EvictionConfig0(0, -2632, 0)
        int0 = evictionConfig0.getMinIdle()
        self.assertEqual(0, int0)
