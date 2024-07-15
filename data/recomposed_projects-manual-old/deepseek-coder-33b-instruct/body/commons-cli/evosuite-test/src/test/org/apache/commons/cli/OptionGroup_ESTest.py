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

# from src.test.org.apache.commons.cli.OptionGroup_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class OptionGroup_ESTest(unittest.TestCase):

    def test13(self) -> None:

        optionGroup0 = OptionGroup()
        boolean0 = optionGroup0.isRequired()
        self.assertFalse(boolean0)

    def test12(self) -> None:

        optionGroup0 = OptionGroup()
        collection0 = optionGroup0.getNames()
        assert collection0 is not None

    def test11(self) -> None:

        optionGroup0 = OptionGroup()
        string0 = optionGroup0.getSelected()
        self.assertIsNone(string0)

    def test10(self) -> None:
        optionGroup0 = OptionGroup()
        optionGroup0.setSelected(None)
        self.assertIsNone(optionGroup0.getSelected())

    def test09(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option0 = Option(1, ",#mo|9z3u<6T*", "", "", False, option_Builder0)
        option_Builder1 = option_Builder0.longOpt("--")
        option1 = Option(
            2147483645,
            ",#mo|9z3u<6T*",
            "--",
            "The addValue method is not intended for client use. Subclasses should use the addValueForProcessing method instead. ",
            True,
            option_Builder1,
        )
        optionGroup0.setSelected(option1)
        try:
            optionGroup0.setSelected(option0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # The option 'null' was specified but an option from this group has already been selected: '--'
            self.verifyException("org.apache.commons.cli.AlreadySelectedException", e)

    def test08(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder1("")
        option0 = option_Builder0.build()
        optionGroup0.setSelected(option0)
        optionGroup0.setSelected(option0)
        self.assertEqual((-1), Option.UNINITIALIZED)

    def test07(self) -> None:

        optionGroup0 = OptionGroup()
        option0 = Option.Option1("JN", "=x@IC-)5T]Z9qG'[}l")
        optionGroup0.addOption(option0)
        string0 = optionGroup0.toString()
        self.assertEqual("[-JN =x@IC-)5T]Z9qG'[}l]", string0)

    def test06(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option0 = Option(1, ",#mo|9z3u<6T*", "", "", False, option_Builder0)
        optionGroup0.addOption(option0)
        option_Builder1 = option_Builder0.longOpt("--")
        option1 = Option(
            2147483645,
            ",#mo|9z3u<6T*",
            "--",
            "The addValue method is not intended for client use. Subclasses should use the addValueForProcessing method instead. ",
            True,
            option_Builder1,
        )
        optionGroup1 = optionGroup0.addOption(option1)
        string0 = optionGroup1.toString()
        self.assertEqual("[--null, ----]", string0)

    def test05(self) -> None:

        optionGroup0 = OptionGroup()
        collection0 = optionGroup0.getOptions()
        assert collection0 is not None

    def test04(self) -> None:

        optionGroup0 = OptionGroup()
        try:
            optionGroup0.addOption(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test03(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option0 = Option(
            703,
            "org.apache.commons.cli.Option$Builder",
            "]",
            "]",
            True,
            option_Builder0,
        )
        optionGroup0.setRequired(True)
        optionGroup0.addOption(option0)
        self.assertTrue(optionGroup0.isRequired())

    def test02(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder1("")
        option0 = option_Builder0.build()
        optionGroup0.setSelected(option0)
        string0 = optionGroup0.getSelected()
        self.assertEqual("", string0)

    def test01(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.longOpt("--")
        option0 = Option(
            2147483645,
            ",#mo|9z3u<6T*",
            "--",
            "The addValue method is not intended for client use. Subclasses should use the addValueForProcessing method instead. ",
            True,
            option_Builder1,
        )
        optionGroup0.setSelected(option0)
        string0 = optionGroup0.getSelected()
        self.assertEqual("--", string0)

    def test00(self) -> None:
        optionGroup0 = OptionGroup()
        optionGroup0.setRequired(True)
        boolean0 = optionGroup0.isRequired()
        self.assertTrue(boolean0)
