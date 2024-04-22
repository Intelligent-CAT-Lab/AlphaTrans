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

    # Class Methods Begin
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__options = None
        self.__parser = PosixParser()


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

    
    def test_GetNames(self) -> None:
        group = OptionGroup()
        group.addOption(OptionBuilder.create1('a'))
        group.addOption(OptionBuilder.create1('b'))

        self.assertIsNotNone(group.getNames(), "null names")
        self.assertEqual(2, len(group.getNames()))
        self.assertTrue("a" in group.getNames())
        self.assertTrue("b" in group.getNames())


    def test_NoOptionsExtraArgs(self) -> None:
        try:
            args = ["arg1", "arg2"]

            cl = self.__parser.parse0(self.__options, args)

            self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
            self.assertFalse(cl.hasOption2("f"), "Confirm -f is NOT set")
            self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
            self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
            self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
            self.assertEqual(2, len(cl.getArgList()), "Confirm TWO extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    
    def test_SingleLongOption(self) -> None:
        try:
            args = ["--file"]

            cl = self.__parser.parse0(self.__options, args)

            self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
            self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
            self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
            self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
            self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
            self.assertEqual(len(cl.getArgList()), 0, "Confirm no extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def test_SingleOption(self) -> None:
        try:
            args = ["-r"]

            cl = self.__parser.parse0(self.__options, args)

            self.assertTrue(cl.hasOption2("r"), "Confirm -r is set")
            self.assertFalse(cl.hasOption2("f"), "Confirm -f is NOT set")
            self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
            self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
            self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
            self.assertEqual(len(cl.getArgList()), 0, "Confirm no extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def test_SingleOptionFromGroup(self) -> None:
        try:
            args = ["-f"]

            cl = self.__parser.parse0(self.__options, args)

            self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
            self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
            self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
            self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
            self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
            self.assertEqual(len(cl.getArgList()), 0, "Confirm no extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def test_ToString(self) -> None:
        group1 = OptionGroup()
        group1.addOption(Option(0, None, "foo", "Foo", False, None))
        group1.addOption(Option(0, None, "bar", "Bar", False, None))

        if "[--bar Bar, --foo Foo]" != (group1.toString()):
            self.assertEqual("[--foo Foo, --bar Bar]", group1.toString())

        group2 = OptionGroup()
        group2.addOption(Option(0, "f", "foo", "Foo", False, None))
        group2.addOption(Option(0, "b", "bar", "Bar", False, None))

        if "[-b Bar, -f Foo]" != (group2.toString()):
            self.assertEqual("[-f Foo, -b Bar]", group2.toString())
    
    
    def test_TwoLongOptionsFromGroup(self) -> None:
        try:
            args = ["--file", "--directory"]
            try:
                self.__parser.parse0(self.__options, args)
                self.fail("two arguments from group not allowed")
            except AlreadySelectedException as e:
                self.assertIsNotNone(e.getOptionGroup(), "null option group")
                self.assertEqual("f", e.getOptionGroup().getSelected(), "selected option")
                self.assertEqual("d", e.getOption().getOpt(), "option")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def test_TwoOptionsFromDifferentGroup(self) -> None:
        try:
            args = ["-f", "-s"]

            cl = self.__parser.parse0(self.__options, args)
            self.assertFalse(cl.hasOption2("r"), "Confirm -r is NOT set")
            self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
            self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
            self.assertTrue(cl.hasOption2("s"), "Confirm -s is set")
            self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
            self.assertEqual(len(cl.getArgList()), 0, "Confirm NO extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def test_TwoOptionsFromGroup(self) -> None:
        try:
            args = ["-f", "-d"]
            try:
                self.__parser.parse0(self.__options, args)
                self.fail("two arguments from group not allowed")
            except AlreadySelectedException as e:
                self.assertIsNotNone(e.getOptionGroup(), "null option group")
                self.assertEqual(e.getOptionGroup().getSelected(), "f", "selected option")
                self.assertEqual(e.getOption().getOpt(), "d", "option")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def test_TwoOptionsFromGroupWithProperties(self) -> None:
        try:
            args = ["-f"]

            properties = {"d": "true"}
            cl = self.__parser.parse2(self.__options, args, properties)

            self.assertTrue(cl.hasOption2("f"))
            self.assertFalse(cl.hasOption2("d"))
        except Exception as e:
            self.fail(f"An exception occurred: {e}")


    def test_TwoValidLongOptions(self) -> None:
        try:
            args = ["--revision", "--file"]

            cl = self.__parser.parse0(self.__options, args)

            self.assertTrue(cl.hasOption2("r"), "Confirm -r is set")
            self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
            self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
            self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
            self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
            self.assertEqual(len(cl.getArgList()), 0, "Confirm no extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def test_TwoValidOptions(self) -> None:
        try:
            args = ["-r", "-f"]

            cl = self.__parser.parse0(self.__options, args)

            self.assertTrue(cl.hasOption2("r"), "Confirm -r is set")
            self.assertTrue(cl.hasOption2("f"), "Confirm -f is set")
            self.assertFalse(cl.hasOption2("d"), "Confirm -d is NOT set")
            self.assertFalse(cl.hasOption2("s"), "Confirm -s is NOT set")
            self.assertFalse(cl.hasOption2("c"), "Confirm -c is NOT set")
            self.assertEqual(len(cl.getArgList()), 0, "Confirm no extra args")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    
    def test_ValidLongOnlyOptions(self) -> None:
        try:
            cl1 = self.__parser.parse0(self.__options, ["--export"])
            self.assertTrue(cl1.hasOption2("export"), "Confirm --export is set")

            cl2 = self.__parser.parse0(self.__options, ["--import"])
            self.assertTrue(cl2.hasOption2("import"), "Confirm --import is set")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    # Class Methods End
