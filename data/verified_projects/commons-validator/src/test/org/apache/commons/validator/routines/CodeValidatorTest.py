import pytest

from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
import unittest

class CodeValidatorTest(unittest.TestCase):

    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        try:
            super().setUp()
        except Exception as e:
            self.fail(f"An exception occurred when setting up the test: {e}")

    
    def tearDown(self) -> None:
        try:
            super().tearDown()
        except Exception as e:
            self.fail(f"An exception occurred when tearing down the test: {e}")

    
    @pytest.mark.test
    def testCheckDigit(self) -> None:
        validator = CodeValidator(3, None, -1, None, -1, None)
        invalidEAN = "9781930110992"
        validEAN = "9781930110991"

        self.assertIsNone(validator.getCheckDigit(), "No CheckDigit")
        self.assertEqual(invalidEAN, validator.validate(invalidEAN), "No CheckDigit invalid")
        self.assertEqual(validEAN, validator.validate(validEAN), "No CheckDigit valid")
        self.assertTrue(validator.isValid(invalidEAN), "No CheckDigit (is) invalid")
        self.assertTrue(validator.isValid(validEAN), "No CheckDigit (is) valid")

        validator = CodeValidator\
            .CodeValidator4(None, -1, EAN13CheckDigit.EAN13_CHECK_DIGIT)

        self.assertIsNotNone(validator.getCheckDigit(), "EAN CheckDigit")
        self.assertIsNone(validator.validate(invalidEAN), "EAN CheckDigit invalid")
        self.assertEqual(validEAN, validator.validate(validEAN), "EAN CheckDigit valid")
        self.assertFalse(validator.isValid(invalidEAN), "EAN CheckDigit (is) invalid")
        self.assertTrue(validator.isValid(validEAN), "EAN CheckDigit (is) valid")
        self.assertIsNone(validator.validate("978193011099X"), "EAN CheckDigit ex")

    
    @pytest.mark.test
    def testLength(self):
        validator = CodeValidator(3, None, -1, None, -1, None)
        length_10 = "1234567890"
        length_11 = "12345678901"
        length_12 = "123456789012"
        length_20 = "12345678901234567890"
        length_21 = "123456789012345678901"
        length_22 = "1234567890123456789012"

        self.assertEqual(-1, validator.getMinLength(), "No min")
        self.assertEqual(-1, validator.getMaxLength(), "No max")

        self.assertEqual(length_10, validator.validate(length_10), "No Length 10")
        self.assertEqual(length_11, validator.validate(length_11), "No Length 11")
        self.assertEqual(length_12, validator.validate(length_12), "No Length 12")
        self.assertEqual(length_20, validator.validate(length_20), "No Length 20")
        self.assertEqual(length_21, validator.validate(length_21), "No Length 21")
        self.assertEqual(length_22, validator.validate(length_22), "No Length 22")

        validator = CodeValidator(3, None, -1, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 - min")
        self.assertEqual(-1, validator.getMaxLength(), "Min 11 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 - 21")
        self.assertEqual(length_22, validator.validate(length_22), "Min 11 - 22")

        validator = CodeValidator(3, None, 21, None, -1, None)
        self.assertEqual(-1, validator.getMinLength(), "Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Max 21 - max")
        self.assertEqual(length_10, validator.validate(length_10), "Max 21 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Max 21 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Max 21 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Max 21 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Max 21 - 21")
        self.assertIsNone(validator.validate(length_22), "Max 21 - 22")

        validator = CodeValidator(3, None, 21, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Min 11 / Max 21 - min")
        self.assertEqual(21, validator.getMaxLength(), "Min 11 / Max 21 - max")
        self.assertIsNone(validator.validate(length_10), "Min 11 / Max 21 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Min 11 / Max 21 - 11")
        self.assertEqual(length_12, validator.validate(length_12), "Min 11 / Max 21 - 12")
        self.assertEqual(length_20, validator.validate(length_20), "Min 11 / Max 21 - 20")
        self.assertEqual(length_21, validator.validate(length_21), "Min 11 / Max 21 - 21")
        self.assertIsNone(validator.validate(length_22), "Min 11 / Max 21 - 22")

        validator = CodeValidator(3, None, 11, None, 11, None)
        self.assertEqual(11, validator.getMinLength(), "Exact 11 - min")
        self.assertEqual(11, validator.getMaxLength(), "Exact 11 - max")
        self.assertIsNone(validator.validate(length_10), "Exact 11 - 10")
        self.assertEqual(length_11, validator.validate(length_11), "Exact 11 - 11")
        self.assertIsNone(validator.validate(length_12), "Exact 11 - 12")

    
    @pytest.mark.test
    def testRegex(self):
        validator = CodeValidator(3, None, -1, None, -1, None)

        value2 = "12"
        value3 = "123"
        value4 = "1234"
        value5 = "12345"
        invalid = "12a4"

        self.assertIsNone(validator.getRegexValidator(), "No Regex")
        self.assertEqual(value2, validator.validate(value2), "No Regex 2")
        self.assertEqual(value3, validator.validate(value3), "No Regex 3")
        self.assertEqual(value4, validator.validate(value4), "No Regex 4")
        self.assertEqual(value5, validator.validate(value5), "No Regex 5")
        self.assertEqual(invalid, validator.validate(invalid), "No Regex invalid")

        regex = "^([0-9]{3,4})$"
        validator = CodeValidator(3, None, -1, None, -1, regex)
        self.assertIsNotNone(validator.getRegexValidator(), "No Regex")
        self.assertIsNone(validator.validate(value2), "Regex 2")
        self.assertEqual(value3, validator.validate(value3), "Regex 3")
        self.assertEqual(value4, validator.validate(value4), "Regex 4")
        self.assertIsNone(validator.validate(value5), "Regex 5")
        self.assertIsNone(validator.validate(invalid), "Regex invalid")

        regex = "^([0-9]{3})(?:[-\\s])([0-9]{3})$"
        validator = CodeValidator.CodeValidator1(RegexValidator.RegexValidator3(regex), 6, None)
        self.assertEqual("123456", validator.validate("123-456"), "Reformat 123-456")
        self.assertEqual("123456", validator.validate("123 456"), "Reformat 123 456")
        self.assertIsNone(validator.validate("123456"), "Reformat 123456")
        self.assertIsNone(validator.validate("123.456"), "Reformat 123.456")

        regex = "^(?:([0-9]{3})(?:[-\\s])([0-9]{3}))|([0-9]{6})$"
        validator = CodeValidator.CodeValidator1(RegexValidator.RegexValidator3(regex), 6, None)
        self.assertEqual(
            "RegexValidator{" + regex + "}",
            str(validator.getRegexValidator()),
            "Reformat 2 Regex"
        )
        self.assertEqual("123456", validator.validate("123-456"), "Reformat 2 123-456")
        self.assertEqual("123456", validator.validate("123 456"), "Reformat 2 123 456")
        self.assertEqual("123456", validator.validate("123456"), "Reformat 2 123456")

    
    @pytest.mark.test
    def testNoInput(self):
        validator = CodeValidator(3, None, -1, None, -1, None)
        self.assertIsNone(validator.validate(None), "Null")
        self.assertIsNone(validator.validate(""), "Zero Length")
        self.assertIsNone(validator.validate("   "), "Spaces")
        self.assertEqual("A", validator.validate(" A  "), "Trimmed")

    
    @pytest.mark.test
    def testValidator294_1(self):
        validator = CodeValidator(3, None, -1, None, 0, None)
        self.assertIsNone(validator.validate(None), "Null")
        validator = CodeValidator(3, None, 0, None, -1, None)
        self.assertIsNone(validator.validate(None), "Null")

    
    @pytest.mark.test
    def testValidator294_2(self):
        validator = CodeValidator(3, None, 0, None, -1, None)
        self.assertIsNone(validator.validate(None), "Null")

    
    @pytest.mark.test
    def testConstructors(self):
        validator = None
        regex = RegexValidator.RegexValidator3("^[0-9]*$")

        validator = CodeValidator.CodeValidator2(regex, EAN13CheckDigit.EAN13_CHECK_DIGIT)
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 1 - regex")
        self.assertEqual(-1, validator.getMinLength(), "Constructor 1 - min length")
        self.assertEqual(-1, validator.getMaxLength(), "Constructor 1 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 1 - check digit"
        )

        validator = CodeValidator.CodeValidator1(regex, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT)
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 2 - regex")
        self.assertEqual(13, validator.getMinLength(), "Constructor 2 - min length")
        self.assertEqual(13, validator.getMaxLength(), "Constructor 2 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 2 - check digit"
        )

        validator = CodeValidator(0, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, regex, 10, None)
        self.assertEqual(regex, validator.getRegexValidator(), "Constructor 3 - regex")
        self.assertEqual(10, validator.getMinLength(), "Constructor 3 - min length")
        self.assertEqual(20, validator.getMaxLength(), "Constructor 3 - max length")
        self.assertEqual(
            EAN13CheckDigit.EAN13_CHECK_DIGIT,
            validator.getCheckDigit(),
            "Constructor 3 - check digit"
        )

        validator = CodeValidator.CodeValidator5("^[0-9]*$", EAN13CheckDigit.EAN13_CHECK_DIGIT)
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

        validator = CodeValidator.CodeValidator4("^[0-9]*$", 13, EAN13CheckDigit.EAN13_CHECK_DIGIT)
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

        validator = CodeValidator(3, EAN13CheckDigit.EAN13_CHECK_DIGIT, 20, None, 10, "^[0-9]*$")
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
