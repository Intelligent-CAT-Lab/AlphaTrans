from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.validator.Arg import *
from src.main.org.apache.commons.validator.Field import *


class FieldTest(unittest.TestCase):

    _field: typing.Any = None

    def tearDown(self) -> None:
        self._field = None

    def setUp(self) -> None:
        self._field = Field()

    def testOverrideSomePosition(self) -> None:

        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-3", "mask"))

        self.assertEqual(
            "testOverrideSomePosition(1) ", 4, len(self._field.getArgs("required"))
        )
        self.assertEqual(
            "testOverrideSomePosition(2) ",
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
        )
        self.assertEqual(
            "testOverrideSomePosition(3) ",
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
        )
        self.assertEqual(
            "testOverrideSomePosition(4) ",
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
        )
        self.assertIsNone(
            "testOverrideSomePosition(5) ", self._field.getArg1("required", 3)
        )

        self.assertEqual(
            "testOverrideSomePosition(6) ", 4, len(self._field.getArgs("mask"))
        )
        self.assertEqual(
            "testOverrideSomePosition(7) ",
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
        )
        self.assertEqual(
            "testOverrideSomePosition(8) ",
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
        )
        self.assertEqual(
            "testOverrideSomePosition(9) ",
            "default-position-2",
            self._field.getArg1("mask", 2).getKey(),
        )
        self.assertEqual(
            "testOverrideSomePosition(10) ",
            "mask-position-3",
            self._field.getArg1("mask", 3).getKey(),
        )

        self.assertEqual(
            "testOverrideSomePosition(11) ",
            "default-position-0",
            self._field.getArg0(0).getKey(),
        )
        self.assertEqual(
            "testOverrideSomePosition(12) ",
            "default-position-1",
            self._field.getArg0(1).getKey(),
        )
        self.assertEqual(
            "testOverrideSomePosition(13) ",
            "default-position-2",
            self._field.getArg0(2).getKey(),
        )
        self.assertIsNone("testOverrideSomePosition(14) ", self._field.getArg0(3))

    def testOverridePositionImplied(self) -> None:

        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg2("required-position-1", "required"))
        self._field.addArg(self.__createArg2("required-position-2", "required"))
        self._field.addArg(self.__createArg2("mask-position-1", "mask"))

        self.assertEqual(3, len(self._field.getArgs("required")))
        self.assertEqual(
            "default-position-0", self._field.getArg1("required", 0).getKey()
        )
        self.assertEqual(
            "required-position-1", self._field.getArg1("required", 1).getKey()
        )
        self.assertEqual(
            "required-position-2", self._field.getArg1("required", 2).getKey()
        )

        self.assertEqual(3, len(self._field.getArgs("mask")))
        self.assertEqual("default-position-0", self._field.getArg1("mask", 0).getKey())
        self.assertEqual("mask-position-1", self._field.getArg1("mask", 1).getKey())
        self.assertIsNone(self._field.getArg1("mask", 2))

        self.assertEqual("default-position-0", self._field.getArg0(0).getKey())
        self.assertIsNone(self._field.getArg0(1))
        self.assertIsNone(self._field.getArg0(2))

    def testOverrideUsingPositionB(self) -> None:

        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(4, len(self._field.getArgs("required")))
        self.assertEqual(
            "default-position-0", self._field.getArg1("required", 0).getKey()
        )
        self.assertEqual(
            "required-position-1", self._field.getArg1("required", 1).getKey()
        )
        self.assertEqual(
            "default-position-2", self._field.getArg1("required", 2).getKey()
        )
        self.assertEqual(
            "required-position-3", self._field.getArg1("required", 3).getKey()
        )

        self.assertEqual(4, len(self._field.getArgs("mask")))
        self.assertEqual("default-position-0", self._field.getArg1("mask", 0).getKey())
        self.assertEqual("default-position-1", self._field.getArg1("mask", 1).getKey())
        self.assertEqual("default-position-2", self._field.getArg1("mask", 2).getKey())
        self.assertIsNone(self._field.getArg1("mask", 3))

    def testOverrideUsingPositionA(self) -> None:

        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))

        self.assertEqual(
            "testOverrideUsingPositionA(1) ", 3, len(self._field.getArgs("required"))
        )
        self.assertEqual(
            "testOverrideUsingPositionA(2) ",
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
        )

        self.assertEqual(
            "testOverrideUsingPositionA(3) ", 3, len(self._field.getArgs("mask"))
        )
        self.assertEqual(
            "testOverrideUsingPositionA(4) ",
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
        )

        self.assertEqual(
            "testOverrideUsingPositionA(5) ",
            "default-position-1",
            self._field.getArg0(1).getKey(),
        )

    def testDefaultSomePositions(self) -> None:

        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg1("default-position-2", 2))
        self._field.addArg(self.__createArg0("default-position-3"))
        self._field.addArg(self.__createArg1("default-position-1", 1))

        self.assertEqual(4, len(self._field.getArgs("required")))
        self.assertEqual(
            "default-position-0", self._field.getArg1("required", 0).getKey()
        )
        self.assertEqual(
            "default-position-1", self._field.getArg1("required", 1).getKey()
        )
        self.assertEqual(
            "default-position-2", self._field.getArg1("required", 2).getKey()
        )
        self.assertEqual(
            "default-position-3", self._field.getArg1("required", 3).getKey()
        )

    def testDefaultOnePosition(self) -> None:

        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg1("default-position-2", 2))
        self._field.addArg(self.__createArg0("default-position-3"))

        self.assertEqual(4, len(self._field.getArgs("required")))
        self.assertEqual(
            "default-position-0", self._field.getArg1("required", 0).getKey()
        )
        self.assertIsNone(self._field.getArg1("required", 1))
        self.assertEqual(
            "default-position-2", self._field.getArg1("required", 2).getKey()
        )
        self.assertEqual(
            "default-position-3", self._field.getArg1("required", 3).getKey()
        )

    def testDefaultUsingPositions(self) -> None:

        self._field.addArg(self.__createArg1("default-position-1", 1))
        self._field.addArg(self.__createArg1("default-position-0", 0))
        self._field.addArg(self.__createArg1("default-position-2", 2))

        self.assertEqual(3, len(self._field.getArgs("required")))
        self.assertEqual(
            "default-position-0", self._field.getArg1("required", 0).getKey()
        )
        self.assertEqual(
            "default-position-1", self._field.getArg1("required", 1).getKey()
        )
        self.assertEqual(
            "default-position-2", self._field.getArg1("required", 2).getKey()
        )

    def testDefaultPositionImplied(self) -> None:

        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(3, len(self._field.getArgs("required")))
        self.assertEqual(
            "default-position-0", self._field.getArg1("required", 0).getKey()
        )
        self.assertEqual(
            "default-position-1", self._field.getArg1("required", 1).getKey()
        )
        self.assertEqual(
            "default-position-2", self._field.getArg1("required", 2).getKey()
        )

    def testEmptyArgs(self) -> None:

        # Assuming that _field is an instance of Field class
        self.assertEqual(0, len(self._field.getArgs("required")))

    @staticmethod
    def FieldTest1() -> FieldTest:
        return FieldTest(None)

    def __init__(self, name: str) -> None:
        self._name = name

    def __createArg3(self, key: str, name: str, position: int) -> Arg:
        arg = self.__createArg2(key, name)
        arg.setPosition(position)
        return arg

    def __createArg2(self, key: str, name: str) -> Arg:
        arg = self.__createArg0(key)
        arg.setName(name)
        return arg

    def __createArg1(self, key: str, position: int) -> Arg:
        arg = self.__createArg0(key)
        arg.setPosition(position)
        return arg

    def __createArg0(self, key: str) -> Arg:
        arg = Arg()
        arg.setKey(key)
        return arg
