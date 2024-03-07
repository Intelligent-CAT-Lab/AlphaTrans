# Imports Begin
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
import unittest
import typing
from typing import *
import numbers

# Imports End


class OptionBuilderTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testTwoCompleteOptions(self) -> None:

        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(Float)
            .withDescription("this is a simple option")
            .create1("s")
        )
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), Float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())
        simple = (
            OptionBuilder.withLongOpt("dimple option")
            .hasArg0()
            .withDescription("this is a dimple option")
            .create1("d")
        )
        self.assertEqual("d", simple.getOpt())
        self.assertEqual("dimple option", simple.getLongOpt())
        self.assertEqual("this is a dimple option", simple.getDescription())
        self.assertEqual(String, simple.getType())
        self.assertTrue(simple.hasArg())
        self.assertFalse(simple.isRequired())
        self.assertFalse(simple.hasArgs())

    def testSpecialOptChars(self) -> None:

        opt1 = OptionBuilder.withDescription("help options").create1("?")
        self.assertEqual("?", opt1.getOpt())
        opt2 = OptionBuilder.withDescription("read from stdin").create1("@")
        self.assertEqual("@", opt2.getOpt())
        try:
            OptionBuilder.create1(" ")
            fail("IllegalArgumentException not caught")
        except IllegalArgumentException:
            pass

    def testOptionArgNumbers(self) -> None:

        pass  # LLM could not translate method body

    def testIllegalOptions(self) -> None:

        try:
            OptionBuilder.withDescription("option description").create1('"')
            self.fail("IllegalArgumentException not caught")
        except IllegalArgumentException:
            pass
        try:
            OptionBuilder.create2("opt`")
            self.fail("IllegalArgumentException not caught")
        except IllegalArgumentException:
            pass
        try:
            OptionBuilder.create2("opt")
        except IllegalArgumentException:
            self.fail("IllegalArgumentException caught")

    def testCreateIncompleteOption(self) -> None:

        with self.assertRaises(IllegalArgumentException):
            OptionBuilder.hasArg0().create0()
        OptionBuilder.create2("opt")

    def testCompleteOption(self) -> None:

        pass  # LLM could not translate method body

    def testBuilderIsResettedAlways(self) -> None:

        try:
            OptionBuilder.withDescription("JUnit").create1('"')
            self.fail("IllegalArgumentException expected")
        except IllegalArgumentException:
            pass
        assertNull(
            "we inherited a description", OptionBuilder.create1("x").getDescription()
        )
        try:
            OptionBuilder.withDescription("JUnit").create0()
            self.fail("IllegalArgumentException expected")
        except IllegalArgumentException:
            pass
        assertNull(
            "we inherited a description", OptionBuilder.create1("x").getDescription()
        )

    def testBaseOptionStringOpt(self) -> None:

        pass  # LLM could not translate method body

    def testBaseOptionCharOpt(self) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
