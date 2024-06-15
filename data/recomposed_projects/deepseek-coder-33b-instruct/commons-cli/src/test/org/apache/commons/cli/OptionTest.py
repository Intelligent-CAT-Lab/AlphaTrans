from __future__ import annotations
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.cli.Option import *


class DefaultOption(Option):

    __defaultValue: str = None

    __serialVersionUID: int = 1

    def getValue0(self) -> str:

        return (
            super().getValue0()
            if super().getValue0() is not None
            else self.__defaultValue
        )

    def __init__(self, opt: str, description: str, defaultValue: str) -> None:

        super().__init__(-1, None, None, None, False, None)
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

        class DefaultOption(Option):
            def __init__(self, opt: str, description: str, defaultValue: str) -> None:
                self.opt = opt
                self.description = description
                self.defaultValue = defaultValue

            def clone(self) -> Option:
                return DefaultOption(self.opt, self.description, self.defaultValue)

            def getValue0(self) -> str:
                return self.defaultValue

        option = DefaultOption("f", "file", "myfile.txt")
        clone = option.clone()
        assert clone.getValue0() == "myfile.txt"
        assert type(clone) == DefaultOption

    def testHashCode(self) -> None:

        assert (
            Option.builder1("test").build().hashCode()
            != Option.builder1("test2").build().hashCode()
        )
        assert (
            Option.builder1("test").build().hashCode()
            != Option.builder0().longOpt("test").build().hashCode()
        )
        assert (
            Option.builder1("test").build().hashCode()
            != Option.builder1("test").longOpt("long test").build().hashCode()
        )

    def testHasArgs(self) -> None:

        option = Option.Option1("f", None)

        option.setArgs(0)
        assert not option.hasArgs()

        option.setArgs(1)
        assert not option.hasArgs()

        option.setArgs(10)
        assert option.hasArgs()

        option.setArgs(Option.UNLIMITED_VALUES)
        assert option.hasArgs()

        option.setArgs(Option.UNINITIALIZED)
        assert not option.hasArgs()

    def testHasArgName(self) -> None:

        option = Option.Option1("f", None)

        option.setArgName(None)
        assert not option.hasArgName()

        option.setArgName("")
        assert not option.hasArgName()

        option.setArgName("file")
        assert option.hasArgName()

    def testGetValue(self) -> None:

        option = Option.Option1("f", None)
        option.setArgs(Option.UNLIMITED_VALUES)

        assert "default" == option.getValue2("default")
        assert None == option.getValue1(0)

        option.addValueForProcessing("foo")

        assert "foo" == option.getValue0()
        assert "foo" == option.getValue1(0)
        assert "foo" == option.getValue2("default")

    def testClone(self) -> None:

        a = TestOption("a", True, "")
        b = a.clone()
        assert a == b
        assert a is not b
        a.setDescription("a")
        assert b.getDescription() == ""
        b.setArgs(2)
        b.addValue("b1")
        b.addValue("b2")
        assert a.getArgs() == 1
        assert len(a.getValuesList()) == 0
        assert len(b.getValues()) == 2

    def testClear(self) -> None:

        option = TestOption("x", True, "")
        assert len(option.getValuesList()) == 0
        option.addValue("a")
        assert len(option.getValuesList()) == 1
        option.clearValues()
        assert len(option.getValuesList()) == 0

    def testBuilderMethods(self) -> None:

        defaultSeparator = chr(0)

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

        # Assuming that the Option class has a static method builder1
        # If it's an instance method, you would need to create an instance of Option first
        Option.builder1("invalid@")

    def testBuilderInvalidOptionName3(self) -> None:

        Option.builder1("invalid?")

    def testBuilderInvalidOptionName2(self) -> None:

        # Assuming that the Option.builder0() method returns an instance of Builder class
        # and the Builder.option() method takes a string as an argument
        # and returns an instance of Option class

        Option.builder0().option("invalid@")

    def testBuilderInvalidOptionName1(self) -> None:

        # Calling the Option.builder0() method
        builder = Option.builder0()

        # Calling the option method on the builder object
        builder.option("invalid?")

    def testBuilderInsufficientParams2(self) -> None:

        Option.builder1(None).desc("desc").build()

    def testBuilderInsufficientParams1(self) -> None:

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
