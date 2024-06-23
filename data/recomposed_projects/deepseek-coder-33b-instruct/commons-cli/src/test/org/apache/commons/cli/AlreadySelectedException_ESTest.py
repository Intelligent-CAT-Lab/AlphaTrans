from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.AlreadySelectedException import *

# from src.main.org.apache.commons.cli.AlreadySelectedException_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class AlreadySelectedException_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test11(self) -> None:

        optionGroup0 = OptionGroup()
        option0 = Option.Option1("", '`"S$9z')
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        optionGroup1 = alreadySelectedException0.getOptionGroup()
        self.assertFalse(optionGroup1.isRequired())

    @pytest.mark.test
    def test10(self) -> None:

        option_Builder0 = Option.builder0()
        option0 = Option(
            -603, "", "$n/T5B&rqV*C+dNJ5", "$n/T5B&rqV*C+dNJ5", False, option_Builder0
        )

        try:
            AlreadySelectedException.AlreadySelectedException1(None, option0)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.AlreadySelectedException", e)

    @pytest.mark.test
    def test09(self) -> None:

        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.numberOfArgs(609)
        option0 = Option(609, "?vMC", "", None, True, option_Builder1)
        optionGroup0 = OptionGroup()
        alreadySelectedException0 = AlreadySelectedException(
            "[ARG...]", optionGroup0, option0
        )
        option1 = alreadySelectedException0.getOption()
        self.assertFalse(option1.isRequired())

    @pytest.mark.test
    def test08(self) -> None:

        optionGroup0 = OptionGroup()
        option0 = Option.Option1("", '`"S$9z')
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        option0.setArgs(0)
        option1 = alreadySelectedException0.getOption()
        self.assertFalse(option1.hasArgName())

    @pytest.mark.test
    def test07(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.longOpt("an>'^?d*e-")
        option0 = Option(48, "an>'^?d*e-", ".FwdooYC8{", None, True, option_Builder0)
        optionGroup0 = OptionGroup()
        alreadySelectedException0 = AlreadySelectedException(
            ".FwdooYC8{", optionGroup0, option0
        )
        option1 = alreadySelectedException0.getOption()
        self.assertFalse(option1.hasValueSeparator())

    @pytest.mark.test
    def test06(self) -> None:

        optionGroup0 = OptionGroup()
        option0 = Option.Option2("", True, "")
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        option0.setArgName("[]")
        option1 = alreadySelectedException0.getOption()
        self.assertEqual(Option.UNINITIALIZED, -1)

    @pytest.mark.test
    def test05(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.optionalArg(True)
        option0 = Option(
            560,
            None,
            "Cannot add value, list full.",
            "[ARG...]",
            False,
            option_Builder1,
        )
        optionGroup0 = OptionGroup()
        alreadySelectedException0 = AlreadySelectedException("", optionGroup0, option0)
        option1 = alreadySelectedException0.getOption()
        self.assertEqual(option1, option0)

    @pytest.mark.test
    def test04(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.valueSeparator1("8")
        option0 = Option(48, "an>'^?d*e-", ".Fwd}:o`OYC8{", None, True, option_Builder1)
        optionGroup0 = OptionGroup()
        alreadySelectedException0 = AlreadySelectedException(
            ".Fwd}:o`OYC8{", optionGroup0, option0
        )
        option1 = alreadySelectedException0.getOption()
        self.assertEqual(Option.UNLIMITED_VALUES, -2)

    @pytest.mark.test
    def test03(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.required1(True)
        option0 = Option(48, "an>'^?d*e-", ".Fwd}:o`OYC8{", None, True, option_Builder0)
        optionGroup0 = OptionGroup()
        alreadySelectedException0 = AlreadySelectedException(
            ".Fwd}:o`OYC8{", optionGroup0, option0
        )
        option1 = alreadySelectedException0.getOption()
        self.assertEqual(-1, Option.UNINITIALIZED)

    @pytest.mark.test
    def test02(self) -> None:
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException0(
            None
        )
        option0 = alreadySelectedException0.getOption()
        self.assertIsNone(option0)

    @pytest.mark.test
    def test01(self) -> None:

        optionGroup0 = OptionGroup()
        option0 = Option.Option1("", '`"S$9z')
        optionGroup0.setRequired(True)
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        optionGroup1 = alreadySelectedException0.getOptionGroup()
        self.assertIs(optionGroup0, optionGroup1)

    @pytest.mark.test
    def test00(self) -> None:
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException0(
            ".Fwd}:o`OYC8{"
        )
        optionGroup0 = alreadySelectedException0.getOptionGroup()
        self.assertIsNone(optionGroup0)
