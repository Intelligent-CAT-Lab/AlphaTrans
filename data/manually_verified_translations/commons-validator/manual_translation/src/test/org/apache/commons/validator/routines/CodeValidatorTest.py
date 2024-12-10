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

    def tearDown(self) -> None:
        super().tearDown()

    def setUp(self) -> None:
        super().setUp()

    def testConstructors(self) -> None:

        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")

        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit"
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit"
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit"
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 4 - regex"
        )
        self.assertEqual(-1, validator.getMinLength(), "Constructor 4 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 4 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 4 - check digit"
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 5 - regex"
        )
        self.assertEqual(13, validator.getMinLength(), "Constructor 5 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 5 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 5 - check digit"
        )

        validator = CodeValidator(
            3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, None, 10, "^[0-9]*$"
        )
        self.assertEqual(
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
            "Constructor 6 - regex"
        )
        self.assertEqual(10, validator.getMinLength(), "Constructor 6 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 6 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 6 - check digit"
        )

    def testValidator294_2(self) -> None:

        validator = CodeValidator(3, None, 0, None, -1, None)
        self.assertEqual(None, validator.validate(None))

    def testValidator294_1(self) -> None:

        validator = CodeValidator(3, None, -1, None, 0, None)
        self.assertEqual(None, validator.validate(None))

        validator = CodeValidator(3, None, 0, None, -1, None)
        self.assertEqual(None, validator.validate(None))

    def testNoInput(self) -> None:

        validator = CodeValidator(3, None, -1, None, -1, None)

        self.assertEqual(validator.validate(None), None)
        self.assertEqual(validator.validate(""), None)
        self.assertEqual(validator.validate("   "), None)
        self.assertEqual(validator.validate(" A  "), "A")

    def testRegex(self) -> None:

        validator = CodeValidator(3, None, -1, None, -1, None)

        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator())
        self.assertEqual(value2, validator.validate(value2))
        self.assertEqual(value3, validator.validate(value3))
        self.assertEqual(value4, validator.validate(value4))
        self.assertEqual(value5, validator.validate(value5))
        self.assertEqual(invalid, validator.validate(invalid))

        regex = "^([0-9]{3,4})$"
        validator = CodeValidator(
            3, None, -1, RegexValidator.RegexValidator3(regex), -1, regex
        )
        self.assertIsNotNone(validator.getRegexValidator())
        self.assertIsNone(validator.validate(value2))
        self.assertEqual(value3, validator.validate(value3))
        self.assertEqual(value4, validator.validate(value4))
        self.assertIsNone(validator.validate(value5))
        self.assertIsNone(validator.validate(invalid))

        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$"
        validator = CodeValidator.CodeValidator1(
            RegexValidator.RegexValidator3(regex), 6, None
        )
        self.assertEqual("123456", validator.validate("123-456"))
        self.assertEqual("123456", validator.validate("123 456"))
        self.assertIsNone(validator.validate("123456"))
        self.assertIsNone(validator.validate("123.456"))

        regex = "^(?:([0-9]{3})(?:[-\\s])([0-9]{3}))|([0-9]{6})$"
        validator = CodeValidator.CodeValidator1(
            RegexValidator.RegexValidator3(regex), 6, None
        )
        self.assertEqual(
            "RegexValidator{" + regex + "}", validator.getRegexValidator().toString()
        )
        self.assertEqual("123456", validator.validate("123-456"))
        self.assertEqual("123456", validator.validate("123 456"))
        self.assertEqual("123456", validator.validate("123456"))

    def testLength(self) -> None:

        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength())
        self.assertEqual(-1, validator.getMaxLength())

        self.assertEqual(length_10, validator.validate(length_10))
        self.assertEqual(length_11, validator.validate(length_11))
        self.assertEqual(length_12, validator.validate(length_12))
        self.assertEqual(length_20, validator.validate(length_20))
        self.assertEqual(length_21, validator.validate(length_21))
        self.assertEqual(length_22, validator.validate(length_22))

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength())
        self.assertEqual(-1, validator.getMaxLength())
        self.assertEqual(None, validator.validate(length_10))
        self.assertEqual(length_11, validator.validate(length_11))
        self.assertEqual(length_12, validator.validate(length_12))
        self.assertEqual(length_20, validator.validate(length_20))
        self.assertEqual(length_21, validator.validate(length_21))
        self.assertEqual(length_22, validator.validate(length_22))

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength())
        self.assertEqual(21, validator.getMaxLength())
        self.assertEqual(length_10, validator.validate(length_10))
        self.assertEqual(length_11, validator.validate(length_11))
        self.assertEqual(length_12, validator.validate(length_12))
        self.assertEqual(length_20, validator.validate(length_20))
        self.assertEqual(length_21, validator.validate(length_21))
        self.assertEqual(None, validator.validate(length_22))

        validator = CodeValidator(3, None, 21, None, 11, None)
        self.assertEqual(11, validator.getMinLength())
        self.assertEqual(21, validator.getMaxLength())
        self.assertEqual(None, validator.validate(length_10))
        self.assertEqual(length_11, validator.validate(length_11))
        self.assertEqual(length_12, validator.validate(length_12))
        self.assertEqual(length_20, validator.validate(length_20))
        self.assertEqual(length_21, validator.validate(length_21))
        self.assertEqual(None, validator.validate(length_22))

        validator = CodeValidator(3, None, 11, None, 11, None)
        self.assertEqual(11, validator.getMinLength())
        self.assertEqual(11, validator.getMaxLength())
        self.assertEqual(None, validator.validate(length_10))
        self.assertEqual(length_11, validator.validate(length_11))
        self.assertEqual(None, validator.validate(length_12))

    def testCheckDigit(self) -> None:

        validator = CodeValidator(3, None, -1, None, -1, None)
        invalidEAN = "9781930110992"
        validEAN = "9781930110991"

        self.assertIsNone(validator.getCheckDigit(), "No CheckDigit")
        self.assertEqual(
            invalidEAN, validator.validate(invalidEAN), "No CheckDigit invalid"
        )
        self.assertEqual(validEAN, validator.validate(validEAN), "No CheckDigit valid")
        self.assertTrue(validator.isValid(invalidEAN), "No CheckDigit (is) invalid")
        self.assertTrue(validator.isValid(validEAN), "No CheckDigit (is) valid")

        validator = CodeValidator.CodeValidator4(
            None, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        self.assertIsNotNone(validator.getCheckDigit(), "EAN CheckDigit")
        self.assertIsNone(validator.validate(invalidEAN), "EAN CheckDigit invalid")
        self.assertEqual(validEAN, validator.validate(validEAN), "EAN CheckDigit valid")
        self.assertFalse(validator.isValid(invalidEAN), "EAN CheckDigit (is) invalid")
        self.assertTrue(validator.isValid(validEAN), "EAN CheckDigit (is) valid")
        self.assertIsNone(validator.validate("978193011099X"), "EAN CheckDigit ex")

    def __init__(self, name: str) -> None:
        super().__init__(name)
