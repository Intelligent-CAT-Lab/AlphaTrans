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

        self.assertEqual(
            "testOverridePositionImplied(1) ", 3, len(self._field.getArgs("required"))
        )
        self.assertEqual(
            "testOverridePositionImplied(2) ",
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
        )
        self.assertEqual(
            "testOverridePositionImplied(3) ",
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
        )
        self.assertEqual(
            "testOverridePositionImplied(4) ",
            "required-position-2",
            self._field.getArg1("required", 2).getKey(),
        )

        self.assertEqual(
            "testOverridePositionImplied(5) ", 3, len(self._field.getArgs("mask"))
        )
        self.assertEqual(
            "testOverridePositionImplied(6) ",
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
        )
        self.assertEqual(
            "testOverridePositionImplied(7) ",
            "mask-position-1",
            self._field.getArg1("mask", 1).getKey(),
        )
        self.assertIsNone(
            "testOverridePositionImplied(8) ", self._field.getArg1("mask", 2)
        )

        self.assertEqual(
            "testOverridePositionImplied(9) ",
            "default-position-0",
            self._field.getArg0(0).getKey(),
        )
        self.assertIsNone("testOverridePositionImplied(10) ", self._field.getArg0(1))
        self.assertIsNone("testOverridePositionImplied(11) ", self._field.getArg0(2))

    def testOverrideUsingPositionB(self) -> None:

        self._field.addArg(self.__createArg3("required-position-3", "required", 3))
        self._field.addArg(self.__createArg3("required-position-1", "required", 1))
        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(
            "testOverrideUsingPositionB(1) ", 4, len(self._field.getArgs("required"))
        )
        self.assertEqual(
            "testOverrideUsingPositionB(2) ",
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
        )
        self.assertEqual(
            "testOverrideUsingPositionB(3) ",
            "required-position-1",
            self._field.getArg1("required", 1).getKey(),
        )
        self.assertEqual(
            "testOverrideUsingPositionB(4) ",
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
        )
        self.assertEqual(
            "testOverrideUsingPositionB(5) ",
            "required-position-3",
            self._field.getArg1("required", 3).getKey(),
        )

        self.assertEqual(
            "testOverrideUsingPositionB(6) ", 4, len(self._field.getArgs("mask"))
        )
        self.assertEqual(
            "testOverrideUsingPositionB(6) ",
            "default-position-0",
            self._field.getArg1("mask", 0).getKey(),
        )
        self.assertEqual(
            "testOverrideUsingPositionB(7) ",
            "default-position-1",
            self._field.getArg1("mask", 1).getKey(),
        )
        self.assertEqual(
            "testOverrideUsingPositionB(8) ",
            "default-position-2",
            self._field.getArg1("mask", 2).getKey(),
        )
        self.assertIsNone(
            "testOverrideUsingPositionB(9) ", self._field.getArg1("mask", 3)
        )

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

        self.assertEqual(
            "testDefaultSomePositions(1) ", 4, len(self._field.getArgs("required"))
        )
        self.assertEqual(
            "testDefaultSomePositions(2) ",
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
        )
        self.assertEqual(
            "testDefaultSomePositions(3) ",
            "default-position-1",
            self._field.getArg1("required", 1).getKey(),
        )
        self.assertEqual(
            "testDefaultSomePositions(4) ",
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
        )
        self.assertEqual(
            "testDefaultSomePositions(5) ",
            "default-position-3",
            self._field.getArg1("required", 3).getKey(),
        )

    def testDefaultOnePosition(self) -> None:

        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg1("default-position-2", 2))
        self._field.addArg(self.__createArg0("default-position-3"))

        self.assertEqual(
            "testDefaultOnePosition(1) ", 4, len(self._field.getArgs("required"))
        )
        self.assertEqual(
            "testDefaultOnePosition(2) ",
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
        )
        self.assertIsNone(
            "testDefaultOnePosition(3) ", self._field.getArg1("required", 1)
        )
        self.assertEqual(
            "testDefaultOnePosition(4) ",
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
        )
        self.assertEqual(
            "testDefaultOnePosition(5) ",
            "default-position-3",
            self._field.getArg1("required", 3).getKey(),
        )

    def testDefaultUsingPositions(self) -> None:

        self._field.addArg(self.__createArg1("default-position-1", 1))
        self._field.addArg(self.__createArg1("default-position-0", 0))
        self._field.addArg(self.__createArg1("default-position-2", 2))

        self.assertEqual(
            "testDefaultUsingPositions(1) ", 3, len(self._field.getArgs("required"))
        )
        self.assertEqual(
            "testDefaultUsingPositions(2) ",
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
        )
        self.assertEqual(
            "testDefaultUsingPositions(3) ",
            "default-position-1",
            self._field.getArg1("required", 1).getKey(),
        )
        self.assertEqual(
            "testDefaultUsingPositions(4) ",
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
        )

    def testDefaultPositionImplied(self) -> None:

        self._field.addArg(self.__createArg0("default-position-0"))
        self._field.addArg(self.__createArg0("default-position-1"))
        self._field.addArg(self.__createArg0("default-position-2"))

        self.assertEqual(
            "testDefaultPositionImplied(1) ", 3, len(self._field.getArgs("required"))
        )
        self.assertEqual(
            "testDefaultPositionImplied(2) ",
            "default-position-0",
            self._field.getArg1("required", 0).getKey(),
        )
        self.assertEqual(
            "testDefaultPositionImplied(3) ",
            "default-position-1",
            self._field.getArg1("required", 1).getKey(),
        )
        self.assertEqual(
            "testDefaultPositionImplied(4) ",
            "default-position-2",
            self._field.getArg1("required", 2).getKey(),
        )

    def testEmptyArgs(self) -> None:

        # Create an instance of Field
        field = Field()

        # Call the getArgs method and check if it returns an empty list
        self.assertEqual("Empty Args(1) ", 0, len(field.getArgs("required")))

    @staticmethod
    def FieldTest1() -> FieldTest:
        return FieldTest(None)

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
