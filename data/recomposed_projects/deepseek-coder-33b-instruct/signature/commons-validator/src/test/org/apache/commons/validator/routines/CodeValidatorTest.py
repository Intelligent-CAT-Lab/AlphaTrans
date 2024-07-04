from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *


class CodeValidatorTest(unittest.TestCase):

    def _tearDown(self) -> None:
        super().tearDown()

    def _setUp(self) -> None:
        super().setUp()

    def testConstructors(self) -> None:

        pass  # LLM could not translate this method

    def testValidator294_2(self) -> None:

        validator = CodeValidator(3, None, 0, None, -1, None)
        self.assertEqual("Null", None, validator.validate(None))

    def testValidator294_1(self) -> None:

        validator = CodeValidator(3, None, -1, None, 0, None)
        self.assertEqual(None, validator.validate(None))

        validator = CodeValidator(3, None, 0, None, -1, None)
        self.assertEqual(None, validator.validate(None))

    def testNoInput(self) -> None:

        validator = CodeValidator(3, None, -1, None, -1, None)
        self.assertEqual("Null", None, validator.validate(None))
        self.assertEqual("Zero Length", None, validator.validate(""))
        self.assertEqual("Spaces", None, validator.validate("   "))
        self.assertEqual("Trimmed", "A", validator.validate(" A  "))

    def testRegex(self) -> None:

        validator = CodeValidator(3, None, -1, None, -1, None)

        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator())
        self.assertEqual(validator.validate(value2), value2)
        self.assertEqual(validator.validate(value3), value3)
        self.assertEqual(validator.validate(value4), value4)
        self.assertEqual(validator.validate(value5), value5)
        self.assertEqual(validator.validate(invalid), invalid)

        regex = "^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)
        self.assertIsNotNone(validator.getRegexValidator())
        self.assertIsNone(validator.validate(value2))
        self.assertEqual(validator.validate(value3), value3)
        self.assertEqual(validator.validate(value4), value4)
        self.assertIsNone(validator.validate(value5))
        self.assertIsNone(validator.validate(invalid))

        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$"
        validator = CodeValidator.CodeValidator1(
            RegexValidator.RegexValidator3(regex), 6, None
        )
        self.assertEqual(validator.validate("123-456"), "123456")
        self.assertEqual(validator.validate("123 456"), "123456")
        self.assertIsNone(validator.validate("123456"))
        self.assertIsNone(validator.validate("123.456"))

        regex = "^(?:([0-9]{3})(?:[-\\s])([0-9]{3}))|([0-9]{6})$"
        validator = CodeValidator.CodeValidator1(
            RegexValidator.RegexValidator3(regex), 6, None
        )
        self.assertEqual(
            validator.getRegexValidator().toString(), f"RegexValidator{{{regex}}}"
        )
        self.assertEqual(validator.validate("123-456"), "123456")
        self.assertEqual(validator.validate("123 456"), "123456")
        self.assertEqual(validator.validate("123456"), "123456")
        self.assertIsNone(validator.validate("123.456"))

    def testLength(self) -> None:

        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual("No min", -1, validator.getMinLength())
        self.assertEqual("No max", -1, validator.getMaxLength())

        self.assertEqual("No Length 10", length_10, validator.validate(length_10))
        self.assertEqual("No Length 11", length_11, validator.validate(length_11))
        self.assertEqual("No Length 12", length_12, validator.validate(length_12))
        self.assertEqual("No Length 20", length_20, validator.validate(length_20))
        self.assertEqual("No Length 21", length_21, validator.validate(length_21))
        self.assertEqual("No Length 22", length_22, validator.validate(length_22))

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual("Min 11 - min", 11, validator.getMinLength())
        self.assertEqual("Min 11 - max", -1, validator.getMaxLength())
        self.assertEqual("Min 11 - 10", None, validator.validate(length_10))
        self.assertEqual("Min 11 - 11", length_11, validator.validate(length_11))
        self.assertEqual("Min 11 - 12", length_12, validator.validate(length_12))
        self.assertEqual("Min 11 - 20", length_20, validator.validate(length_20))
        self.assertEqual("Min 11 - 21", length_21, validator.validate(length_21))
        self.assertEqual("Min 11 - 22", length_22, validator.validate(length_22))

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual("Max 21 - min", -1, validator.getMinLength())
        self.assertEqual("Max 21 - max", 21, validator.getMaxLength())
        self.assertEqual("Max 21 - 10", length_10, validator.validate(length_10))
        self.assertEqual("Max 21 - 11", length_11, validator.validate(length_11))
        self.assertEqual("Max 21 - 12", length_12, validator.validate(length_12))
        self.assertEqual("Max 21 - 20", length_20, validator.validate(length_20))
        self.assertEqual("Max 21 - 21", length_21, validator.validate(length_21))
        self.assertEqual("Max 21 - 22", None, validator.validate(length_22))

        validator = CodeValidator(3, None, 21, None, 11, None)
        self.assertEqual("Min 11 / Max 21 - min", 11, validator.getMinLength())
        self.assertEqual("Min 11 / Max 21 - max", 21, validator.getMaxLength())
        self.assertEqual("Min 11 / Max 21 - 10", None, validator.validate(length_10))
        self.assertEqual(
            "Min 11 / Max 21 - 11", length_11, validator.validate(length_11)
        )
        self.assertEqual(
            "Min 11 / Max 21 - 12", length_12, validator.validate(length_12)
        )
        self.assertEqual(
            "Min 11 / Max 21 - 20", length_20, validator.validate(length_20)
        )
        self.assertEqual(
            "Min 11 / Max 21 - 21", length_21, validator.validate(length_21)
        )
        self.assertEqual("Min 11 / Max 21 - 22", None, validator.validate(length_22))

        validator = CodeValidator(3, None, 11, None, 11, None)
        self.assertEqual("Exact 11 - min", 11, validator.getMinLength())
        self.assertEqual("Exact 11 - max", 11, validator.getMaxLength())
        self.assertEqual("Exact 11 - 10", None, validator.validate(length_10))
        self.assertEqual("Exact 11 - 11", length_11, validator.validate(length_11))
        self.assertEqual("Exact 11 - 12", None, validator.validate(length_12))

    def testCheckDigit(self) -> None:

        validator = CodeValidator(3, None, -1, None, -1, None)
        invalidEAN = "9781930110992"
        validEAN = "9781930110991"

        self.assertIsNone(validator.getCheckDigit(), "No CheckDigit")
        self.assertEqual(
            validator.validate(invalidEAN), invalidEAN, "No CheckDigit invalid"
        )
        self.assertEqual(validator.validate(validEAN), validEAN, "No CheckDigit valid")
        self.assertTrue(validator.isValid(invalidEAN), "No CheckDigit (is) invalid")
        self.assertTrue(validator.isValid(validEAN), "No CheckDigit (is) valid")

        validator = CodeValidator.CodeValidator4(
            None, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        self.assertIsNotNone(validator.getCheckDigit(), "EAN CheckDigit")
        self.assertIsNone(validator.validate(invalidEAN), "EAN CheckDigit invalid")
        self.assertEqual(validator.validate(validEAN), validEAN, "EAN CheckDigit valid")
        self.assertFalse(validator.isValid(invalidEAN), "EAN CheckDigit (is) invalid")
        self.assertTrue(validator.isValid(validEAN), "EAN CheckDigit (is) valid")
        self.assertIsNone(validator.validate("978193011099X"), "EAN CheckDigit ex")

    def __init__(self, name: str) -> None:
        super().__init__(name)
