from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.AlreadySelectedException import *

# from src.test.org.apache.commons.cli.AlreadySelectedException_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class AlreadySelectedException_ESTest(unittest.TestCase):

    def test12(self) -> None:
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException0(
            ""
        )
        option0 = alreadySelectedException0.getOption()
        self.assertIsNone(option0)

    def test11(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option0 = Option(-1013, "f", "N)N", "0!)", False, option_Builder0)
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        optionGroup1 = alreadySelectedException0.getOptionGroup()
        assert optionGroup1.getSelected() is None

    def test10(self) -> None:

        optionGroup0 = OptionGroup()
        try:
            AlreadySelectedException.AlreadySelectedException1(optionGroup0, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.cli.AlreadySelectedException", e)

    def test09(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder1("")
        option_Builder0.numberOfArgs(0)
        option0 = option_Builder0.build()
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        option1 = alreadySelectedException0.getOption()
        assert not option1.isRequired()

    def test08(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder1("")
        option_Builder1 = option_Builder0.option("r")
        option0 = option_Builder1.build()
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        option1 = alreadySelectedException0.getOption()
        assert option1.getValue0() is None

    def test07(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option_Builder0.argName("IEz_7")
        option0 = Option(2131, None, None, None, False, option_Builder0)
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        option1 = alreadySelectedException0.getOption()
        self.assertIsNone(option1.getOpt())

    def test06(self) -> None:

        optionGroup0 = OptionGroup()
        option0 = Option.Option2(None, True, " [ARG]")
        option0.setArgs(2131)
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        option1 = alreadySelectedException0.getOption()
        self.assertIsNone(option1.getLongOpt())

    def test05(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option0 = Option(0, "", "", "`C%|.x0SIuAvS10", False, option_Builder0)
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        option1 = alreadySelectedException0.getOption()
        self.assertFalse(option1.isRequired())

    def test04(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option0 = Option(-1013, "f", "N)N", "0!)", False, option_Builder0)
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        option0.setOptionalArg(True)
        option1 = alreadySelectedException0.getOption()
        self.assertIsNone(option1.getLongOpt())

    def test03(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.valueSeparator1("'")
        option0 = Option(2131, None, None, None, False, option_Builder1)
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        option1 = alreadySelectedException0.getOption()
        self.assertEqual(-1, option1.getArgs())

    def test02(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder1("")
        option0 = Option(61, "'", "'", None, False, option_Builder0)
        option0.setRequired(True)
        alreadySelectedException0 = AlreadySelectedException("'", optionGroup0, option0)
        option1 = alreadySelectedException0.getOption()
        self.assertIs(option0, option1)

    def test01(self) -> None:

        optionGroup0 = OptionGroup()
        optionGroup0.setRequired(True)
        option_Builder0 = Option.builder0()
        option0 = Option(-1013, "f", "N)N", "0!)", False, option_Builder0)
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException1(
            optionGroup0, option0
        )
        optionGroup1 = alreadySelectedException0.getOptionGroup()
        self.assertIsNone(optionGroup1.getSelected())

    def test00(self) -> None:
        alreadySelectedException0 = AlreadySelectedException.AlreadySelectedException0(
            ""
        )
        optionGroup0 = alreadySelectedException0.getOptionGroup()
        self.assertIsNone(optionGroup0)
