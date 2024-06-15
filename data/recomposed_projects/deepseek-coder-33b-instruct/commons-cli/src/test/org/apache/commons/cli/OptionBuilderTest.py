from __future__ import annotations
import unittest
import pytest
import io
import numbers
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *


class OptionBuilderTest(unittest.TestCase):

    def testTwoCompleteOptions(self) -> None:

        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )

        assert simple.getOpt() == "s"
        assert simple.getLongOpt() == "simple option"
        assert simple.getDescription() == "this is a simple option"
        assert simple.getType() == float
        assert simple.hasArg()
        assert simple.isRequired()
        assert simple.hasArgs()

        simple = (
            OptionBuilder.withLongOpt("dimple option")
            .hasArg0()
            .withDescription("this is a dimple option")
            .create1("d")
        )

        assert simple.getOpt() == "d"
        assert simple.getLongOpt() == "dimple option"
        assert simple.getDescription() == "this is a dimple option"
        assert simple.getType() == str
        assert simple.hasArg()
        assert not simple.isRequired()
        assert not simple.hasArgs()

    def testSpecialOptChars(self) -> None:

        opt1 = OptionBuilder.withDescription("help options").create1("?")
        assert opt1.getOpt() == "?"

        opt2 = OptionBuilder.withDescription("read from stdin").create1("@")
        assert opt2.getOpt() == "@"

        try:
            OptionBuilder.create1(" ")
            assert False, "ValueError not caught"
        except ValueError:
            pass

    def testOptionArgNumbers(self) -> None:

        opt = (
            OptionBuilder.withDescription("option description").hasArgs1(2).create1("o")
        )
        assert opt.getArgs() == 2

    def testIllegalOptions(self) -> None:

        pass  # LLM could not translate this method

    def testCreateIncompleteOption(self) -> None:

        try:
            OptionBuilder.hasArg0().create0()
            self.fail("Incomplete option should be rejected")
        except ValueError as e:
            OptionBuilder.create2("opt")

    def testCompleteOption(self) -> None:

        simple = (
            OptionBuilder.withLongOpt("simple option")
            .hasArg0()
            .isRequired0()
            .hasArgs0()
            .withType0(float)
            .withDescription("this is a simple option")
            .create1("s")
        )

        assert simple.getOpt() == "s"
        assert simple.getLongOpt() == "simple option"
        assert simple.getDescription() == "this is a simple option"
        assert simple.getType() == float
        assert simple.hasArg()
        assert simple.isRequired()
        assert simple.hasArgs()

    def testBuilderIsResettedAlways(self) -> None:

        try:
            OptionBuilder.withDescription("JUnit").create1('"')
            self.fail("ValueError expected")
        except ValueError:
            pass
        self.assertIsNone(
            OptionBuilder.create1("x").getDescription(), "we inherited a description"
        )

        try:
            OptionBuilder.withDescription("JUnit").create0()
            self.fail("ValueError expected")
        except ValueError:
            pass
        self.assertIsNone(
            OptionBuilder.create1("x").getDescription(), "we inherited a description"
        )

    def testBaseOptionStringOpt(self) -> None:

        base = OptionBuilder.withDescription("option description").create2("o")

        self.assertEqual("o", base.getOpt())
        self.assertEqual("option description", base.getDescription())
        self.assertFalse(base.hasArg())

    def testBaseOptionCharOpt(self) -> None:

        base = OptionBuilder.withDescription("option description").create1("o")

        self.assertEqual("o", base.getOpt())
        self.assertEqual("option description", base.getDescription())
        self.assertFalse(base.hasArg())
