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
        cl1: CommandLine = self.__parser.parse0(self.__options, ["--export"])
        self.assertTrue("Confirm --export is set", cl1.hasOption2("export"))

        cl2: CommandLine = self.__parser.parse0(self.__options, ["--import"])
        self.assertTrue("Confirm --import is set", cl2.hasOption2("import"))

    def testTwoValidOptions(self) -> None:
        args = ["-r", "-f"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertTrue("Confirm -r is set", cl.hasOption2("r"))
        self.assertTrue("Confirm -f is set", cl.hasOption2("f"))
        self.assertFalse("Confirm -d is NOT set", cl.hasOption2("d"))
        self.assertFalse("Confirm -s is NOT set", cl.hasOption2("s"))
        self.assertFalse("Confirm -c is NOT set", cl.hasOption2("c"))
        self.assertTrue("Confirm no extra args", cl.getArgList().isEmpty())

    def testTwoValidLongOptions(self) -> None:
        args = ["--revision", "--file"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertTrue("Confirm -r is set", cl.hasOption2("r"))
        self.assertTrue("Confirm -f is set", cl.hasOption2("f"))
        self.assertFalse("Confirm -d is NOT set", cl.hasOption2("d"))
        self.assertFalse("Confirm -s is NOT set", cl.hasOption2("s"))
        self.assertFalse("Confirm -c is NOT set", cl.hasOption2("c"))
        self.assertTrue("Confirm no extra args", cl.getArgList().isEmpty())

    def testTwoOptionsFromGroupWithProperties(self) -> None:
        args = ["-f"]

        properties = {}
        properties["d"] = "true"

        cl = self.__parser.parse2(self.__options, args, properties)
        self.assertTrue(cl.hasOption2("f"))
        self.assertFalse(cl.hasOption2("d"))

    def testTwoOptionsFromGroup(self) -> None:
        args = ["-f", "-d"]
        try:
            self.__parser.parse0(self.__options, args)
            self.fail("two arguments from group not allowed")
        except AlreadySelectedException as e:
            self.assertIsNotNone("null option group", e.getOptionGroup())
            self.assertEqual("selected option", "f", e.getOptionGroup().getSelected())
            self.assertEqual("option", "d", e.getOption().getOpt())

    def testTwoOptionsFromDifferentGroup(self) -> None:
        args = ["-f", "-s"]

        cl = self.__parser.parse0(self.__options, args)
        self.assertFalse("Confirm -r is NOT set", cl.hasOption2("r"))
        self.assertTrue("Confirm -f is set", cl.hasOption2("f"))
        self.assertFalse("Confirm -d is NOT set", cl.hasOption2("d"))
        self.assertTrue("Confirm -s is set", cl.hasOption2("s"))
        self.assertFalse("Confirm -c is NOT set", cl.hasOption2("c"))
        self.assertTrue("Confirm NO extra args", cl.getArgList().isEmpty())

    def testTwoLongOptionsFromGroup(self) -> None:
        args = ["--file", "--directory"]
        try:
            self.__parser.parse0(self.__options, args)
            self.fail("two arguments from group not allowed")
        except AlreadySelectedException as e:
            self.assertIsNotNone("null option group", e.getOptionGroup())
            self.assertEqual("selected option", "f", e.getOptionGroup().getSelected())
            self.assertEqual("option", "d", e.getOption().getOpt())

    def testToString(self) -> None:
        group1 = OptionGroup()
        group1.addOption(Option(0, None, "foo", "Foo", False, None))
        group1.addOption(Option(0, None, "bar", "Bar", False, None))

        if "[--bar Bar, --foo Foo]" != group1.toString():
            self.assertEqual("[--foo Foo, --bar Bar]", group1.toString())

        group2 = OptionGroup()
        group2.addOption(Option(0, "f", "foo", "Foo", False, None))
        group2.addOption(Option(0, "b", "bar", "Bar", False, None))

        if "-b Bar, -f Foo" != group2.toString():
            self.assertEqual("[-f Foo, -b Bar]", group2.toString())

    def testSingleOptionFromGroup(self) -> None:
        args = ["-f"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertFalse("Confirm -r is NOT set", cl.hasOption2("r"))
        self.assertTrue("Confirm -f is set", cl.hasOption2("f"))
        self.assertFalse("Confirm -d is NOT set", cl.hasOption2("d"))
        self.assertFalse("Confirm -s is NOT set", cl.hasOption2("s"))
        self.assertFalse("Confirm -c is NOT set", cl.hasOption2("c"))
        self.assertTrue("Confirm no extra args", cl.getArgList().isEmpty())

    def testSingleOption(self) -> None:
        args = ["-r"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertTrue("Confirm -r is set", cl.hasOption2("r"))
        self.assertFalse("Confirm -f is NOT set", cl.hasOption2("f"))
        self.assertFalse("Confirm -d is NOT set", cl.hasOption2("d"))
        self.assertFalse("Confirm -s is NOT set", cl.hasOption2("s"))
        self.assertFalse("Confirm -c is NOT set", cl.hasOption2("c"))
        self.assertTrue("Confirm no extra args", cl.getArgList().isEmpty())

    def testSingleLongOption(self) -> None:
        args = ["--file"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertFalse("Confirm -r is NOT set", cl.hasOption2("r"))
        self.assertTrue("Confirm -f is set", cl.hasOption2("f"))
        self.assertFalse("Confirm -d is NOT set", cl.hasOption2("d"))
        self.assertFalse("Confirm -s is NOT set", cl.hasOption2("s"))
        self.assertFalse("Confirm -c is NOT set", cl.hasOption2("c"))
        self.assertTrue("Confirm no extra args", cl.getArgList().isEmpty())

    def testNoOptionsExtraArgs(self) -> None:
        args = ["arg1", "arg2"]

        cl = self.__parser.parse0(self.__options, args)

        self.assertFalse("Confirm -r is NOT set", cl.hasOption2("r"))
        self.assertFalse("Confirm -f is NOT set", cl.hasOption2("f"))
        self.assertFalse("Confirm -d is NOT set", cl.hasOption2("d"))
        self.assertFalse("Confirm -s is NOT set", cl.hasOption2("s"))
        self.assertFalse("Confirm -c is NOT set", cl.hasOption2("c"))
        self.assertEqual("Confirm TWO extra args", 2, cl.getArgList().size())

    def testGetNames(self) -> None:
        group: OptionGroup = OptionGroup()
        group.addOption(OptionBuilder.create1("a"))
        group.addOption(OptionBuilder.create1("b"))

        assert group.getNames() is not None, "null names"
        assert len(group.getNames()) == 2, "incorrect number of names"
        assert "a" in group.getNames(), "missing name 'a'"
        assert "b" in group.getNames(), "missing name 'b'"

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
