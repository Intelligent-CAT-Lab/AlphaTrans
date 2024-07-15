from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.MissingArgumentException import *

# from src.test.org.apache.commons.cli.MissingArgumentException_ESTest_scaffolding import *
from src.main.org.apache.commons.cli.Option import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class MissingArgumentException_ESTest(unittest.TestCase):

    def test9(self) -> None:

        option0 = Option.Option2("", True, "")
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            1, None, option0
        )
        option1 = missingArgumentException0.getOption()
        self.assertEqual("\u0000", option1.getValueSeparator())

    def test8(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.longOpt("org.apache.commons.cli.Option")
        option0 = option_Builder0.build()
        missingArgumentException0 = MissingArgumentException(
            (-925), "org.apache.commons.cli.Option", option0
        )
        option1 = missingArgumentException0.getOption()
        self.assertIsNone(option1)

    def test7(self) -> None:

        option0 = Option.Option1("NO_ARGS_ALLOWED", "NO_ARGS_ALLOWED")
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            -1, "NO_ARGS_ALLOWED", option0
        )
        assert missingArgumentException0 is not None

    def test6(self) -> None:

        # Undeclared exception
        try:
            MissingArgumentException.MissingArgumentException1(1, "~m=A%.&|J:F", None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.apache.commons.cli.MissingArgumentException", e)

    def test5(self) -> None:

        option0 = Option.Option1("m", "m")
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            1, "j=XDFq^zS*0=F1j[9f", option0
        )
        option0.setArgs(0)
        option1 = missingArgumentException0.getOption()
        assert not option1.hasArgName()

    def test4(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.argName("org.apache.commons.cli.Option")
        option_Builder0.longOpt("org.apache.commons.cli.Option")
        option0 = option_Builder0.build()
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            1, "org.apache.commons.cli.Option", option0
        )
        option1 = missingArgumentException0.getOption()
        assert option1.hasLongOpt()

    def test3(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder0.hasArgs()
        option_Builder0.longOpt("org.apache.commons.cli.Option")
        option0 = option_Builder0.build()
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            1, "org.apache.commons.cli.Option", option0
        )
        option1 = missingArgumentException0.getOption()
        assert option1.hasLongOpt()

    def test2(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.optionalArg(True)
        option0 = Option(
            1, '&JF"<BZ%HI~TN,M', '&JF"<BZ%HI~TN,M', "", True, option_Builder1
        )
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            1, '&JF"<BZ%HI~TN,M', option0
        )
        option1 = missingArgumentException0.getOption()
        assert not option1.hasLongOpt()

    def test1(self) -> None:

        option0 = Option.Option1("m", "m")
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            1, "j=XDFq^zS*0=F1j[9f", option0
        )
        option0.setValueSeparator('"')
        option1 = missingArgumentException0.getOption()
        assert not option1.hasOptionalArg()

    def test0(self) -> None:

        option_Builder0 = Option.builder0()
        option_Builder1 = option_Builder0.required0()
        option_Builder0.longOpt("org.apache.commons.cli.Option")
        option0 = option_Builder1.build()
        missingArgumentException0 = MissingArgumentException.MissingArgumentException1(
            1, "org.apache.commons.cli.Option", option0
        )
        option1 = missingArgumentException0.getOption()
        self.assertEqual(Option.UNLIMITED_VALUES, -2)
