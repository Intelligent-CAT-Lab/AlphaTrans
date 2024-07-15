from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.OptionValidator import *

# from src.test.org.apache.commons.cli.OptionValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class OptionValidator_ESTest(unittest.TestCase):

    def test9(self) -> None:

        try:
            OptionValidator.validate("`")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal option name '`'
            #
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test8(self) -> None:
        optionValidator0 = OptionValidator()

    def test7(self) -> None:

        string0 = OptionValidator.validate("l")
        self.assertEqual("l", string0)

    def test6(self) -> None:

        string0 = OptionValidator.validate("?")
        self.assertEqual("?", string0)

    def test5(self) -> None:

        string0 = OptionValidator.validate("@")
        self.assertEqual("@", string0)

    def test4(self) -> None:

        string0 = OptionValidator.validate(None)
        self.assertIsNone(string0)

    def test3(self) -> None:

        string0 = OptionValidator.validate("")
        self.assertEqual("", string0)

    def test2(self) -> None:

        string0 = OptionValidator.validate("xjr")
        self.assertEqual("xjr", string0)

    def test1(self) -> None:

        try:
            OptionValidator.validate('LeOX:D)K_kF.Y"V')
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # The option 'LeOX:D)K_kF.Y\"V' contains an illegal character : ':'
            self.verifyException("org.apache.commons.cli.OptionValidator", e)

    def test0(self) -> None:

        try:
            OptionValidator.validate("'")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Illegal option name '''
            #
            self.verifyException("org.apache.commons.cli.OptionValidator", e)
