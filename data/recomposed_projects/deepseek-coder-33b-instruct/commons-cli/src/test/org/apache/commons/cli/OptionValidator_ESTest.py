from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.OptionValidator import *

# from src.main.org.apache.commons.cli.OptionValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class OptionValidator_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test8(self) -> None:

        string0 = OptionValidator.validate("?")
        self.assertEqual("?", string0)

    @pytest.mark.test
    def test7(self) -> None:
        optionValidator0 = OptionValidator()

    @pytest.mark.test
    def test6(self) -> None:

        string0 = OptionValidator.validate("j")
        self.assertEqual("j", string0)

    @pytest.mark.test
    def test5(self) -> None:

        try:
            OptionValidator.validate("=")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal option name '='
            #
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test4(self) -> None:

        string0 = OptionValidator.validate("@")
        self.assertEqual("@", string0)

    @pytest.mark.test
    def test3(self) -> None:

        string0 = OptionValidator.validate(None)
        self.assertIsNone(string0)

    @pytest.mark.test
    def test2(self) -> None:

        string0 = OptionValidator.validate("")
        self.assertEqual("", string0)

    @pytest.mark.test
    def test1(self) -> None:

        try:
            OptionValidator.validate("BwEj?")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option 'BwEj?' contains an illegal character : '?'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    @pytest.mark.test
    def test0(self) -> None:

        try:
            OptionValidator.validate("^")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal option name '^'
            #
            self.verifyException("org.apache.commons.cli.OptionValidator", e)
