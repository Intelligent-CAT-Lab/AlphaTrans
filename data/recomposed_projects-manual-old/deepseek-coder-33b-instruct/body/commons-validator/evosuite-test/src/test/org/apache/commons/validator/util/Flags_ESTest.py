from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.util.Flags import *

# from src.test.org.apache.commons.validator.util.Flags_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Flags_ESTest(unittest.TestCase):

    def test18(self) -> None:

        flags0 = Flags(1, 1)
        self.assertEqual(1, flags0.getFlags())

        flags0.turnOff(1)
        self.assertEqual(0, flags0.getFlags())

    def test17(self) -> None:

        flags0 = Flags(1, 1767)
        flags0.clear()
        self.assertEqual(0, flags0.getFlags())

    def test16(self) -> None:

        flags0 = Flags(1, 1767)
        long0 = flags0.getFlags()
        self.assertEqual(0, long0)

    def test15(self) -> None:

        flags0 = Flags(1, 1767)
        object0 = flags0.clone()
        flags0.turnOnAll()
        boolean0 = flags0.equals(object0)
        self.assertFalse(boolean0)
        self.assertEqual(-1, flags0.getFlags())

    def test14(self) -> None:

        flags0 = Flags(1, 1)
        flags0.hashCode()
        self.assertEqual(1, flags0.getFlags())

    def test13(self) -> None:

        flags0 = Flags(1, 702)
        boolean0 = flags0.isOn(702)
        self.assertEqual(0, flags0.getFlags())
        self.assertFalse(boolean0)

    def test12(self) -> None:

        flags0 = Flags(1, 702)
        self.assertEqual(0, flags0.getFlags())

        flags0.turnOnAll()
        boolean0 = flags0.isOn(-1746)
        self.assertEqual(-1, flags0.getFlags())
        self.assertTrue(boolean0)

    def test11(self) -> None:

        flags0 = Flags(1, 702)
        self.assertEqual(0, flags0.getFlags())

        flags0.turnOnAll()
        boolean0 = flags0.isOff(-1746)
        self.assertEqual(-1, flags0.getFlags())
        self.assertFalse(boolean0)

    def test10(self) -> None:

        flags0 = Flags(1, 1)
        self.assertEqual(1, flags0.getFlags())

        flags0.turnOffAll()
        boolean0 = flags0.isOff(1)
        self.assertTrue(boolean0)

    def test09(self) -> None:

        flags0 = Flags(1, 1)
        boolean0 = flags0.equals(flags0)
        self.assertTrue(boolean0)
        self.assertEqual(1, flags0.getFlags())

    def test08(self) -> None:

        flags0 = Flags(1, 1)
        object0 = object()
        boolean0 = flags0.equals(object0)
        self.assertFalse(boolean0)
        self.assertEqual(1, flags0.getFlags())

    def test07(self) -> None:

        flags0 = Flags(1, 1)
        flags1 = flags0.clone()
        boolean0 = flags0.equals(flags1)
        self.assertTrue(boolean0)
        self.assertEqual(1, flags1.getFlags())

    def test06(self) -> None:

        flags0 = Flags(1, 1)
        string0 = flags0.toString()
        self.assertEqual(
            "0000000000000000000000000000000000000000000000000000000000000001", string0
        )

    def test05(self) -> None:

        flags0 = Flags(2211, 2211)
        self.assertEqual(0, flags0.getFlags())

        flags0.turnOnAll()
        long0 = flags0.getFlags()
        self.assertEqual(-1, long0)

    def test04(self) -> None:

        flags0 = Flags(7, 7)
        self.assertEqual(0, flags0.getFlags())

        flags0.turnOn(1)
        long0 = flags0.getFlags()
        self.assertEqual(1, long0)

    def test03(self) -> None:

        flags0 = Flags(-237, -237)
        boolean0 = flags0.isOn(-1098)
        self.assertFalse(boolean0)
        self.assertEqual(0, flags0.getFlags())

    def test02(self) -> None:

        flags0 = Flags(2211, 2211)
        self.assertEqual(0, flags0.getFlags())

        flags0.turnOn(2211)
        boolean0 = flags0.isOff(2211)
        self.assertEqual(2211, flags0.getFlags())
        self.assertFalse(boolean0)

    def test01(self) -> None:

        flags0 = Flags(0, 0)
        self.assertEqual(0, flags0.getFlags())

        flags0.turnOnAll()
        flags0.turnOn(-1943)
        self.assertEqual(-1, flags0.getFlags())

    def test00(self) -> None:

        flags0 = Flags(1, 1575)
        flags0.turnOn(1575)
        flags1 = Flags(1, 4099)
        boolean0 = flags0.equals(flags1)
        self.assertEqual(0, flags1.getFlags())
        self.assertEqual(1575, flags0.getFlags())
        self.assertFalse(boolean0)
