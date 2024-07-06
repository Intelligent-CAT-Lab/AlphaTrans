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
        super()._tearDown()

    def _setUp(self) -> None:
        super()._setUp()

    def testConstructors(self) -> None:
        validator: CodeValidator = None
        regex: RegexValidator = RegexValidator.RegexValidator3("^[0-9]*$")

        validator = CodeValidator.CodeValidator2(
            regex, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual("Constructor 1 - regex", regex, validator.getRegexValidator())
        self.assertEqual("Constructor 1 - min length", -1, validator.getMinLength())
        self.assertEqual("Constructor 1 - max length", -1, validator.getMaxLength())
        self.assertEqual(
            "Constructor 1 - check digit",
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
        )

        validator = CodeValidator.CodeValidator1(
            regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual("Constructor 2 - regex", regex, validator.getRegexValidator())
        self.assertEqual("Constructor 2 - min length", 13, validator.getMinLength())
        self.assertEqual("Constructor 2 - max length", 13, validator.getMaxLength())
        self.assertEqual(
            "Constructor 2 - check digit",
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
        )

        validator = CodeValidator(
            0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None
        )
        self.assertEqual("Constructor 3 - regex", regex, validator.getRegexValidator())
        self.assertEqual("Constructor 3 - min length", 10, validator.getMinLength())
        self.assertEqual("Constructor 3 - max length", 20, validator.getMaxLength())
        self.assertEqual(
            "Constructor 3 - check digit",
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
        )

        validator = CodeValidator.CodeValidator5(
            "^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "Constructor 4 - regex",
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
        )
        self.assertEqual("Constructor 4 - min length", -1, validator.getMinLength())
        self.assertEqual("Constructor 4 - max length", -1, validator.getMaxLength())
        self.assertEqual(
            "Constructor 4 - check digit",
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
        )

        validator = CodeValidator.CodeValidator4(
            "^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )
        self.assertEqual(
            "Constructor 5 - regex",
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
        )
        self.assertEqual("Constructor 5 - min length", 13, validator.getMinLength())
        self.assertEqual("Constructor 5 - max length", 13, validator.getMaxLength())
        self.assertEqual(
            "Constructor 5 - check digit",
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
        )

        validator = CodeValidator(
            3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, None, 10, "^[0-9]*$"
        )
        self.assertEqual(
            "Constructor 6 - regex",
            "RegexValidator{^[0-9]*$}",
            validator.getRegexValidator().toString(),
        )
        self.assertEqual("Constructor 6 - min length", 10, validator.getMinLength())
        self.assertEqual("Constructor 6 - max length", 20, validator.getMaxLength())
        self.assertEqual(
            "Constructor 6 - check digit",
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
        )

    def testValidator294_2(self) -> None:
        validator = CodeValidator(3, None, 0, None, -1, None)
        self.assertEqual("Null", None, validator.validate(None))

    def testValidator294_1(self) -> None:
        validator = CodeValidator(3, None, -1, None, 0, None)
        self.assertEqual("Null", None, validator.validate(None))
        validator = CodeValidator(3, None, 0, None, -1, None)
        self.assertEqual("Null", None, validator.validate(None))

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

        self.assertIsNone("No Regex", validator.getRegexValidator())
        self.assertEqual("No Regex 2", value2, validator.validate(value2))
        self.assertEqual("No Regex 3", value3, validator.validate(value3))
        self.assertEqual("No Regex 4", value4, validator.validate(value4))
        self.assertEqual("No Regex 5", value5, validator.validate(value5))
        self.assertEqual("No Regex invalid", invalid, validator.validate(invalid))

        regex = "^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)
        self.assertIsNotNone("No Regex", validator.getRegexValidator())
        self.assertEqual("Regex 2", None, validator.validate(value2))
        self.assertEqual("Regex 3", value3, validator.validate(value3))
        self.assertEqual("Regex 4", value4, validator.validate(value4))
        self.assertEqual("Regex 5", None, validator.validate(value5))
        self.assertEqual("Regex invalid", None, validator.validate(invalid))

        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$"
        validator = CodeValidator.CodeValidator1(
            RegexValidator.RegexValidator3(regex), 6, None
        )
        self.assertEqual("Reformat 123-456", "123456", validator.validate("123-456"))
        self.assertEqual("Reformat 123 456", "123456", validator.validate("123 456"))
        self.assertEqual("Reformat 123456", None, validator.validate("123456"))
        self.assertEqual("Reformat 123.456", None, validator.validate("123.456"))

        regex = "^(?:([0-9]{3})(?:[-\\s])([0-9]{3}))|([0-9]{6})$"
        validator = CodeValidator.CodeValidator1(
            RegexValidator.RegexValidator3(regex), 6, None
        )
        self.assertEqual(
            "Reformat 2 Regex",
            "RegexValidator{" + regex + "}",
            validator.getRegexValidator().toString(),
        )
        self.assertEqual("Reformat 2 123-456", "123456", validator.validate("123-456"))
        self.assertEqual("Reformat 2 123 456", "123456", validator.validate("123 456"))
        self.assertEqual("Reformat 2 123456", "123456", validator.validate("123456"))

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

        self.assertIsNone("No CheckDigit", validator.getCheckDigit())
        self.assertEqual(
            "No CheckDigit invalid", invalidEAN, validator.validate(invalidEAN)
        )
        self.assertEqual("No CheckDigit valid", validEAN, validator.validate(validEAN))
        self.assertEqual(
            "No CheckDigit (is) invalid", True, validator.isValid(invalidEAN)
        )
        self.assertEqual("No CheckDigit (is) valid", True, validator.isValid(validEAN))

        validator = CodeValidator.CodeValidator4(
            None, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        self.assertIsNotNone("EAN CheckDigit", validator.getCheckDigit())
        self.assertEqual("EAN CheckDigit invalid", None, validator.validate(invalidEAN))
        self.assertEqual("EAN CheckDigit valid", validEAN, validator.validate(validEAN))
        self.assertEqual(
            "EAN CheckDigit (is) invalid", False, validator.isValid(invalidEAN)
        )
        self.assertEqual("EAN CheckDigit (is) valid", True, validator.isValid(validEAN))
        self.assertEqual("EAN CheckDigit ex", None, validator.validate("978193011099X"))

    def __init__(self, name: str) -> None:
        super().__init__(name)
