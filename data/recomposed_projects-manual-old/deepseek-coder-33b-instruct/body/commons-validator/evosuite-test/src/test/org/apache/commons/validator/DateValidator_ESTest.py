from __future__ import annotations
import time
import locale
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.DateValidator import *

# from src.test.org.apache.commons.validator.DateValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.apache.commons.validator.routines.DateValidator import *

# from src.test.org.apache.commons.validator.routines.DateValidator_ESTest_scaffolding import *


class DateValidator_ESTest(unittest.TestCase):

    def test10(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        boolean0 = dateValidator0.isValid0("2", "2", True)
        self.assertTrue(boolean0)

    def test09(self) -> None:

        date_validator0 = DateValidator()
        boolean0 = date_validator0.isValid0(None, None, True)
        self.assertFalse(boolean0)

    def test08(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        boolean0 = dateValidator0.isValid0(
            "org.apache.commons.validator.DateValidator", None, True
        )
        self.assertFalse(boolean0)

    def test07(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        boolean0 = dateValidator0.isValid0("2)8~s.7G_nqk", "", True)
        self.assertFalse(boolean0)

    def test06(self) -> None:

        dateValidator0 = DateValidator()
        boolean0 = dateValidator0.isValid0("2", "2", False)
        self.assertTrue(boolean0)

    def test05(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        boolean0 = dateValidator0.isValid0("2.$!!W$QX1X$j", "2", True)
        self.assertFalse(boolean0)

    def test04(self) -> None:

        date_validator0 = DateValidator.getInstance()
        locale0 = Locale.JAPAN
        boolean0 = date_validator0.isValid1("2.$W$QX1X$j", locale0)
        self.assertFalse(boolean0)

    def test03(self) -> None:

        date_validator0 = DateValidator()
        locale0 = Locale.CHINA
        boolean0 = date_validator0.isValid1(None, locale0)
        self.assertFalse(boolean0)

    def test02(self) -> None:

        date_validator0 = DateValidator()
        boolean0 = date_validator0.isValid1("", None)
        self.assertFalse(boolean0)

    def test01(self) -> None:

        dateValidator0 = DateValidator.getInstance()

        with pytest.raises(ValueError):
            dateValidator0.isValid0("", "{Lm_<A!--", False)
            pytest.fail("Expecting exception: ValueError")

        verifyException("java.text.SimpleDateFormat", ValueError)

    def test00(self) -> None:

        dateValidator0 = DateValidator.getInstance()
        boolean0 = dateValidator0.isValid0('YcLj?v"(b', "2", True)
        self.assertFalse(boolean0)
