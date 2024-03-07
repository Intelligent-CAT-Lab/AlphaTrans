# Imports Begin
from src.main.org.apache.commons.cli.PosixParser import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.AlreadySelectedException import *
import unittest
import os
import typing
from typing import *

# Imports End


class OptionGroupTest(unittest.TestCase):

    # Class Fields Begin
    __options: Options = None
    __parser: Parser = PosixParser()
    # Class Fields End

    # Class Methods Begin
    def testValidLongOnlyOptions(self) -> None:

        cl1 = self.__parser.parse0(self.__options, ["--export"])
        assert cl1.hasOption2("export")
        cl2 = self.__parser.parse0(self.__options, ["--import"])
        assert cl2.hasOption2("import")

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
        assert cl.hasOption2("r")
        assert cl.hasOption2("f")
        assert not cl.hasOption2("d")
        assert not cl.hasOption2("s")
        assert not cl.hasOption2("c")
        assert cl.getArgList().isEmpty()

    def testTwoOptionsFromGroupWithProperties(self) -> None:

        args = ["-f"]
        properties = {"d": "true"}
        cl = self.parser.parse2(self.options, args, properties)
        assert cl.hasOption2("f")
        assert not cl.hasOption2("d")

    def testTwoOptionsFromGroup(self) -> None:

        args = ["-f", "-d"]
        try:
            self.__parser.parse0(self.__options, args)
            self.fail("two arguments from group not allowed")
        except AlreadySelectedException as e:
            self.assertIsNotNone(e.getOptionGroup())
            self.assertEqual(e.getOptionGroup().getSelected(), "f")
            self.assertEqual(e.getOption().getOpt(), "d")

    def testTwoOptionsFromDifferentGroup(self) -> None:

        args = ["-f", "-s"]
        cl = self.__parser.parse0(self.__options, args)
        assert not cl.hasOption2("r")
        assert cl.hasOption2("f")
        assert not cl.hasOption2("d")
        assert cl.hasOption2("s")
        assert not cl.hasOption2("c")
        assert cl.getArgList().isEmpty()

    def testTwoLongOptionsFromGroup(self) -> None:

        args = ["--file", "--directory"]
        try:
            self.parser.parse0(self.options, args)
            self.fail("two arguments from group not allowed")
        except AlreadySelectedException as e:
            assertNotNull("null option group", e.getOptionGroup())
            self.assertEqual("selected option", "f", e.getOptionGroup().getSelected())
            self.assertEqual("option", "d", e.getOption().getOpt())

    def testToString(self) -> None:

        pass  # LLM could not translate method body

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
        assert cl.hasOption2("r")
        assert not cl.hasOption2("f")
        assert not cl.hasOption2("d")
        assert not cl.hasOption2("s")
        assert not cl.hasOption2("c")
        assert cl.getArgList().isEmpty()

    def testSingleLongOption(self) -> None:

        args = ["--file"]
        cl = self.__parser.parse0(self.__options, args)
        assert not cl.hasOption2("r")
        assert cl.hasOption2("f")
        assert not cl.hasOption2("d")
        assert not cl.hasOption2("s")
        assert not cl.hasOption2("c")
        assert cl.getArgList().isEmpty()

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

        pass  # LLM could not translate method body

    def setUp(self) -> None:

        file_option = Option(0, "f", "file", "file to process", False, None)
        dir_option = Option(0, "d", "directory", "directory to process", False, None)
        group = OptionGroup()
        group.addOption(file_option)
        group.addOption(dir_option)
        self.__options = Options().addOptionGroup(group)
        section_option = Option(0, "s", "section", "section to process", False, None)
        chapter_option = Option(0, "c", "chapter", "chapter to process", False, None)
        group2 = OptionGroup()
        group2.addOption(section_option)
        group2.addOption(chapter_option)
        self.__options.addOptionGroup(group2)
        import_option = Option(0, None, "import", "section to process", False, None)
        export_option = Option(0, None, "export", "chapter to process", False, None)
        group3 = OptionGroup()
        group3.addOption(import_option)
        group3.addOption(export_option)
        self.__options.addOptionGroup(group3)
        self.__options.addOption3("r", "revision", False, "revision number")

    # Class Methods End
