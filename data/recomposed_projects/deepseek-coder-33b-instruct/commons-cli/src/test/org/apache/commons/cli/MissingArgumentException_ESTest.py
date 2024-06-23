from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.MissingArgumentException import *

# from src.main.org.apache.commons.cli.MissingArgumentException_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class MissingArgumentException_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test7(self) -> None:

        option0 = Option.Option2("", True, "[ksvY~p%WpVqK")
        missingArgumentException0 = MissingArgumentException(0, "", option0)

    @pytest.mark.test
    def test6(self) -> None:

        # Undeclared exception
        try:
            MissingArgumentException.MissingArgumentException1(1, "", None)
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.cli.MissingArgumentException", e)

    @pytest.mark.test
    def test5(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.argName("[ option: ")
        option0 = Option(1, "~U@", "~U@", "~U@", False, option_Builder1)
        missingArgumentException0 = MissingArgumentException(1, "[ option: ", option0)
        option1 = missingArgumentException0.getOption()
        self.assertFalse(option1.hasOptionalArg())

    @pytest.mark.test
    def test4(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.hasArgs()
        option0 = Option(-94, None, None, None, True, option_Builder1)
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            1, None, option0
        )
        option1 = missingArgumentException0.getOption()
        self.assertIsNone(option1.getOpt())

    @pytest.mark.test
    def test3(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.optionalArg(True)
        option_Builder0.longOpt("5g]_'\!`.&96A3hN)")
        option0 = option_Builder0.build()
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            1, "5g]_'\!`.&96A3hN)", option0
        )
        option1 = missingArgumentException0.getOption()
        assert not option1.hasValueSeparator()

    @pytest.mark.test
    def test2(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.valueSeparator0()
        option_Builder1.longOpt("")
        option0 = option_Builder0.build()
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            1, "]", option0
        )
        option1 = missingArgumentException0.getOption()
        self.assertEqual((-1), option1.getArgs())

    @pytest.mark.test
    def test1(self) -> None:

        option0 = Option.Option2("", True, "{f!)rVQ4n0'J{l6';")
        option0.setRequired(True)
        missingArgumentException0 = MissingArgumentException(1, "", option0)
        option1 = missingArgumentException0.getOption()
        self.assertIsNone(option1.getValue0())

    @pytest.mark.test
    def test0(self) -> None:

        option0 = Option.Option2("", True, "{f!)rVQ4n0'J{l6';")
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            -1, "", option0
        )
        option1 = missingArgumentException0.getOption()
        self.assertIsNone(option1)
