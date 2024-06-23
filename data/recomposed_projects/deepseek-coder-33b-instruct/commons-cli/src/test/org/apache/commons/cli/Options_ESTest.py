from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Options import *

# from src.main.org.apache.commons.cli.Options_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Options_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test34(self) -> None:
        options0 = Options()
        collection0 = options0.getOptions()
        self.assertIsNotNone(collection0)

    @pytest.mark.test
    def test33(self) -> None:

        options0 = Options()
        try:
            options0.addOption1("x)-pq5voD+D:4n", True, "zHU")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test32(self) -> None:

        options0 = Options()
        list0 = options0.getRequiredOptions()
        self.assertEqual(0, len(list0))

    @pytest.mark.test
    def test31(self) -> None:

        options0 = Options()
        string0 = options0.toString()
        self.assertIsNotNone(string0)

    @pytest.mark.test
    def test30(self) -> None:

        options0 = Options()
        option_Builder0 = Option.builder0()
        option0 = Option(-1994091957, None, 'c"', ")C|~,1UB5", False, option_Builder0)
        optionGroup0 = options0.getOptionGroup(option0)
        self.assertIsNone(optionGroup0)

    @pytest.mark.test
    def test29(self) -> None:
        options0 = Options()
        collection0 = options0.getOptionGroups()
        assert collection0 is not None

    @pytest.mark.test
    def test28(self) -> None:

        options0 = Options()
        options1 = options0.addOption2("d", "d")
        boolean0 = options1.hasOption("d")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test27(self) -> None:

        options0 = Options()
        options0.addRequiredOption(
            "NO_ARGS_ALLOWED", "NO_ARGS_ALLOWED", False, "NO_ARGS_ALLOWED"
        )
        list0 = options0.getMatchingOptions("NO_ARGS_ALLOWED")
        self.assertTrue("NO_ARGS_ALLOWED" in list0)

    @pytest.mark.test
    def test26(self) -> None:

        options0 = Options()
        options0.addRequiredOption(
            "NO_ARGS_ALLOWED", "NO_ARGS_ALLOWED", False, "NO_ARGS_ALLOWED"
        )
        list0 = options0.getMatchingOptions("')4n|,.")
        self.assertEqual(0, len(list0))

    @pytest.mark.test
    def test25(self) -> None:

        options0 = Options()
        options0.addOption3("0U6", "0U6", True, "0U6")
        list0 = options0.getMatchingOptions("")
        self.assertTrue("0U6" in list0)

    @pytest.mark.test
    def test24(self) -> None:

        options0 = Options()
        option0 = options0.getOption(None)
        self.assertIsNone(option0)

    @pytest.mark.test
    def test23(self) -> None:

        options0 = Options()
        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option0 = Option(-1, "", "urZoxan=9g5", "", False, option_Builder0)
        optionGroup1 = optionGroup0.addOption(option0)
        options0.addOptionGroup(optionGroup1)
        option1 = options0.getOption(None)
        self.assertFalse(option1.isRequired())
        self.assertIsNotNone(option1)

    @pytest.mark.test
    def test22(self) -> None:

        options0 = Options()
        boolean0 = options0.hasLongOption("'k)C|~h,qE|tB}$}")
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test21(self) -> None:

        options0 = Options()
        options1 = options0.addRequiredOption(
            "NO_ARGS_ALLOWED", "NO_ARGS_ALLOWED", False, "NO_ARGS_ALLOWED"
        )
        boolean0 = options1.hasLongOption("NO_ARGS_ALLOWED")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test20(self) -> None:

        options0 = Options()
        boolean0 = options0.hasOption("Sz")
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test19(self) -> None:

        options0 = Options()
        options0.addRequiredOption("p", ")C|~h,E|tB5}$}", False, "p")
        boolean0 = options0.hasOption(")C|~h,E|tB5}$}")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test18(self) -> None:

        options0 = Options()
        boolean0 = options0.hasShortOption("A CloneNotSupportedException was thrown: ")
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test17(self) -> None:

        options0 = Options()
        options1 = options0.addOption2("J8", "J8")
        boolean0 = options1.hasShortOption("J8")
        self.assertTrue(boolean0)

    @pytest.mark.test
    def test16(self) -> None:

        options0 = Options()
        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.longOpt("")
        option0 = option_Builder1.build()
        options1 = options0.addOption0(option0)
        option1 = options1.getOption("")
        self.assertFalse(option1.hasArgName())

    @pytest.mark.test
    def test15(self) -> None:

        options0 = Options()
        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.required0()
        option0 = option_Builder1.build()
        options1 = options0.addOption0(option0)
        options2 = options1.addOption0(option0)
        self.assertIs(options0, options2)

    @pytest.mark.test
    def test14(self) -> None:

        options0 = Options()

        try:
            options0.addOption0(None)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: NullPointerException")

    @pytest.mark.test
    def test13(self) -> None:

        options0 = Options()
        try:
            options0.addOption3(
                "' Op_tions:I[ sho>t ",
                "' Op_tions:I[ sho>t ",
                False,
                "' Op_tions:I[ sho>t ",
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test12(self) -> None:

        options0 = Options()

        try:
            options0.addOptionGroup(None)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.Options", e)

    @pytest.mark.test
    def test11(self) -> None:

        options0 = Options()
        try:
            options0.addRequiredOption(
                "+`gLm]Ys|]}n9", "+`gLm]Ys|]}n9", True, "+`gLm]Ys|]}n9"
            )
            self.fail("Expecting exception: ValueError")
        except ValueError as e:
            # The option '+`gLm]Ys|]}n9' contains an illegal character : '+'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test10(self) -> None:

        options0 = Options()
        options0.addRequiredOption("mL", "mL", True, "mL")

        try:
            options0.getMatchingOptions(None)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: NullPointerException")

    @pytest.mark.test
    def test09(self) -> None:

        options0 = Options()
        try:
            options0.getOptionGroup(None)
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            verifyException("org.apache.commons.cli.Options", e)

    @pytest.mark.test
    def test08(self) -> None:

        options0 = Options()
        options1 = options0.addOption1("", True, "")
        self.assertIs(options0, options1)

    @pytest.mark.test
    def test07(self) -> None:

        options0 = Options()
        options1 = options0.addOption2("", "")
        option0 = options1.getOption("")
        self.assertFalse(option0.hasLongOpt())
        self.assertIsNotNone(option0)
        self.assertFalse(option0.hasArg())

    @pytest.mark.test
    def test06(self) -> None:

        options0 = Options()
        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.optionalArg(True)
        option0 = option_Builder1.build()
        options1 = options0.addOption0(option0)
        option1 = options1.getOption("")
        self.assertIsNone(option1.getLongOpt())

    @pytest.mark.test
    def test05(self) -> None:

        options0 = Options()
        options1 = options0.addRequiredOption("", "", False, "")
        option0 = options1.getOption("")
        self.assertTrue(option0.isRequired())
        self.assertFalse(option0.hasArg())

    @pytest.mark.test
    def test04(self) -> None:

        options0 = Options()
        option0 = Option.Option2("", True, None)
        optionGroup0 = OptionGroup()
        optionGroup1 = optionGroup0.addOption(option0)
        options1 = options0.addOptionGroup(optionGroup1)
        optionGroup2 = options1.getOptionGroup(option0)
        self.assertFalse(option0.isRequired())
        self.assertIsNotNone(optionGroup2)

    @pytest.mark.test
    def test03(self) -> None:

        options0 = Options()
        option_Builder0 = Option.builder0()
        option0 = Option(-1994091957, None, 'c"', ")C|~,1UB5", False, option_Builder0)
        optionGroup0 = OptionGroup()
        optionGroup1 = optionGroup0.addOption(option0)
        optionGroup1.setRequired(True)
        options0.addOptionGroup(optionGroup0)
        optionGroup2 = options0.getOptionGroup(option0)
        assert optionGroup2 is not None
        assert not option0.isRequired()

    @pytest.mark.test
    def test02(self) -> None:

        options0 = Options()
        options1 = options0.addRequiredOption(None, None, True, None)
        list0 = options1.helpOptions()
        self.assertEqual(len(list0), 1)

    @pytest.mark.test
    def test01(self) -> None:

        options0 = Options()
        list0 = options0.helpOptions()
        self.assertTrue(not list0)

    @pytest.mark.test
    def test00(self) -> None:

        options0 = Options()
        try:
            options0.addOption2("u^Lq#7|W<k7$}SmL=0", "")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.cli.OptionValidator", e)
