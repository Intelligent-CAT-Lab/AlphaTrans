from __future__ import annotations
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.AlreadySelectedException import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.PosixParser import *


class OptionGroupTest(unittest.TestCase):

    __parser: Parser = PosixParser()
    __options: Options = None

    def testValidLongOnlyOptions(self) -> None:

        # Create an instance of the Parser class
        parser = Parser()

        # Create an instance of the Options class
        options = Options()

        # Add options to the Options instance
        options.addOption("export", False, "Export option")
        options.addOption("import", False, "Import option")

        # Parse the command line arguments
        cl1 = parser.parse0(options, ["--export"])

        # Check if the "export" option is set
        self.assertTrue(cl1.hasOption2("export"))

        # Parse the command line arguments
        cl2 = parser.parse0(options, ["--import"])

        # Check if the "import" option is set
        self.assertTrue(cl2.hasOption2("import"))

    def testTwoValidOptions(self) -> None:

        args = ["-r", "-f"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertTrue("Confirm -r is set", cl.hasOption2("r"))
        self.assertTrue("Confirm -f is set", cl.hasOption2("f"))
        self.assertFalse("Confirm -d is NOT set", cl.hasOption2("d"))
        self.assertFalse("Confirm -s is NOT set", cl.hasOption2("s"))
        self.assertFalse("Confirm -c is NOT set", cl.hasOption2("c"))
        self.assertTrue("Confirm no extra args", not cl.getArgList())

    def testTwoValidLongOptions(self) -> None:

        args = ["--revision", "--file"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertTrue("Confirm -r is set", cl.hasOption2("r"))
        self.assertTrue("Confirm -f is set", cl.hasOption2("f"))
        self.assertFalse("Confirm -d is NOT set", cl.hasOption2("d"))
        self.assertFalse("Confirm -s is NOT set", cl.hasOption2("s"))
        self.assertFalse("Confirm -c is NOT set", cl.hasOption2("c"))
        self.assertTrue("Confirm no extra args", not cl.getArgList())

    def testTwoOptionsFromGroupWithProperties(self) -> None:

        # Define the arguments
        args = ["-f"]

        # Create a properties object and add a property
        properties = {}
        properties["d"] = "true"

        # Parse the arguments and properties
        cl = self.__parser.parse2(self.__options, args, properties)

        # Assert that the option "f" is present
        assert cl.hasOption2("f")

        # Assert that the option "d" is not present
        assert not cl.hasOption2("d")

    def testTwoOptionsFromGroup(self) -> None:

        args = ["-f", "-d"]

        try:
            self.__parser.parse0(self.__options, args)
            self.fail("two arguments from group not allowed")
        except AlreadySelectedException as e:
            self.assertIsNotNone(e.getOptionGroup(), "null option group")
            self.assertEqual(e.getOptionGroup().getSelected(), "f", "selected option")
            self.assertEqual(e.getOption().getOpt(), "d", "option")

    def testTwoOptionsFromDifferentGroup(self) -> None:

        args = ["-f", "-s"]

        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertTrue(cl.hasOption2("s"), "Confirm -s is set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
        self.assertTrue(not cl.getArgList(), "Confirm NO extra args")

    def testTwoLongOptionsFromGroup(self) -> None:

        args = ["--file", "--directory"]

        try:
            self.__parser.parse0(self.__options, args)
            self.fail("two arguments from group not allowed")
        except AlreadySelectedException as e:
            self.assertIsNotNone(e.getOptionGroup(), "null option group")
            self.assertEqual(e.getOptionGroup().getSelected(), "f", "selected option")
            self.assertEqual(e.getOption().getOpt(), "d", "option")

    def testToString(self) -> None:

        group1 = OptionGroup()
        group1.addOption(Option(0, None, "foo", "Foo", False, None))
        group1.addOption(Option(0, None, "bar", "Bar", False, None))

        if group1.toString() != "[--bar Bar, --foo Foo]":
            self.assertEqual("[--foo Foo, --bar Bar]", group1.toString())

        group2 = OptionGroup()
        group2.addOption(Option(0, "f", "foo", "Foo", False, None))
        group2.addOption(Option(0, "b", "bar", "Bar", False, None))

        if group2.toString() != "[-b Bar, -f Foo]":
            self.assertEqual("[-f Foo, -b Bar]", group2.toString())

    def testSingleOptionFromGroup(self) -> None:

        args = ["-f"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
        self.assertTrue(len(cl.getArgList()) == 0, "Confirm no extra args")

    def testSingleOption(self) -> None:

        args = ["-r"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertTrue(cl.hasOption2("r"))
        self.assertFalse(cl.hasOption2("f"))
        self.assertFalse(cl.hasOption2("d"))
        self.assertFalse(cl.hasOption2("s"))
        self.assertFalse(cl.hasOption2("c"))
        self.assertTrue(len(cl.getArgList()) == 0)

    def testSingleLongOption(self) -> None:

        args = ["--file"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
        self.assertTrue(len(cl.getArgList()) == 0, "Confirm no extra args")

    def testNoOptionsExtraArgs(self) -> None:

        args = ["arg1", "arg2"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
        self.assertFalse(cl.hasOption2("f"), "Confirm -f is NOT set")
        self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
        self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
        self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
        self.assertEqual(len(cl.getArgList()), 2, "Confirm TWO extra args")

    def testGetNames(self) -> None:

        group = OptionGroup()
        group.addOption(OptionBuilder.create1("a"))
        group.addOption(OptionBuilder.create1("b"))

        self.assertIsNotNone(group.getNames(), "null names")
        self.assertEqual(2, len(group.getNames()))
        self.assertIn("a", group.getNames())
        self.assertIn("b", group.getNames())

    def setUp(self) -> None:

        file = Option(0, "f", "file", "file to process", False, None)
        dir = Option(0, "d", "directory", "directory to process", False, None)
        group = OptionGroup()
        group.addOption(file)
        group.addOption(dir)
        self.__options = Options().addOptionGroup(group)

        section = Option(0, "s", "section", "section to process", False, None)
        chapter = Option(0, "c", "chapter", "chapter to process", False, None)
        group2 = OptionGroup()
        group2.addOption(section)
        group2.addOption(chapter)

        self.__options.addOptionGroup(group2)

        importOpt = Option(0, None, "import", "section to process", False, None)
        exportOpt = Option(0, None, "export", "chapter to process", False, None)
        group3 = OptionGroup()
        group3.addOption(importOpt)
        group3.addOption(exportOpt)
        self.__options.addOptionGroup(group3)

        self.__options.addOption3("r", "revision", False, "revision number")
