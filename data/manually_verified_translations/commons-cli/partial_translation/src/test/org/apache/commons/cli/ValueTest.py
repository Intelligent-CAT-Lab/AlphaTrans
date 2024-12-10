from __future__ import annotations
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionBuilder import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.PosixParser import *


class ValueTest(unittest.TestCase):

    __opts: Options = Options()
    __cl: CommandLine = None

    def testShortWithArgWithOption(self) -> None:

        assert self.__cl.hasOption1(self.__opts.getOption("b"))
        assert self.__cl.getOptionValue2(self.__opts.getOption("b")) is not None
        assert self.__cl.getOptionValue2(self.__opts.getOption("b")) == "foo"

    def testShortWithArg(self) -> None:

        self.assertTrue(self.__cl.hasOption2("b"))
        self.assertIsNotNone(self.__cl.getOptionValue4("b"))
        self.assertEqual(self.__cl.getOptionValue4("b"), "foo")

    def testShortOptionalNArgValuesWithOption(self) -> None:

        args = ["-i", "ink", "idea", "isotope", "ice"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)

        self.assertTrue(cmd.hasOption2("i"))
        self.assertEqual("ink", cmd.getOptionValue2(self.__opts.getOption("i")))
        self.assertEqual("ink", cmd.getOptionValues1(self.__opts.getOption("i"))[0])
        self.assertEqual("idea", cmd.getOptionValues1(self.__opts.getOption("i"))[1])
        self.assertEqual(len(cmd.getArgs()), 2)
        self.assertEqual("isotope", cmd.getArgs()[0])
        self.assertEqual("ice", cmd.getArgs()[1])

    def testShortOptionalNArgValues(self) -> None:

        args = ["-i", "ink", "idea", "isotope", "ice"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)

        self.assertTrue(cmd.hasOption2("i"))
        self.assertEqual("ink", cmd.getOptionValue4("i"))
        self.assertEqual("ink", cmd.getOptionValues2("i")[0])
        self.assertEqual("idea", cmd.getOptionValues2("i")[1])
        self.assertEqual(len(cmd.getArgs()), 2)
        self.assertEqual("isotope", cmd.getArgs()[0])
        self.assertEqual("ice", cmd.getArgs()[1])

    def testShortOptionalArgValueWithOption(self) -> None:

        args = ["-e", "everything"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption1(self.__opts.getOption("e")))
        self.assertEqual("everything", cmd.getOptionValue2(self.__opts.getOption("e")))

    def testShortOptionalArgValuesWithOption(self) -> None:

        args = ["-j", "ink", "idea"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)

        assert cmd.hasOption1(self.__opts.getOption("j"))
        assert cmd.getOptionValue2(self.__opts.getOption("j")) == "ink"
        assert cmd.getOptionValues1(self.__opts.getOption("j"))[0] == "ink"
        assert cmd.getOptionValues1(self.__opts.getOption("j"))[1] == "idea"
        assert len(cmd.getArgs()) == 0

    def testShortOptionalArgValues(self) -> None:

        args = ["-j", "ink", "idea"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)

        self.assertTrue(cmd.hasOption2("j"))
        self.assertEqual("ink", cmd.getOptionValue4("j"))
        self.assertEqual("ink", cmd.getOptionValues2("j")[0])
        self.assertEqual("idea", cmd.getOptionValues2("j")[1])
        self.assertEqual(len(cmd.getArgs()), 0)

    def testShortOptionalArgValue(self) -> None:

        args = ["-e", "everything"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption2("e"))
        self.assertEqual("everything", cmd.getOptionValue4("e"))

    def testShortOptionalArgNoValueWithOption(self) -> None:

        args = ["-e"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption1(self.__opts.getOption("e")))
        self.assertIsNone(cmd.getOptionValue2(self.__opts.getOption("e")))

    def testShortOptionalArgNoValue(self) -> None:

        args = ["-e"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption2("e"))
        self.assertIsNone(cmd.getOptionValue4("e"))

    def testShortNoArgWithOption(self) -> None:

        assert self.__cl.hasOption1(self.__opts.getOption("a"))
        assert self.__cl.getOptionValue2(self.__opts.getOption("a")) is None

    def testShortNoArg(self) -> None:

        self.assertTrue(self.__cl.hasOption2("a"))
        self.assertIsNone(self.__cl.getOptionValue4("a"))

    def testLongWithArgWithOption(self) -> None:

        assert self.__cl.hasOption1(self.__opts.getOption("d"))
        assert self.__cl.getOptionValue2(self.__opts.getOption("d")) is not None
        assert self.__cl.getOptionValue2(self.__opts.getOption("d")) == "bar"

    def testLongWithArg(self) -> None:

        assert self.__cl.hasOption2("d")
        assert self.__cl.getOptionValue4("d") is not None
        assert self.__cl.getOptionValue4("d") == "bar"

    def testLongOptionalNoValueWithOption(self) -> None:

        args = ["--fish"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption1(self.__opts.getOption("fish")))
        self.assertIsNone(cmd.getOptionValue2(self.__opts.getOption("fish")))

    def testLongOptionalNoValue(self) -> None:

        args = ["--fish"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption2("fish"))
        self.assertIsNone(cmd.getOptionValue4("fish"))

    def testLongOptionalNArgValuesWithOption(self) -> None:

        args = ["--hide", "house", "hair", "head"]

        parser = Parser()

        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption1(self.__opts.getOption("hide")))
        self.assertEqual("house", cmd.getOptionValue2(self.__opts.getOption("hide")))
        self.assertEqual(
            "house", cmd.getOptionValues1(self.__opts.getOption("hide"))[0]
        )
        self.assertEqual("hair", cmd.getOptionValues1(self.__opts.getOption("hide"))[1])
        self.assertEqual(len(cmd.getArgs()), 1)
        self.assertEqual("head", cmd.getArgs()[0])

    def testLongOptionalNArgValues(self) -> None:

        args = ["--hide", "house", "hair", "head"]

        parser = PosixParser()

        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption2("hide"))
        self.assertEqual("house", cmd.getOptionValue4("hide"))
        self.assertEqual("house", cmd.getOptionValues2("hide")[0])
        self.assertEqual("hair", cmd.getOptionValues2("hide")[1])
        self.assertEqual(len(cmd.getArgs()), 1)
        self.assertEqual("head", cmd.getArgs()[0])

    def testLongOptionalArgValueWithOption(self) -> None:

        args = ["--fish", "face"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption1(self.__opts.getOption("fish")))
        self.assertEqual("face", cmd.getOptionValue2(self.__opts.getOption("fish")))

    def testLongOptionalArgValuesWithOption(self) -> None:

        args = ["--gravy", "gold", "garden"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)

        self.assertTrue(cmd.hasOption1(self.__opts.getOption("gravy")))
        self.assertEqual("gold", cmd.getOptionValue2(self.__opts.getOption("gravy")))
        self.assertEqual(
            "gold", cmd.getOptionValues1(self.__opts.getOption("gravy"))[0]
        )
        self.assertEqual(
            "garden", cmd.getOptionValues1(self.__opts.getOption("gravy"))[1]
        )
        self.assertEqual(len(cmd.getArgs()), 0)

    def testLongOptionalArgValues(self) -> None:

        args = ["--gravy", "gold", "garden"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)

        self.assertTrue(cmd.hasOption2("gravy"))
        self.assertEqual("gold", cmd.getOptionValue4("gravy"))
        self.assertEqual("gold", cmd.getOptionValues2("gravy")[0])
        self.assertEqual("garden", cmd.getOptionValues2("gravy")[1])
        self.assertEqual(len(cmd.getArgs()), 0)

    def testLongOptionalArgValue(self) -> None:

        args = ["--fish", "face"]

        parser = PosixParser()
        cmd = parser.parse0(self.__opts, args)
        self.assertTrue(cmd.hasOption2("fish"))
        self.assertEqual("face", cmd.getOptionValue4("fish"))

    def testLongNoArgWithOption(self) -> None:

        assert self.__cl.hasOption1(self.__opts.getOption("c"))
        assert self.__cl.getOptionValue2(self.__opts.getOption("c")) is None

    def testLongNoArg(self) -> None:

        self.assertTrue(self.__cl.hasOption2("c"))
        self.assertIsNone(self.__cl.getOptionValue4("c"))

    def setUp(self) -> None:

        self.__opts.addOption1("a", False, "toggle -a")
        self.__opts.addOption1("b", True, "set -b")
        self.__opts.addOption3("c", "c", False, "toggle -c")
        self.__opts.addOption3("d", "d", True, "set -d")

        self.__opts.addOption0(OptionBuilder.hasOptionalArg().create1("e"))
        self.__opts.addOption0(
            OptionBuilder.hasOptionalArg().withLongOpt("fish").create0()
        )
        self.__opts.addOption0(
            OptionBuilder.hasOptionalArgs0().withLongOpt("gravy").create0()
        )
        self.__opts.addOption0(
            OptionBuilder.hasOptionalArgs1(2).withLongOpt("hide").create0()
        )
        self.__opts.addOption0(OptionBuilder.hasOptionalArgs1(2).create1("i"))
        self.__opts.addOption0(OptionBuilder.hasOptionalArgs0().create1("j"))

        args = ["-a", "-b", "foo", "--c", "--d", "bar"]

        parser = PosixParser()
        self.__cl = parser.parse0(self.__opts, args)
