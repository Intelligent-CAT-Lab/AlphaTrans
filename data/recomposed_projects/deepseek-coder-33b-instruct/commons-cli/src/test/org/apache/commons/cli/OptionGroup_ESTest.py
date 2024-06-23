from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.OptionGroup import *

# from src.main.org.apache.commons.cli.OptionGroup_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class OptionGroup_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test12(self) -> None:

        optionGroup0 = OptionGroup()
        collection0 = optionGroup0.getOptions()
        self.assertIsNotNone(collection0)

    @pytest.mark.test
    def test11(self) -> None:

        optionGroup0 = OptionGroup()
        boolean0 = optionGroup0.isRequired()
        self.assertFalse(boolean0)

    @pytest.mark.test
    def test10(self) -> None:

        optionGroup0 = OptionGroup()
        optionGroup0.setRequired(True)
        option0 = Option.Option2("", True, "")
        optionGroup0.addOption(option0)
        self.assertTrue(optionGroup0.isRequired())

    @pytest.mark.test
    def test09(self) -> None:

        optionGroup0 = OptionGroup()
        collection0 = optionGroup0.getNames()
        self.assertIsNotNone(collection0)

    @pytest.mark.test
    def test08(self) -> None:

        optionGroup0 = OptionGroup()
        option_Builder0 = Option.builder0()
        option0 = Option(
            842, "F2Dp#LT'h3@K", "F2Dp#LT'h3@K", "F2Dp#LT'h3@K", True, option_Builder0
        )
        option0.setLongOpt("J}M=~SL3%[Hjh")
        optionGroup0.setSelected(option0)
        option0.setLongOpt("F2Dp#LT'h3@K")
        try:
            optionGroup0.setSelected(option0)
            self.fail("Expecting exception: Exception")

        except Exception as e:
            # The option 'F2Dp#LT'h3@K' was specified but an option from this group has already been selected: 'J}M=~SL3%[Hjh'
            self.verifyException("org.apache.commons.cli.AlreadySelectedException", e)

    @pytest.mark.test
    def test07(self) -> None:
        optionGroup0 = OptionGroup()
        optionGroup0.setSelected(None)
        self.assertIsNone(optionGroup0.getSelected())

    @pytest.mark.test
    def test06(self) -> None:

        optionGroup0 = OptionGroup()
        option0 = Option.Option1("", "")
        optionGroup0.setSelected(option0)
        optionGroup0.setSelected(option0)
        self.assertFalse(option0.hasLongOpt())

    @pytest.mark.test
    def test05(self) -> None:

        optionGroup0 = OptionGroup()
        option0 = Option.Option1("q7D", "q7D")
        optionGroup1 = optionGroup0.addOption(option0)
        option_Builder0 = Option.builder0()
        option1 = Option(-2968, "q7D", "]", "q7D", False, option_Builder0)
        optionGroup1.addOption(option1)
        string0 = optionGroup0.toString()
        self.assertEqual("[-q7D q7D, --null]", string0)

    @pytest.mark.test
    def test04(self) -> None:

        optionGroup0 = OptionGroup()
        string0 = optionGroup0.getSelected()
        self.assertIsNone(string0)

    @pytest.mark.test
    def test03(self) -> None:

        optionGroup0 = OptionGroup()
        try:
            optionGroup0.addOption(None)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertIsNotNone(str(e))
            self.assertTrue("org.apache.commons.cli.OptionGroup" in str(e))

    @pytest.mark.test
    def test02(self) -> None:

        optionGroup0 = OptionGroup()
        option0 = Option.Option1("", "")
        optionGroup0.setSelected(option0)
        string0 = optionGroup0.getSelected()
        self.assertEqual("", string0)

    @pytest.mark.test
    def test01(self) -> None:

        optionGroup0 = OptionGroup()
        option0 = Option.Option2("q7D", False, "")
        optionGroup0.setSelected(option0)
        string0 = optionGroup0.getSelected()
        self.assertEqual("q7D", string0)

    @pytest.mark.test
    def test00(self) -> None:
        optionGroup0 = OptionGroup()
        optionGroup0.setRequired(True)
        boolean0 = optionGroup0.isRequired()
        self.assertTrue(boolean0)
