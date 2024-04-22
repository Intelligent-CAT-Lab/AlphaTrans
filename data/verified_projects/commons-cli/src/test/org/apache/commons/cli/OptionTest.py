# Imports Begin
from src.main.org.apache.commons.cli.Option import *
import unittest
import typing
from typing import *

# Imports End

class OptionTest(unittest.TestCase):
    #Inner Classes Start
    class DefaultOption(Option):
        # Class Fields Begin
        __serialVersionUID: int = 1
        # Class Fields End

        # Class Methods Begin
        def __init__(self, opt: str, description: str, defaultValue: str) -> None:
            super().__init__(-1, None, None, None, False, None)
            self.__defaultValue = defaultValue

        
        def getValue0(self) -> str:
            # No need to check if super().getValue0() is not None in Python
            # Python will raise AttributeError if the attribute doesn't exist
            return (
                super().getValue0()
                if super().getValue0() is not None
                else self.__defaultValue
            )
        
        # Class Methods End
    
    class TestOption(Option):
        # Class Fields Begin
        __serialVersionUID: int = 1
        # Class Fields End

        # Class Methods Begin
        def __init__(self, opt, hasArg, description):
            super().__init__(-1, opt, None, description, hasArg, None)


        def addValue(self, value: str) -> bool:
            self.addValueForProcessing(value)
            return True

        # Class Methods End

    # Inner Classes End
        
    # Class Methods Begin
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
        unittest.TestCase().assertEqual(opt, option.getOpt())
        unittest.TestCase().assertEqual(description, option.getDescription())
        unittest.TestCase().assertEqual(longOpt, option.getLongOpt())
        unittest.TestCase().assertEqual(numArgs, option.getArgs())
        unittest.TestCase().assertEqual(argName, option.getArgName())
        unittest.TestCase().assertEqual(required, option.isRequired())

        unittest.TestCase().assertEqual(optionalArg, option.hasOptionalArg())
        unittest.TestCase().assertEqual(valueSeparator, option.getValueSeparator())
        unittest.TestCase().assertEqual(cls, type(option))
    

    def test_BuilderInsufficientParams1(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder0().desc("desc").build()

    
    def test_BuilderInsufficientParams2(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder1(None).desc("desc").build()
    
    
    def test_BuilderInvalidOptionName1(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder0().option("invalid?")
    
    
    def test_BuilderInvalidOptionName2(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder0().option("invalid@")
    
    
    def test_BuilderInvalidOptionName3(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder1("invalid?")
    
    
    def test_BuilderInvalidOptionName4(self) -> None:
        with self.assertRaises(ValueError):
            Option.builder1("invalid@")
    
    
    def test_BuilderMethods(self) -> None:
        defaultSeparator = '\x00'

        self.__checkOption(
                Option.builder1("a").desc("desc").build(),\
                "a",\
                "desc",\
                None,\
                Option.UNINITIALIZED,\
                None,\
                False,\
                False,\
                defaultSeparator,\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").build(),\
                "a",\
                "desc",\
                None,\
                Option.UNINITIALIZED,\
                None,\
                False,\
                False,\
                defaultSeparator,\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").longOpt("aaa").build(),\
                "a",\
                "desc",\
                "aaa",\
                Option.UNINITIALIZED,\
                None,\
                False,\
                False,\
                defaultSeparator,\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").hasArg1(True).build(),\
                "a",\
                "desc",\
                None,\
                1,\
                None,\
                False,\
                False,\
                defaultSeparator,\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").hasArg1(False).build(),\
                "a",\
                "desc",\
                None,\
                Option.UNINITIALIZED,\
                None,\
                False,\
                False,\
                defaultSeparator,\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").hasArg1(True).build(),\
                "a",\
                "desc",\
                None,\
                1,\
                None,\
                False,\
                False,\
                defaultSeparator,\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").numberOfArgs(3).build(),\
                "a",\
                "desc",\
                None,\
                3,\
                None,\
                False,\
                False,\
                defaultSeparator,\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").required1(True).build(),\
                "a",\
                "desc",\
                None,\
                Option.UNINITIALIZED,\
                None,\
                True,\
                False,\
                defaultSeparator,\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").required1(False).build(),\
                "a",\
                "desc",\
                None,\
                Option.UNINITIALIZED,\
                None,\
                False,\
                False,\
                defaultSeparator,\
                str)

        self.__checkOption(
                Option.builder1("a").desc("desc").argName("arg1").build(),\
                "a",\
                "desc",\
                None,\
                Option.UNINITIALIZED,\
                "arg1",\
                False,\
                False,\
                defaultSeparator,\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").optionalArg(False).build(),\
                "a",\
                "desc",\
                None,\
                Option.UNINITIALIZED,\
                None,\
                False,\
                False,\
                defaultSeparator,\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").optionalArg(True).build(),\
                "a",\
                "desc",\
                None,\
                Option.UNINITIALIZED,\
                None,\
                False,\
                True,\
                defaultSeparator,\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").valueSeparator1(':').build(),\
                "a",\
                "desc",\
                None,\
                Option.UNINITIALIZED,\
                None,\
                False,\
                False,\
                ':',\
                str)
        self.__checkOption(
                Option.builder1("a").desc("desc").type(int).build(),\
                "a",\
                "desc",\
                None,\
                Option.UNINITIALIZED,\
                None,\
                False,\
                False,\
                defaultSeparator,\
                int)
        self.__checkOption(
                Option.builder0().option("a").desc("desc").type(int).build(),\
                "a",\
                "desc",\
                None,\
                Option.UNINITIALIZED,\
                None,\
                False,\
                False,\
                defaultSeparator,
                int)
    
    
    def test_Clear(self) -> None:
        option = OptionTest.TestOption("x", True, "")
        self.assertEqual(0, len(option.getValuesList()))
        option.addValue("a")
        self.assertEqual(1, len(option.getValuesList()))
        option.clearValues()
        self.assertEqual(0, len(option.getValuesList()))

    
    def test_Clone(self) -> None:
        a = OptionTest.TestOption("a", True, "")
        b = a.clone()
        self.assertEqual(a, b)
        self.assertIsNot(a, b)
        a.setDescription("a")
        self.assertEqual("", b.getDescription())
        b.setArgs(2)
        b.addValue("b1")
        b.addValue("b2")
        self.assertEqual(1, a.getArgs())
        self.assertEqual(0, len(a.getValuesList()))
        self.assertEqual(2, len(b.getValues()))

    
    def test_GetValue(self) -> None:
        option = Option.Option1("f", None)
        option.setArgs(Option.UNLIMITED_VALUES)

        self.assertEqual("default", option.getValue2("default"))
        self.assertIsNone(option.getValue1(0))

        option.addValueForProcessing("foo")

        self.assertEqual("foo", option.getValue0())
        self.assertEqual("foo", option.getValue1(0))
        self.assertEqual("foo", option.getValue2("default"))

    
    def test_HasArgName(self) -> None:
        option = Option.Option1("f", None)

        option.setArgName(None)
        self.assertFalse(option.hasArgName())

        option.setArgName("")
        self.assertFalse(option.hasArgName())

        option.setArgName("file")
        self.assertTrue(option.hasArgName())


    def test_HasArgs(self) -> None:
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
    
    
    def test_HashCode(self) -> None:
        self.assertNotEqual(
                Option.builder1("test").build().hashCode(),\
                Option.builder1("test2").build().hashCode())
        self.assertNotEqual(
                Option.builder1("test").build().hashCode(),\
                Option.builder0().longOpt("test").build().hashCode())
        self.assertNotEqual(
                Option.builder1("test").build().hashCode(),\
                Option.builder1("test").longOpt("long test").build().hashCode())
    
    
    def test_Subclass(self) -> None:
        option = OptionTest.DefaultOption("f", "file", "myfile.txt")
        clone = option.clone()
        self.assertEqual("myfile.txt", clone.getValue0())
        self.assertEqual(OptionTest.DefaultOption, type(clone))
    
    # Class Methods End

