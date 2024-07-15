from __future__ import annotations
import time
import locale
import re
import os
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.money.format.MoneyPrintContext import *

# from src.test.org.joda.money.format.MoneyPrintContext_ESTest_scaffolding import *


class MoneyPrintContext_ESTest(unittest.TestCase):

    def test3(self) -> None:

        moneyPrintContext0 = None
        try:
            moneyPrintContext0 = MoneyPrintContext(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Locale must not be null
            MoneyFormatter.verifyException("org.joda.money.format.MoneyFormatter", e)

    def test2(self) -> None:
        locale0 = Locale.CHINA
        moneyPrintContext0 = MoneyPrintContext(locale0)
        locale1 = moneyPrintContext0.getLocale()
        self.assertEqual("zho", locale1.getISO3Language())

    def test1(self) -> None:

        locale0 = Locale.JAPANESE
        moneyPrintContext0 = MoneyPrintContext(locale0)

        with self.assertRaises(RuntimeError):
            moneyPrintContext0.setLocale(None)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.joda.money.format.MoneyFormatter", e)

    def test0(self) -> None:
        locale0 = Locale.JAPANESE
        moneyPrintContext0 = MoneyPrintContext(locale0)
        moneyPrintContext0.setLocale(locale0)
        self.assertEqual("ja", locale0.getLanguage())
