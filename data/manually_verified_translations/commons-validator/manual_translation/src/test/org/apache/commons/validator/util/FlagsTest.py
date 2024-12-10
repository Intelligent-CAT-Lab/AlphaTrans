from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.util.Flags import *


class FlagsTest(unittest.TestCase):

    __INT_FLAG: int = 4
    __LONG_FLAG_2: int = 2
    __LONG_FLAG: int = 1

    def testToString(self) -> None:

        f = Flags(0, 0)
        s = f.toString()
        self.assertEqual(64, len(s))

        f.turnOn(self.__INT_FLAG)
        s = f.toString()
        self.assertEqual(64, len(s))

        expected = "0000000000000000000000000000000000000000000000000000000000000100"
        self.assertEqual(expected, s)

    def testEqualsObject(self) -> None:
        pass

    def testClone(self) -> None:
        pass

    def testIsOn_isTrueWhenHighOrderBitIsSetAndQueried(self) -> None:

        allOn = Flags(1, ~0)
        highOrderBit = 0x8000000000000000

        self.assertTrue(allOn.isOn(highOrderBit))

    def testIsOn_isFalseWhenNotAllFlagsInArgumentAreOn(self) -> None:

        first = Flags(1, 1)
        firstAndSecond = 3

        self.assertFalse(first.isOn(firstAndSecond))

    def testTurnOnAll(self) -> None:
        f = Flags(0, 0)
        f.turnOnAll()
        self.assertEqual(0xFFFFFFFFFFFFFFFF, f.getFlags())

    def testClear(self) -> None:
        f = Flags(1, 98432)
        f.clear()
        self.assertEqual(0, f.getFlags())

    def testTurnOffAll(self) -> None:
        f = Flags(1, 98432)
        f.turnOffAll()
        self.assertEqual(0, f.getFlags())

    def testTurnOff(self) -> None:
        pass

    def testTurnOnOff(self) -> None:
        pass

    def testIsOnOff(self) -> None:

        f = Flags(0, 0)
        f.turnOn(self.__LONG_FLAG)
        f.turnOn(self.__INT_FLAG)
        self.assertTrue(f.isOn(self.__LONG_FLAG))
        self.assertTrue(not f.isOff(self.__LONG_FLAG))

        self.assertTrue(f.isOn(self.__INT_FLAG))
        self.assertTrue(not f.isOff(self.__INT_FLAG))

        self.assertTrue(f.isOff(self.__LONG_FLAG_2))

    def testGetFlags(self) -> None:
        f = Flags(1, 45)
        self.assertEqual(f.getFlags(), 45)

    def testHashCode(self) -> None:
        f = Flags(1, 45)
        self.assertEqual(f.hashCode(), 45)

    def __init__(self, name: str) -> None:
        super().__init__(name)
