from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.cli.Option import *


class DefaultOption(Option):

    __defaultValue: str = ""

    __serialVersionUID: int = 1

    def getValue0(self) -> str:
        return (
            super().getValue0()
            if super().getValue0() is not None
            else self.__defaultValue
        )

    def __init__(self, opt: str, description: str, defaultValue: str) -> None:
        super(-1, null, null, null, false, null)
        self.__defaultValue = defaultValue


class TestOption(Option):

    __serialVersionUID: int = 1

    def addValue(self, value: str) -> bool:
        self.addValueForProcessing(value)
        return True

    def __init__(self, opt: str, hasArg: bool, description: str) -> None:
        super().__init__(-1, opt, None, description, hasArg, None)


class OptionTest(unittest.TestCase):

    def testSubclass(self) -> None:
        option: Option = DefaultOption("f", "file", "myfile.txt")
        clone: Option = option.clone()
        self.assertEqual("myfile.txt", clone.getValue0())
        self.assertEqual(DefaultOption, clone.getClass())

    def testHashCode(self) -> None:
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test2").build().hashCode(),
        )
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder0().longOpt("test").build().hashCode(),
        )
        self.assertNotEqual(
            Option.builder1("test").build().hashCode(),
            Option.builder1("test").longOpt("long test").build().hashCode(),
        )

    def testHasArgs(self) -> None:
        option = Option.Option1("f", None)

        option.setArgs(0)
        self.assertFalse(option.hasArgs())

        option.setArgs(1)
        self.assertFalse(option.hasArgs())

        option.setArgs(10)
        self.assertTrue(option.hasArgs())

        option.setArgs(Option.UNLIMITED_VALUES)
        self.assertTrue(option.hasArgs())

        option.setArgs(Option.UNINITIALIZED)
        self.assertFalse(option.hasArgs())

    def testHasArgName(self) -> None:
        option = Option.Option1("f", None)

        option.setArgName(None)
        self.assertFalse(option.hasArgName())

        option.setArgName("")
        self.assertFalse(option.hasArgName())

        option.setArgName("file")
        self.assertTrue(option.hasArgName())

    def testGetValue(self) -> None:
        option: Option = Option.Option1("f", None)
        option.setArgs(Option.UNLIMITED_VALUES)

        self.assertEqual("default", option.getValue2("default"))
        self.assertIsNone(option.getValue1(0))

        option.addValueForProcessing("foo")

        self.assertEqual("foo", option.getValue0())
        self.assertEqual("foo", option.getValue1(0))
        self.assertEqual("foo", option.getValue2("default"))

    def testClone(self) -> None:
        a: TestOption = TestOption("a", True, "")
        b: TestOption = a.clone()
        self.assertEqual(a, b)
        self.assertNotEqual(a, b)
        a.setDescription("a")
        self.assertEqual("", b.getDescription())
        b.setArgs(2)
        b.addValue("b1")
        b.addValue("b2")
        self.assertEqual(1, a.getArgs())
        self.assertEqual(0, a.getValuesList().size())
        self.assertEqual(2, b.getValues().length)

    def testClear(self) -> None:
        option = TestOption("x", True, "")
        self.assertEqual(0, option.getValuesList().size())
        option.addValue("a")
        self.assertEqual(1, option.getValuesList().size())
        option.clearValues()
        self.assertEqual(0, option.getValuesList().size())

    def testBuilderMethods(self) -> None:
        defaultSeparator: str = "\u0000"

        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            defaultSeparator,
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            defaultSeparator,
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").longOpt("aaa").build(),
            "a",
            "desc",
            "aaa",
            Option.UNINITIALIZED,
            None,
            False,
            False,
            defaultSeparator,
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            defaultSeparator,
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            defaultSeparator,
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").hasArg1(True).build(),
            "a",
            "desc",
            None,
            1,
            None,
            False,
            False,
            defaultSeparator,
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").numberOfArgs(3).build(),
            "a",
            "desc",
            None,
            3,
            None,
            False,
            False,
            defaultSeparator,
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            True,
            False,
            defaultSeparator,
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").required1(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            defaultSeparator,
            str,
        )

        self.__checkOption(
            Option.builder1("a").desc("desc").argName("arg1").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            "arg1",
            False,
            False,
            defaultSeparator,
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(False).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            defaultSeparator,
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").optionalArg(True).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            True,
            defaultSeparator,
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").valueSeparator1(":").build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            ":",
            str,
        )
        self.__checkOption(
            Option.builder1("a").desc("desc").type(int).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            defaultSeparator,
            int,
        )
        self.__checkOption(
            Option.builder0().option("a").desc("desc").type(int).build(),
            "a",
            "desc",
            None,
            Option.UNINITIALIZED,
            None,
            False,
            False,
            defaultSeparator,
            int,
        )

    def testBuilderInvalidOptionName4(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder1("invalid@")

    def testBuilderInvalidOptionName3(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder1("invalid?")

    def testBuilderInvalidOptionName2(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder0().option("invalid@")

    def testBuilderInvalidOptionName1(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder0().option("invalid?")

    def testBuilderInsufficientParams2(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder1(None).desc("desc").build()

    def testBuilderInsufficientParams1(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder0().desc("desc").build()

    @staticmethod
    def __checkOption(
        option: Option,
        opt: str,
        description: str,
        longOpt: str,
        numArgs: int,
        argName: str,
        required: bool,
        optionalArg: bool,
        valueSeparator: str,
        cls: typing.Type[typing.Any],
    ) -> None:
        assert opt == option.getOpt()
        assert description == option.getDescription()
        assert longOpt == option.getLongOpt()
        assert numArgs == option.getArgs()
        assert argName == option.getArgName()
        assert required == option.isRequired()
        assert optionalArg == option.hasOptionalArg()
        assert valueSeparator == option.getValueSeparator()
        assert cls == option.getType()
