from __future__ import annotations
import unittest
import pytest
import io
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

        cl1 = self.__parser.parse0(self.__options, ["--export"])
        assert cl1.hasOption2("export"), "Confirm --export is set"

        cl2 = self.__parser.parse0(self.__options, ["--import"])
        assert cl2.hasOption2("import"), "Confirm --import is set"

    def testTwoValidOptions(self) -> None:

        args = ["-r", "-f"]

        cl = self.__parser.parse0(self.__options, args)

        assert cl.hasOption2("r"), "Confirm -r is set"
        assert cl.hasOption2("f"), "Confirm -f is set"
        assert not cl.hasOption2("d"), "Confirm -d is NOT set"
        assert not cl.hasOption2("s"), "Confirm -s is NOT set"
        assert not cl.hasOption2("c"), "Confirm -c is NOT set"
        assert not cl.getArgList(), "Confirm no extra args"

    def testTwoValidLongOptions(self) -> None:

        args = ["--revision", "--file"]

        cl = self.__parser.parse0(self.__options, args)

        assert cl.hasOption2("r"), "Confirm -r is set"
        assert cl.hasOption2("f"), "Confirm -f is set"
        assert not cl.hasOption2("d"), "Confirm -d is NOT set"
        assert not cl.hasOption2("s"), "Confirm -s is NOT set"
        assert not cl.hasOption2("c"), "Confirm -c is NOT set"
        assert not cl.getArgList(), "Confirm no extra args"

    def testTwoOptionsFromGroupWithProperties(self) -> None:

        args = ["-f"]

        properties = {"d": "true"}

        cl = self.__parser.parse2(self.__options, args, properties)
        assert cl.hasOption2("f")
        assert not cl.hasOption2("d")

    def testTwoOptionsFromGroup(self) -> None:

        args = ["-f", "-d"]

        try:
            self.__parser.parse0(self.__options, args)
            assert False, "two arguments from group not allowed"
        except AlreadySelectedException as e:
            assert e.getOptionGroup() is not None, "null option group"
            assert e.getOptionGroup().getSelected() == "f", "selected option"
            assert e.getOption().getOpt() == "d", "option"

    def testTwoOptionsFromDifferentGroup(self) -> None:

        args = ["-f", "-s"]

        cl = self.__parser.parse0(self.__options, args)
        assert not cl.hasOption2("r"), "Confirm -r is NOT set"
        assert cl.hasOption2("f"), "Confirm -f is set"
        assert not cl.hasOption2("d"), "Confirm -d is NOT set"
        assert cl.hasOption2("s"), "Confirm -s is set"
        assert not cl.hasOption2("c"), "Confirm -c is NOT set"
        assert not cl.getArgList(), "Confirm NO extra args"

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
            assert group1.toString() == "[--foo Foo, --bar Bar]"

        group2 = OptionGroup()
        group2.addOption(Option(0, "f", "foo", "Foo", False, None))
        group2.addOption(Option(0, "b", "bar", "Bar", False, None))

        if group2.toString() != "[-b Bar, -f Foo]":
            assert group2.toString() == "[-f Foo, -b Bar]"

    def testSingleOptionFromGroup(self) -> None:

        args = ["-f"]

        cl = self.__parser.parse0(self.__options, args)

        assert not cl.hasOption2("r"), "Confirm -r is NOT set"
        assert cl.hasOption2("f"), "Confirm -f is set"
        assert not cl.hasOption2("d"), "Confirm -d is NOT set"
        assert not cl.hasOption2("s"), "Confirm -s is NOT set"
        assert not cl.hasOption2("c"), "Confirm -c is NOT set"
        assert not cl.getArgList(), "Confirm no extra args"

    def testSingleOption(self) -> None:

        args = ["-r"]

        cl = self.__parser.parse0(self.__options, args)

        assert cl.hasOption2("r"), "Confirm -r is set"
        assert not cl.hasOption2("f"), "Confirm -f is NOT set"
        assert not cl.hasOption2("d"), "Confirm -d is NOT set"
        assert not cl.hasOption2("s"), "Confirm -s is NOT set"
        assert not cl.hasOption2("c"), "Confirm -c is NOT set"
        assert not cl.getArgList(), "Confirm no extra args"

    def testSingleLongOption(self) -> None:

        args = ["--file"]

        cl = self.__parser.parse0(self.__options, args)

        assert not cl.hasOption2("r"), "Confirm -r is NOT set"
        assert cl.hasOption2("f"), "Confirm -f is set"
        assert not cl.hasOption2("d"), "Confirm -d is NOT set"
        assert not cl.hasOption2("s"), "Confirm -s is NOT set"
        assert not cl.hasOption2("c"), "Confirm -c is NOT set"
        assert not cl.getArgList(), "Confirm no extra args"

    def testNoOptionsExtraArgs(self) -> None:

        args = ["arg1", "arg2"]

        cl = self.__parser.parse0(self.__options, args)

        assert not cl.hasOption2("r"), "Confirm -r is NOT set"
        assert not cl.hasOption2("f"), "Confirm -f is NOT set"
        assert not cl.hasOption2("d"), "Confirm -d is NOT set"
        assert not cl.hasOption2("s"), "Confirm -s is NOT set"
        assert not cl.hasOption2("c"), "Confirm -c is NOT set"
        assert len(cl.getArgList()) == 2, "Confirm TWO extra args"

    def testGetNames(self) -> None:

        group = OptionGroup()
        group.addOption(OptionBuilder.create1("a"))
        group.addOption(OptionBuilder.create1("b"))

        assert group.getNames() is not None, "null names"
        assert len(group.getNames()) == 2, "Names size is not 2"
        assert "a" in group.getNames(), "'a' not in names"
        assert "b" in group.getNames(), "'b' not in names"

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
