from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.Util import *

# from src.main.org.apache.commons.cli.Util_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Util_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test10(self) -> None:
        util0 = Util()

    @pytest.mark.test
    def test09(self) -> None:

        string0 = Util.stripLeadingAndTrailingQuotes("")
        self.assertEqual("", string0)

    @pytest.mark.test
    def test08(self) -> None:

        string0 = Util.stripLeadingAndTrailingQuotes("x,")
        self.assertEqual("x,", string0)

    @pytest.mark.test
    def test07(self) -> None:

        string0 = Util.stripLeadingAndTrailingQuotes('"e1;BsQpF""')
        self.assertEqual('"e1;BsQpF""', string0)

    @pytest.mark.test
    def test06(self) -> None:

        string0 = Util.stripLeadingAndTrailingQuotes('"e1;BsQpF')
        self.assertEqual('"e1;BsQpF', string0)

    @pytest.mark.test
    def test05(self) -> None:

        string0 = Util.stripLeadingAndTrailingQuotes('"e1;BsQpF"')
        self.assertEqual(string0, "e1;BsQpF")

    @pytest.mark.test
    def test04(self) -> None:

        string0 = Util.stripLeadingHyphens('"e1;BsQpF"')
        self.assertEqual('"e1;BsQpF"', string0)
        self.assertIsNotNone(string0)

    @pytest.mark.test
    def test03(self) -> None:

        string0 = Util.stripLeadingHyphens(None)
        self.assertIsNone(string0)

    @pytest.mark.test
    def test02(self) -> None:

        string0 = Util.stripLeadingHyphens("--")
        self.assertEqual(string0, "")

    @pytest.mark.test
    def test01(self) -> None:

        string0 = Util.stripLeadingHyphens("-")
        self.assertEqual(string0, "")

    @pytest.mark.test
    def test00(self) -> None:

        try:
            Util.stripLeadingAndTrailingQuotes(None)
            self.fail("Expecting exception: NullPointerException")

        except Exception as e:
            self.assertIsInstance(e, NullPointerException)
            self.assertIsNone(e.getMessage())
            self.verifyException("org.apache.commons.cli.Util", e)
