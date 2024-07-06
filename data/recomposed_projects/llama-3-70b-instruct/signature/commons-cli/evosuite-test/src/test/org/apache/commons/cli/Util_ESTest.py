from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.Util import *

# from src.test.org.apache.commons.cli.Util_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Util_ESTest(unittest.TestCase):

    def test10(self) -> None:
        util0 = Util()

    def test09(self) -> None:

        string0 = Util.stripLeadingAndTrailingQuotes("")
        self.assertEqual("", string0)

    def test08(self) -> None:

        string0 = Util.stripLeadingAndTrailingQuotes(";ELV?%J2rx*R")
        self.assertEqual(";ELV?%J2rx*R", string0)

    def test07(self) -> None:

        string0 = Util.stripLeadingAndTrailingQuotes('""--"')
        self.assertEqual('""--"', string0)

    def test06(self) -> None:

        string0 = Util.stripLeadingAndTrailingQuotes('"_R:-vkZHq')
        self.assertEqual('"_R:-vkZHq', string0)

    def test05(self) -> None:

        string0 = Util.stripLeadingAndTrailingQuotes('"--"')
        self.assertEqual(string0, "--")

    def test04(self) -> None:

        string0 = Util.stripLeadingHyphens("--")
        assert string0 is not None
        assert string0 == ""

    def test03(self) -> None:

        string0 = Util.stripLeadingHyphens(None)
        self.assertIsNone(string0)

    def test02(self) -> None:

        string0 = Util.stripLeadingHyphens("")
        self.assertEqual("", string0)

    def test01(self) -> None:

        string0 = Util.stripLeadingHyphens("-R:-vkZHq")
        self.assertEqual("R:-vkZHq", string0)

    def test00(self) -> None:

        try:
            Util.stripLeadingAndTrailingQuotes(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e.__class__), "<class 'RuntimeError'>")
