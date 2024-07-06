from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.IBANValidator import *

# from src.test.org.apache.commons.validator.routines.IBANValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class IBANValidator_ESTest(unittest.TestCase):

    def test27(self) -> None:

        iBANValidator0 = IBANValidator.getInstance()
        boolean0 = iBANValidator0.hasValidator("vkMR>/ua7t7x")
        self.assertFalse(boolean0)

    def test26(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()
        iBANValidator_ValidatorArray0 = (
            iBANValidator0.DEFAULT_IBAN_VALIDATOR.getDefaultValidators()
        )
        self.assertEqual(77, len(iBANValidator_ValidatorArray0))

    def test25(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()
        iBANValidator_Validator0 = iBANValidator0.setValidator1("DO", 34, "DO")
        self.assertIsNotNone(iBANValidator_Validator0)

    def test24(self) -> None:

        iban_validator_validator0 = None
        try:
            iban_validator_validator0 = Validator("pk", 27, "pk")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid country Code; must be exactly 2 upper-case characters
            self.assertEqual(
                str(e), "Invalid country Code; must be exactly 2 upper-case characters"
            )

    def test23(self) -> None:

        iban_validator_validator0 = None
        try:
            iban_validator_validator0 = Validator("S1", 27, "S1")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid country Code; must be exactly 2 upper-case characters
            self.assertEqual(
                str(e), "Invalid country Code; must be exactly 2 upper-case characters"
            )

    def test22(self) -> None:

        iban_validator_validator0 = None
        try:
            iban_validator_validator0 = Validator("UA", 2978, "UA")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid length parameter, must be in range 8 to 34 inclusive: 2978
            self.assertTrue(
                "Invalid length parameter, must be in range 8 to 34 inclusive: 2978"
                in str(e)
            )

    def test21(self) -> None:

        iban_validator_validator0 = None
        try:
            iban_validator_validator0 = Validator("SI", -8, "SI")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid length parameter, must be in range 8 to 34 inclusive: -8
            self.assertTrue(
                "Invalid length parameter, must be in range 8 to 34 inclusive: -8"
                in str(e)
            )

    def test20(self) -> None:

        iban_validator_validator0 = None
        try:
            iban_validator_validator0 = Validator("RO", 9, "K'A<{ITI")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # countryCode 'RO' does not agree with format: K'A<{ITI
            self.assertTrue(
                "countryCode 'RO' does not agree with format: K'A<{ITI" in str(e)
            )

    def test19(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()
        boolean0 = iBANValidator0.isValid("QAQAd{2}[A-Z]{4}[A-Z0-9]{21}")
        self.assertFalse(boolean0)

    def test18(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()
        boolean0 = iBANValidator0.hasValidator("QAQAd{2}[A-Z]{4}[A-Z0-9]{21}")
        self.assertTrue(boolean0)

    def test17(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()
        iBANValidator_Validator0 = iBANValidator0.getValidator(None)
        self.assertIsNone(iBANValidator_Validator0)

    def test16(self) -> None:

        iBANValidator0 = IBANValidator.getInstance()
        boolean0 = iBANValidator0.isValid("}")
        self.assertFalse(boolean0)

    def test15(self) -> None:

        iBANValidator0 = IBANValidator.DEFAULT_IBAN_VALIDATOR

        with self.assertRaises(RuntimeError):
            iBANValidator0.setValidator0(None)

        self.verifyException(
            "org.apache.commons.validator.routines.IBANValidator",
            RuntimeError("The singleton validator cannot be modified"),
        )

    def test14(self) -> None:

        iBANValidator0 = IBANValidator.getInstance()

        try:
            iBANValidator0.setValidator1("RegexValidator{", (-910), "$%")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException(
                "org.apache.commons.validator.routines.IBANValidator", e
            )

    def test13(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()
        iBANValidator_Validator0 = iBANValidator0.setValidator1(
            "IEIEd{2}[A-Z]{4}d{14}", (-1), "IEIEd{2}[A-Z]{4}d{14}"
        )
        self.assertIsNone(iBANValidator_Validator0)

    def test12(self) -> None:

        iban_validator_validator_array0 = [None] * 1
        iban_validator0 = None
        try:
            iban_validator0 = IBANValidator(iban_validator_validator_array0)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.validator.routines.IBANValidator", e
            )

    def test11(self) -> None:

        iBANValidator0 = IBANValidator.getInstance()
        iBANValidator_Validator0 = iBANValidator0.getValidator("$%")
        self.assertIsNone(iBANValidator_Validator0)

    def test10(self) -> None:

        iBANValidator0 = IBANValidator.DEFAULT_IBAN_VALIDATOR
        iBANValidator_Validator0 = iBANValidator0.getValidator("z")
        self.assertIsNone(iBANValidator_Validator0)

    def test09(self) -> None:

        iban_validator0 = IBANValidator.IBANValidator1()

        try:
            iban_validator0.setValidator0(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.validator.routines.IBANValidator", e)

    def test08(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()

        with pytest.raises(RuntimeError):
            iBANValidator0.setValidator1(None, -4212, None)
            self.fail("Expecting exception: RuntimeError")

    def test07(self) -> None:

        iBANValidator0 = IBANValidator.DEFAULT_IBAN_VALIDATOR
        iBANValidator_Validator0 = iBANValidator0.getValidator(
            "SCSCd{2}[A-Z]{4}d{20}[A-Z]{3}"
        )
        iBANValidator_ValidatorArray0 = [None] * 1
        iBANValidator_ValidatorArray0[0] = iBANValidator_Validator0
        iBANValidator1 = IBANValidator(iBANValidator_ValidatorArray0)
        self.assertFalse(iBANValidator1 == iBANValidator0)

    def test06(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()
        iBANValidator_Validator0 = iBANValidator0.setValidator1("FO", (-1), "FO")
        iBANValidator0.setValidator0(iBANValidator_Validator0)
        iBANValidator_Validator1 = iBANValidator0.setValidator0(
            iBANValidator_Validator0
        )
        self.assertIs(iBANValidator_Validator1, iBANValidator_Validator0)

    def test05(self) -> None:

        iban_validator_validator0 = None
        try:
            iban_validator_validator0 = Validator("0", 250, "0")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Invalid country Code; must be exactly 2 upper-case characters
            self.assertEqual(
                str(e), "Invalid country Code; must be exactly 2 upper-case characters"
            )

    def test04(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()

        try:
            iBANValidator0.setValidator1("FO", 8, "DO")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException(
                "org.apache.commons.validator.routines.IBANValidator$Validator", e
            )

    def test03(self) -> None:

        iBANValidator_Validator0 = Validator("FO", 9, "FOFO")

    def test02(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()
        boolean0 = iBANValidator0.isValid("LVd{2}[A-Z]{4}[A-Z0-9]{13}")
        self.assertFalse(boolean0)

    def test01(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()

        try:
            iBANValidator0.setValidator1("h4t", 0, "h4t")
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException(
                "org.apache.commons.validator.routines.IBANValidator$Validator", e
            )

    def test00(self) -> None:

        iBANValidator0 = IBANValidator.IBANValidator1()
        iBANValidator_Validator0 = iBANValidator0.setValidator1(
            "BH", -1023, "HI='TR+yTK$E"
        )
        self.assertIsNotNone(iBANValidator_Validator0)
