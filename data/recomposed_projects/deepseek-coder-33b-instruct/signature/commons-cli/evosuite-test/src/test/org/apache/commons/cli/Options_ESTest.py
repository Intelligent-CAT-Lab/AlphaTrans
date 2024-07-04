from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *

# from src.test.org.apache.commons.cli.Options_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Options_ESTest(unittest.TestCase):

    def test36(self) -> None:

        options0 = Options()
        options1 = options0.addRequiredOption("ab", "ab", False, "ab")
        boolean0 = options1.hasLongOption("ab")
        self.assertTrue(boolean0)

    def test35(self) -> None:
        options0 = Options()
        collection0 = options0.getOptions()
        assert collection0 is not None

    def test34(self) -> None:

        options0 = Options()
        list0 = options0.getRequiredOptions()
        self.assertEqual(0, len(list0))

    def test33(self) -> None:

        options0 = Options()
        string0 = options0.toString()
        self.assertIsNotNone(string0)

    def test32(self) -> None:

        options0 = Options()
        try:
            options0.getOptionGroup(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test31(self) -> None:
        options0 = Options()
        collection0 = options0.getOptionGroups()
        assert collection0 is not None

    def test30(self) -> None:

        options0 = Options()
        options1 = options0.addOption2("", "N,?#*fE")
        self.assertIs(options1, options0)

    def test29(self) -> None:

        options0 = Options()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.required1(True)
        option0 = Option(1, " :: ", "N,?#*fE", None, True, option_Builder1)
        options1 = options0.addOption0(option0)
        options2 = options0.addOption0(option0)
        self.assertIs(options2, options1)

    def test28(self) -> None:

        options0 = Options()
        options0.addOption3("", 'nIW;QV"gUH+C', True, 'nIW;QV"gUH+C')
        list0 = options0.getMatchingOptions('nIW;QV"gUH+C')
        self.assertTrue('nIW;QV"gUH+C' in list0)

    def test27(self) -> None:

        options0 = Options()
        options1 = options0.addOption3(None, "'6MWzZs~t'1", True, None)

        try:
            options1.getMatchingOptions(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            pass

    def test26(self) -> None:

        options0 = Options()
        options1 = options0.addOption3("", "", True, "")
        list0 = options1.getMatchingOptions("sU`d")
        self.assertEqual(0, len(list0))

    def test25(self) -> None:

        options0 = Options()
        options0.addRequiredOption("", "B", True, "B")
        list0 = options0.getMatchingOptions("")
        self.assertTrue("B" in list0)

    def test24(self) -> None:

        options0 = Options()
        option0 = options0.getOption(None)
        self.assertIsNone(option0)

    def test23(self) -> None:

        options0 = Options()
        boolean0 = options0.hasLongOption(None)
        self.assertFalse(boolean0)

    def test22(self) -> None:

        options0 = Options()
        boolean0 = options0.hasOption("")
        self.assertFalse(boolean0)

    def test21(self) -> None:

        options0 = Options()
        options1 = options0.addOption2(None, None)
        boolean0 = options1.hasOption(None)
        self.assertTrue(boolean0)

    def test20(self) -> None:

        options0 = Options()
        options0.addOption3("", 'nIW;QV"gUH+C', True, 'nIW;QV"gUH+C')
        boolean0 = options0.hasOption('nIW;QV"gUH+C')
        self.assertTrue(boolean0)

    def test19(self) -> None:

        options0 = Options()
        boolean0 = options0.hasShortOption("N,?#*fE")
        self.assertFalse(boolean0)

    def test18(self) -> None:

        options0 = Options()
        options1 = options0.addOption3("", "", True, "")
        boolean0 = options1.hasShortOption("")
        self.assertTrue(boolean0)

    def test17(self) -> None:

        options0 = Options()
        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.longOpt("")
        option0 = option_Builder1.build()
        options1 = options0.addOption0(option0)
        self.assertIs(options0, options1)

    def test16(self) -> None:

        options0 = Options()

        try:
            options0.addOption0(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.Options", e)

    def test15(self) -> None:

        options0 = Options()
        try:
            options0.addOption2(")I.%HqO($VQ", ")I.%HqO($VQ")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.cli.OptionValidator", e)

    def test14(self) -> None:

        options0 = Options()
        try:
            options0.addOption3(
                "U1Kpfcbzi<9kEY", "U1Kpfcbzi<9kEY", False, "U1Kpfcbzi<9kEY"
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.cli.OptionValidator", e)

    def test13(self) -> None:

        options0 = Options()

        try:
            options0.addOptionGroup(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.Options", e)

    def test12(self) -> None:

        options0 = Options()
        try:
            options0.addRequiredOption(
                "U1Kpfcbzi<9kEY", "U1Kpfcbzi<9kEY", False, "U1Kpfcbzi<9kEY"
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.cli.OptionValidator", e)

    def test11(self) -> None:

        options0 = Options()
        options1 = options0.addOption1("KZ", True, "KZ")
        assert options1 is options0

    def test10(self) -> None:

        options0 = Options()
        options1 = options0.addOption3("s", 'nIW;QV"gUH+C', True, 'nIW;QV"gUH+C')
        option0 = options1.getOption('nIW;QV"gUH+C')
        self.assertEqual('nIW;QV"gUH+C', option0.getDescription())
        self.assertEqual(1, option0.getArgs())
        self.assertIsNotNone(option0)

    def test09(self) -> None:

        options0 = Options()
        option_Builder0 = Option.builder0()
        option_Builder0.hasArgs()
        option0 = Option(
            -1092, 'C*913)Z?>h^g"Q=', "k", 'C*913)Z?>h^g"Q=', False, option_Builder0
        )
        options0.addOption0(option0)
        option1 = options0.getOption(None)
        self.assertIsNone(option1.getValue0())

    def test08(self) -> None:

        options0 = Options()
        option_Builder0 = Option.builder0()
        option0 = Option(1, " :: ", "N,?#*fE", None, True, option_Builder0)
        option0.setValueSeparator("|")
        options1 = options0.addOption0(option0)
        option1 = options1.getOption(None)
        self.assertEqual(-2, Option.UNLIMITED_VALUES)

    def test07(self) -> None:

        options0 = Options()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.required1(True)
        option0 = Option(1, " :: ", "N,?#*fE", None, True, option_Builder1)
        options0.addOption0(option0)
        option1 = options0.getOption(None)
        self.assertIsNone(option1.getLongOpt())

    def test06(self) -> None:

        options0 = Options()
        optionGroup0 = OptionGroup()
        option0 = Option.Option1("", "~%:SVI2n")
        optionGroup1 = optionGroup0.addOption(option0)
        options0.addOptionGroup(optionGroup1)
        optionGroup2 = options0.getOptionGroup(option0)
        assert not option0.isRequired()
        assert optionGroup2 is not None

    def test05(self) -> None:

        options0 = Options()
        optionGroup0 = OptionGroup()
        option0 = Option.Option1("", "~%:SVI2n")
        optionGroup1 = optionGroup0.addOption(option0)
        optionGroup1.setRequired(True)
        options0.addOptionGroup(optionGroup1)
        optionGroup2 = options0.getOptionGroup(option0)
        assert optionGroup2 is not None
        assert not option0.isRequired()

    def test04(self) -> None:

        option0 = Option.Option2(None, True, "\!?iczs^t1=D2BcoQp")
        options0 = Options()
        optionGroup0 = options0.getOptionGroup(option0)
        self.assertIsNone(optionGroup0)

    def test03(self) -> None:

        options0 = Options()
        option_Builder0 = Option.builder0()
        option0 = Option(1, " :: ", "N,?#*fE", None, True, option_Builder0)
        options1 = options0.addOption0(option0)
        list0 = options1.helpOptions()
        self.assertFalse(len(list0) == 0)

    def test02(self) -> None:

        options0 = Options()
        list0 = options0.helpOptions()
        self.assertTrue(not list0)

    def test01(self) -> None:

        options0 = Options()
        try:
            options0.addOption1("<;KF0E4@i;7}+,|l", False, "C6;r`@:sh`rI")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.cli.OptionValidator", e)

    def test00(self) -> None:

        options0 = Options()
        options1 = options0.addRequiredOption("4M", None, True, "4M")
        assert options0 is options1
