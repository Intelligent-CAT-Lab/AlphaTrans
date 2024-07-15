from __future__ import annotations
import time
import re
import mock
import os
import numbers
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.CreditCardValidator import *

# from src.test.org.apache.commons.validator.CreditCardValidator_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.CreditCardValidator import *

# from src.test.org.apache.commons.validator.routines.CreditCardValidator_ESTest_scaffolding import *
from src.main.org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit import *


class CreditCardValidator_ESTest(unittest.TestCase):

    def test30(self) -> None:

        creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2()
        boolean0 = creditCardValidator0.isValid(None)
        self.assertFalse(boolean0)

    def test29(self) -> None:

        creditCardValidator0 = CreditCardValidator.CreditCardValidator0()
        object0 = creditCardValidator0.validate("")
        self.assertIsNone(object0)

    def test28(self) -> None:
        creditCardValidator0 = CreditCardValidator.genericCreditCardValidator1(172)
        self.assertEqual(4, CreditCardValidator.MASTERCARD)

    def test27(self) -> None:

        creditCardValidator_CreditCardRangeArray0 = []
        codeValidatorArray0 = [None] * 19
        creditCardValidator0 = CreditCardValidator(
            0, 0, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0
        )
        self.assertEqual(64, CreditCardValidator.MASTERCARD_PRE_OCT2016)

    def test26(self) -> None:

        creditCardValidator_CreditCardRangeArray0 = [CreditCardRange()]
        codeValidatorArray0 = []
        creditCardValidator0 = CreditCardValidator(
            0, (-2), creditCardValidator_CreditCardRangeArray0, codeValidatorArray0
        )
        self.assertEqual(64, CreditCardValidator.MASTERCARD_PRE_OCT2016)

    def test25(self) -> None:

        creditCardValidator0 = None
        try:
            creditCardValidator0 = CreditCardValidator(1, 16, None, None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Card validators are missing
            self.assertEqual(str(e), "Card validators are missing")

    def test24(self) -> None:

        creditCardValidator_CreditCardRangeArray0 = [None] * 3
        codeValidatorArray0 = [None] * 5
        creditCardValidator0 = CreditCardValidator(
            2, 0, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0
        )
        self.assertEqual(8, CreditCardValidator.DISCOVER)

    def test23(self) -> None:

        creditCardValidator0 = None
        try:
            creditCardValidator0 = CreditCardValidator(2, 2, None, None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            # Card ranges are missing
            self.assertEqual(str(e), "Card ranges are missing")

    def test22(self) -> None:

        creditCardValidator_CreditCardRangeArray0 = []
        codeValidatorArray0 = [None]
        creditCardValidator0 = CreditCardValidator(
            -3703, -3703, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0
        )
        self.assertEqual(16, CreditCardValidator.DINERS)

    def test21(self) -> None:

        creditCardValidator_CreditCardRangeArray0 = [None] * 6
        creditCardValidator0 = None
        try:
            creditCardValidator0 = CreditCardValidator(
                3, -2215, creditCardValidator_CreditCardRangeArray0, None
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Card validators are missing
            #
            self.verifyException(
                "org.apache.commons.validator.routines.CreditCardValidator", e
            )

    def test20(self) -> None:

        code_validator_array0 = [None] * 8
        credit_card_validator0 = None
        try:
            credit_card_validator0 = CreditCardValidator(
                3, 525, None, code_validator_array0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # Card ranges are missing
            #
            self.verifyException(
                "org.apache.commons.validator.routines.CreditCardValidator", e
            )

    def test19(self) -> None:

        creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2()
        boolean0 = creditCardValidator0.isValid("TMKe/T5OKYI")
        self.assertFalse(boolean0)

    def test18(self) -> None:

        creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2()
        boolean0 = creditCardValidator0.isValid("")
        self.assertFalse(boolean0)

    def test17(self) -> None:

        creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2()
        object0 = creditCardValidator0.validate(None)
        self.assertIsNone(object0)

    def test16(self) -> None:

        creditCardValidator_CreditCardRange0 = CreditCardRange(
            0, "", "", 0, (-12), None
        )
        boolean0 = CreditCardValidator.validLength(
            0, creditCardValidator_CreditCardRange0
        )
        self.assertFalse(boolean0)

    def test15(self) -> None:

        creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2()
        creditCardValidator_CreditCardRangeArray0 = [None] * 2
        intArray0 = [0] * 9
        creditCardValidator_CreditCardRange0 = CreditCardValidator.CreditCardRange(
            1,
            "org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit",
            "org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit",
            3,
            (-67),
            intArray0,
        )
        creditCardValidator_CreditCardRangeArray0[0] = (
            creditCardValidator_CreditCardRange0
        )
        codeValidatorArray0 = [None] * 7
        codeValidatorArray0[0] = creditCardValidator0.VPAY_VALIDATOR
        codeValidatorArray0[1] = creditCardValidator0.MASTERCARD_VALIDATOR
        codeValidatorArray0[2] = creditCardValidator0.MASTERCARD_VALIDATOR
        codeValidatorArray0[3] = creditCardValidator0.VISA_VALIDATOR
        codeValidatorArray0[4] = creditCardValidator0.DISCOVER_VALIDATOR
        codeValidatorArray0[5] = creditCardValidator0.VPAY_VALIDATOR
        codeValidatorArray0[6] = creditCardValidator0.VPAY_VALIDATOR
        creditCardValidator1 = CreditCardValidator(
            3, 882, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0
        )

        try:
            creditCardValidator1.validate("00")
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException(
                "org.apache.commons.validator.routines.CreditCardValidator", e
            )

    def test14(self) -> None:

        intArray0 = [94]
        creditCardValidator_CreditCardRange0 = CreditCardRange(
            94, "X", "X", 94, 94, intArray0
        )
        boolean0 = CreditCardValidator.validLength(
            94, creditCardValidator_CreditCardRange0
        )
        self.assertTrue(boolean0)

    def test13(self) -> None:

        intArray0 = [0]
        creditCardValidator_CreditCardRange0 = CreditCardRange(
            0, "p-rKBj@6Z`lHn0P", "ylYy:@R:Vx5pMc", 625, 625, intArray0
        )
        boolean0 = CreditCardValidator.validLength(
            0, creditCardValidator_CreditCardRange0
        )
        self.assertFalse(boolean0)

    def test12(self) -> None:

        intArray0 = [0]
        creditCardValidator_CreditCardRange0 = CreditCardRange(
            0, "", "l'EI", 0, 0, intArray0
        )
        boolean0 = CreditCardValidator.validLength(
            0, creditCardValidator_CreditCardRange0
        )
        self.assertTrue(boolean0)

    def test11(self) -> None:

        creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2()
        creditCardValidator_CreditCardRangeArray0 = [None] * 2
        codeValidatorArray0 = [None] * 7
        codeValidatorArray0[0] = creditCardValidator0.VPAY_VALIDATOR
        codeValidatorArray0[1] = creditCardValidator0.MASTERCARD_VALIDATOR
        codeValidatorArray0[2] = creditCardValidator0.MASTERCARD_VALIDATOR
        codeValidatorArray0[3] = creditCardValidator0.VISA_VALIDATOR
        codeValidatorArray0[4] = creditCardValidator0.DISCOVER_VALIDATOR
        codeValidatorArray0[5] = creditCardValidator0.VPAY_VALIDATOR
        codeValidatorArray0[6] = creditCardValidator0.DISCOVER_VALIDATOR
        creditCardValidator1 = CreditCardValidator(
            3, 882, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0
        )
        object0 = creditCardValidator1.validate(
            "org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit"
        )
        self.assertIsNone(object0)

    def test10(self) -> None:

        creditCardValidator0 = CreditCardValidator.genericCreditCardValidator2()
        creditCardValidator_CreditCardRangeArray0 = [None] * 2
        intArray0 = [0] * 9
        creditCardValidator_CreditCardRange0 = CreditCardValidator.CreditCardRange(
            1,
            "org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit",
            "org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit",
            3,
            (-67),
            intArray0,
        )
        creditCardValidator_CreditCardRangeArray0[0] = (
            creditCardValidator_CreditCardRange0
        )
        creditCardValidator_CreditCardRangeArray0[1] = (
            creditCardValidator_CreditCardRange0
        )
        codeValidatorArray0 = [None] * 7
        codeValidatorArray0[0] = creditCardValidator0.VPAY_VALIDATOR
        codeValidatorArray0[1] = creditCardValidator0.MASTERCARD_VALIDATOR
        codeValidatorArray0[2] = creditCardValidator0.MASTERCARD_VALIDATOR
        codeValidatorArray0[3] = creditCardValidator0.VISA_VALIDATOR
        codeValidatorArray0[4] = creditCardValidator0.DISCOVER_VALIDATOR
        codeValidatorArray0[5] = creditCardValidator0.VPAY_VALIDATOR
        codeValidatorArray0[6] = creditCardValidator0.MASTERCARD_VALIDATOR
        creditCardValidator1 = CreditCardValidator(
            3, 882, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0
        )
        object0 = creditCardValidator1.validate("00")
        self.assertIsNone(object0)

    def test09(self) -> None:

        creditCardValidator0 = CreditCardValidator.genericCreditCardValidator0(0, -2444)
        self.assertEqual(16, CreditCardValidator.DINERS)

    def test08(self) -> None:

        creditCardValidator_CreditCardRangeArray0 = [None] * 3
        codeValidatorArray0 = [None] * 6
        creditCardValidator0 = CreditCardValidator(
            0, (-2309), creditCardValidator_CreditCardRangeArray0, codeValidatorArray0
        )
        self.assertEqual(8, CreditCardValidator.DISCOVER)

    def test07(self) -> None:

        creditCardValidator_CreditCardRangeArray0 = [None] * 6
        codeValidatorArray0 = [None] * 5
        creditCardValidator0 = CreditCardValidator(
            1, (-1475), creditCardValidator_CreditCardRangeArray0, codeValidatorArray0
        )
        self.assertEqual(0, CreditCardValidator.NONE)

    def test06(self) -> None:

        eAN13CheckDigit0 = ISBNCheckDigit.ISBN13_CHECK_DIGIT

        with pytest.raises(RuntimeError):
            CreditCardValidator.createRangeValidator(None, eAN13CheckDigit0)
            pytest.fail("Expecting exception: RuntimeError")

    def test05(self) -> None:

        creditCardValidator_CreditCardRangeArray0 = [
            CreditCardValidator.CreditCardRange()
        ]
        codeValidatorArray0 = []
        creditCardValidator0 = CreditCardValidator(
            3, 3, creditCardValidator_CreditCardRangeArray0, codeValidatorArray0
        )

        try:
            creditCardValidator0.isValid("00")
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.validator.routines.CreditCardValidator", e
            )

    def test04(self) -> None:

        try:
            CreditCardValidator.validLength(3378, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "RuntimeError")

    def test03(self) -> None:

        pass  # LLM could not translate this method

    def test02(self) -> None:

        intArray0 = [1]
        creditCardValidator_CreditCardRange0 = CreditCardRange(
            -9, ",G@vYXW9.EgVRF|", ",G@vYXW9.EgVRF|", -9, -9, intArray0
        )
        boolean0 = CreditCardValidator.validLength(
            -9, creditCardValidator_CreditCardRange0
        )
        self.assertFalse(boolean0)

    def test01(self) -> None:

        intArray0 = [0] * 3
        creditCardValidator_CreditCardRange0 = CreditCardRange(
            973, "Q)]4V'!/+", "#c,wp2_8D#1g", 0, (-2444), intArray0
        )

    def test00(self) -> None:

        intArray0 = [1]
        creditCardValidator_CreditCardRange0 = CreditCardRange(
            0, "", "", 0, 19, intArray0
        )
        boolean0 = CreditCardValidator.validLength(
            3, creditCardValidator_CreditCardRange0
        )
        self.assertTrue(boolean0)
