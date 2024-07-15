from __future__ import annotations
import re
import typing
from typing import *
import unittest
import pytest
import io
import numbers
import unittest
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
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
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
        self.assertEqual(str, simple.getType())
        self.assertTrue(simple.hasArg())
        self.assertFalse(simple.isRequired())
        self.assertFalse(simple.hasArgs())

    def testSpecialOptChars(self) -> None:
        opt1: Option = OptionBuilder.withDescription("help options").create1("?")
        self.assertEqual("?", opt1.getOpt())

        opt2: Option = OptionBuilder.withDescription("read from stdin").create1("@")
        self.assertEqual("@", opt2.getOpt())

        with self.assertRaises(ValueError):
            OptionBuilder.create1(" ")

    def testOptionArgNumbers(self) -> None:
        opt = (
            OptionBuilder.withDescription("option description").hasArgs1(2).create1("o")
        )
        self.assertEqual(2, opt.getArgs())

    def testIllegalOptions(self) -> None:

        pass  # LLM could not translate this method

    def testCreateIncompleteOption(self) -> None:
        with self.assertRaises(ValueError):
            OptionBuilder.hasArg0().create0()
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
        self.assertEqual("s", simple.getOpt())
        self.assertEqual("simple option", simple.getLongOpt())
        self.assertEqual("this is a simple option", simple.getDescription())
        self.assertEqual(simple.getType(), float)
        self.assertTrue(simple.hasArg())
        self.assertTrue(simple.isRequired())
        self.assertTrue(simple.hasArgs())

    def testBuilderIsResettedAlways(self) -> None:

        pass  # LLM could not translate this method

    def testBaseOptionStringOpt(self) -> None:
        base: Option = OptionBuilder.withDescription("option description").create2("o")

        self.assertEqual("o", base.getOpt())
        self.assertEqual("option description", base.getDescription())
        self.assertFalse(base.hasArg())

    def testBaseOptionCharOpt(self) -> None:
        base: Option = OptionBuilder.withDescription("option description").create1("o")

        self.assertEqual("o", base.getOpt())
        self.assertEqual("option description", base.getDescription())
        self.assertFalse(base.hasArg())
