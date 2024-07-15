from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.CommandLine import *
from src.main.org.apache.commons.cli.DefaultParser import *

# from src.test.org.apache.commons.cli.DefaultParser_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DefaultParser_ESTest(unittest.TestCase):

    def test31(self) -> None:

        boolean0 = True
        defaultParser0 = DefaultParser(-2, False, boolean0)
        options0 = Options()
        options0.addRequiredOption("17Q", "a7", True, "17Q")
        properties0 = {}
        stringArray0 = ["--a7", "--a7"]
        try:
            defaultParser0.parse2(options0, stringArray0, properties0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Missing argument for option: 17Q
            self.verifyException("org.apache.commons.cli.MissingArgumentException", e)

    def test30(self) -> None:

        boolean0 = False
        options0 = Options()
        options0.addRequiredOption("a7", "a7", True, "a7")
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser_Builder0.setStripLeadingAndTrailingQuotes(boolean0)
        option_Builder0 = Option.builder1("a7")
        option_Builder1 = option_Builder0.hasArgs()
        option0 = option_Builder1.build()
        options0.addOption0(option0)
        defaultParser0 = defaultParser_Builder0.build()
        stringArray0 = ["--a7"]
        properties0 = {}
        try:
            defaultParser0.parse2(options0, stringArray0, properties0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Missing required option: a7
            self.verifyException("org.apache.commons.cli.MissingOptionException", e)

    def test29(self) -> None:

        boolean0 = False
        defaultParser0 = DefaultParser(1757, True, boolean0)
        options0 = Options()
        options0.addRequiredOption("a7", "a7", True, "a7")
        stringArray0 = [None] * 5
        stringArray0[0] = "--a7"
        stringArray0[1] = '-"%Y6)Hb@U0'
        stringArray0[2] = "--a7"
        stringArray0[3] = "a7"
        stringArray0[4] = "e=Q}U8Te5`g(/W8`I/"
        commandLine0 = defaultParser0.parse0(options0, stringArray0)
        self.assertIsNotNone(commandLine0)

    def test28(self) -> None:

        options0 = Options()
        options0.addRequiredOption("a7", "a7", True, "a7")
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser_Builder0.setAllowPartialMatching(False)
        defaultParser0 = defaultParser_Builder0.build()
        stringArray0 = [None] * 2
        stringArray0[0] = "--a7"
        try:
            defaultParser0.parse1(options0, stringArray0, True)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.Util", e)

    def test27(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        defaultParser0._handleConcatenatedOptions("]")

    def test26(self) -> None:

        boolean0 = False
        defaultParser0 = DefaultParser(1757, True, boolean0)

        try:
            defaultParser0._handleConcatenatedOptions('-"%Y6)Hb@U0')
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    def test25(self) -> None:

        boolean0 = True
        options0 = Options()
        properties0 = {}
        defaultParser0 = DefaultParser(-77807378, True, boolean0)
        stringArray0 = ["--<Y"]
        defaultParser0.parse3(options0, stringArray0, properties0, True)
        defaultParser0._handleConcatenatedOptions("--)")

    def test24(self) -> None:

        options0 = Options()
        options1 = options0.addRequiredOption("a7", "a7", True, "a7")
        defaultParser_Builder0 = DefaultParser.builder()
        boolean0 = bool("---e=Q}!/8Te5`g(/W8`I/")
        defaultParser_Builder0.setStripLeadingAndTrailingQuotes(boolean0)
        defaultParser0 = defaultParser_Builder0.build()
        stringArray0 = [""] * 8
        stringArray0[0] = "--a7"
        stringArray0[2] = "---e=Q}!/8Te5`g(/W8`I/"
        try:
            defaultParser0.parse0(options1, stringArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unrecognized option: ---e=Q}!/8Te5`g(/W8`I/
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    def test23(self) -> None:

        options0 = Options()
        optionGroup0 = OptionGroup()
        option0 = Option.Option2("a7", False, "a7")
        optionGroup1 = optionGroup0.addOption(option0)
        options1 = options0.addOptionGroup(optionGroup1)
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        stringArray0 = [None] * 7
        stringArray0[0] = "a7"
        stringArray0[1] = "-a7"
        # Undeclared exception in Java code
        try:
            defaultParser0.parse0(options1, stringArray0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            pass

    def test22(self) -> None:

        options0 = Options()
        defaultParser_Builder0 = DefaultParser.builder()
        properties0 = {}
        properties0["a7"] = defaultParser_Builder0
        defaultParser0 = defaultParser_Builder0.build()
        try:
            defaultParser0.parse2(options0, None, properties0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Default option wasn't defined
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    def test21(self) -> None:

        boolean0 = True
        options0 = Options()
        defaultParser0 = DefaultParser(0, True, boolean0)
        stringArray0 = [None] * 5
        stringArray0[0] = "HNb#}Cz Zh"
        stringArray0[1] = "-Y"
        try:
            defaultParser0.parse1(options0, stringArray0, False)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unrecognized option: -Y
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    def test20(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        options0 = Options()
        options0.addRequiredOption("17Q", "a7", True, "17Q")
        defaultParser0 = defaultParser_Builder0.build()
        stringArray0 = [None] * 5
        stringArray0[0] = "--a7"
        stringArray0[1] = "a7"
        stringArray0[2] = "-e=Q}!/8Te5`g(/W8`I/"
        try:
            defaultParser0.parse0(options0, stringArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unrecognized option: -e=Q}!/8Te5`g(/W8`I/
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    def test19(self) -> None:

        boolean0 = False
        defaultParser0 = DefaultParser(0, True, boolean0)
        options0 = Options()
        stringArray0 = ["a72@9'`8,", "-^V'Itm$9U9=5"]
        try:
            defaultParser0.parse0(options0, stringArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unrecognized option: -^V'Itm$9U9=5
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    def test18(self) -> None:

        boolean0 = True
        defaultParser0 = DefaultParser(2786, False, boolean0)
        options0 = Options()
        stringArray0 = ["--"]
        properties0 = {}
        commandLine0 = defaultParser0.parse2(options0, stringArray0, properties0)
        self.assertIsNotNone(commandLine0)

    def test17(self) -> None:

        boolean0 = True
        defaultParser0 = DefaultParser(2786, False, boolean0)
        options0 = Options()
        properties0 = {}
        stringArray0 = [None] * 9
        stringArray0[0] = 'wF_;l@-0|Ks"'
        stringArray0[1] = "-"

        try:
            defaultParser0.parse3(options0, stringArray0, properties0, False)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")

    def test16(self) -> None:

        options0 = Options()
        options1 = options0.addRequiredOption("a7", "a7", True, "a7")
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        stringArray0 = [None] * 8
        stringArray0[0] = "--a7"
        stringArray0[1] = "---e=Q}!/8Te5`g(/W8`I/"
        try:
            defaultParser0.parse0(options1, stringArray0)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError:
            pass

    def test15(self) -> None:

        options0 = Options()
        options0.addRequiredOption("a7", "a7", True, "a7")
        defaultParser_Builder0 = DefaultParser.builder()
        boolean0 = True
        defaultParser_Builder0.setStripLeadingAndTrailingQuotes(boolean0)
        defaultParser0 = defaultParser_Builder0.build()
        stringArray0 = [None] * 5
        stringArray0[0] = "--a7"
        properties0 = {}
        try:
            defaultParser0.parse2(options0, stringArray0, properties0)
            self.fail("Expecting exception: RuntimeError")
        except Exception as e:
            self.verifyException("org.apache.commons.cli.Util", e)

    def test14(self) -> None:

        boolean0 = True
        defaultParser0 = DefaultParser(1, boolean0, boolean0)

    def test13(self) -> None:

        boolean0 = False
        defaultParser0 = DefaultParser(0, False, boolean0)
        options0 = Options()
        optionGroup0 = OptionGroup()
        option0 = Option.Option1("", "<Y")
        optionGroup1 = optionGroup0.addOption(option0)
        options0.addOptionGroup(optionGroup1)
        stringArray0 = [None] * 9

        try:
            defaultParser0.parse3(options0, stringArray0, None, False)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")

    def test12(self) -> None:

        defaultParser0 = DefaultParser(-1855, False, None)
        options0 = Options()
        properties0 = {}
        commandLine0 = defaultParser0.parse3(options0, None, properties0, True)
        self.assertIsNotNone(commandLine0)

    def test11(self) -> None:

        boolean0 = False
        defaultParser0 = DefaultParser(0, False, boolean0)

        try:
            defaultParser0._checkRequiredOptions()
            self.fail("Expecting exception: MissingOptionException")

        except MissingOptionException.MissingOptionException1:
            pass

    def test10(self) -> None:

        boolean0 = True
        defaultParser0 = DefaultParser(1507, False, boolean0)
        linkedList0 = []
        object0 = object()
        linkedList0.append(object0)
        defaultParser0._expectedOpts = linkedList0
        try:
            defaultParser0._checkRequiredOptions()
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Missing required option: <object object at 0x7f81c924>
            self.assertIsInstance(e, MissingOptionException)

    def test09(self) -> None:

        options0 = Options()
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        defaultParser0.parse1(options0, None, False)
        try:
            defaultParser0.handleConcatenatedOptions("-^V'Itm$AU9=5")
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unrecognized option: -^V'Itm$AU9=5
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    def test08(self) -> None:

        options0 = Options()
        defaultParser_Builder0 = Builder()
        defaultParser0 = defaultParser_Builder0.build()
        stringArray0 = []
        properties0 = {}
        properties0[defaultParser_Builder0] = defaultParser_Builder0

        with pytest.raises(ClassCastException):
            defaultParser0.parse2(options0, stringArray0, properties0)
            self.fail("Expecting exception: ClassCastException")

        self.verifyException("java.util.Properties", e)

    def test07(self) -> None:

        boolean0 = True
        defaultParser0 = DefaultParser(1757, True, boolean0)
        options0 = Options()
        properties0 = {}
        stringArray0 = ["", ""]
        properties0[defaultParser0] = "EG'LT"
        stringArray0[0] = "EG'LT"

        with pytest.raises(ClassCastException):
            defaultParser0.parse3(options0, stringArray0, properties0, True)
            self.fail("Expecting exception: ClassCastException")

        self.verifyException("java.util.Properties", e)

    def test06(self) -> None:

        options0 = Options()
        defaultParser_Builder0 = DefaultParser.builder()
        stringArray0 = ["-,"]
        defaultParser0 = defaultParser_Builder0.build()
        properties0 = {}
        try:
            defaultParser0.parse3(options0, stringArray0, properties0, False)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unrecognized option: -,
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    def test05(self) -> None:

        options0 = Options()
        stringArray0 = ["----bHyQ}NI|`fyQSze=|"]
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        commandLine0 = defaultParser0.parse1(options0, stringArray0, True)
        self.assertIsNotNone(commandLine0)

    def test04(self) -> None:

        boolean0 = False
        defaultParser0 = DefaultParser(0, True, boolean0)
        options0 = Options()
        properties0 = {}
        stringArray0 = ["-;RfOwY"]
        commandLine0 = defaultParser0.parse3(options0, stringArray0, properties0, True)
        self.assertIsNotNone(commandLine0)

    def test03(self) -> None:

        options0 = Options()
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        stringArray0 = [""] * 5
        stringArray0[0] = "-e=Q}!/8Te5`g(/W8`I/"
        commandLine0 = defaultParser0.parse1(options0, stringArray0, True)
        self.assertIsNotNone(commandLine0)

    def test02(self) -> None:

        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser0 = defaultParser_Builder0.build()
        options0 = Options()
        stringArray0 = [""] * 5
        stringArray0[0] = "A[:Tyr#Yqv"
        defaultParser0.parse1(options0, stringArray0, True)
        defaultParser0.checkRequiredOptions()

    def test01(self) -> None:

        options0 = Options()
        stringArray0 = ["----bHyQ}NI|`fyQSze=|"]
        defaultParser_Builder0 = DefaultParser.builder()
        defaultParser_Builder0.setAllowPartialMatching(False)
        defaultParser0 = defaultParser_Builder0.build()
        try:
            defaultParser0.parse0(options0, stringArray0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # Unrecognized option: ----bHyQ}NI|`fyQSze=|
            self.verifyException("org.apache.commons.cli.DefaultParser", e)

    def test00(self) -> None:

        boolean0 = False
        defaultParser0 = DefaultParser(0, True, boolean0)
        defaultParser0._handleConcatenatedOptions("")
