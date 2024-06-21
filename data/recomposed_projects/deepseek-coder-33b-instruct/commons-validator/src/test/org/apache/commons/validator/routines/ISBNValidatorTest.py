import unittest
import re
from src.main.org.apache.commons.validator.routines.ISBNValidator import *

class ISBNValidatorTest(unittest.TestCase):

    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)
        self.__validISBN10Format = [
            "1234567890",
            "123456789X",
            "12345-1234567-123456-X",
            "12345 1234567 123456 X",
            "1-2-3-4",
            "1 2 3 4",
        ]

        self.__invalidISBN10Format = [
            "",  # empty
            "   ",  # empty
            "1",  # too short
            "123456789",  # too short
            "12345678901",  # too long
            "12345678X0",  # X not at end
            "123456-1234567-123456-X",  # Group too long
            "12345-12345678-123456-X",  # Publisher too long
            "12345-1234567-1234567-X",  # Title too long
            "12345-1234567-123456-X2",  # Check Digit too long
            "--1 930110 99 5",  # format
            "1 930110 99 5--",  # format
            "1 930110-99 5-",  # format
            "1.2.3.4",  # Invalid Separator
            "1=2=3=4",  # Invalid Separator
            "1_2_3_4",  # Invalid Separator
            "123456789Y",  # Other character at the end
            "dsasdsadsa",  # invalid characters
            "I love sparrows!",  # invalid characters
            "068-556-98-45"  # format
        ]

        self.__validISBN13Format = [
            "9781234567890",
            "9791234567890",
            "978-12345-1234567-123456-1",
            "979-12345-1234567-123456-1",
            "978 12345 1234567 123456 1",
            "979 12345 1234567 123456 1",
            "978-1-2-3-4",
            "979-1-2-3-4",
            "978 1 2 3 4",
            "979 1 2 3 4",
        ]

        self.__invalidISBN13Format = [
            "",  # empty
            "   ",  # empty
            "1",  # too short
            "978123456789",  # too short
            "97812345678901",  # too long
            "978-123456-1234567-123456-1",  # Group too long
            "978-12345-12345678-123456-1",  # Publisher too long
            "978-12345-1234567-1234567-1",  # Title too long
            "978-12345-1234567-123456-12",  # Check Digit too long
            "--978 1 930110 99 1",  # format
            "978 1 930110 99 1--",  # format
            "978 1 930110-99 1-",  # format
            "123-4-567890-12-8",  # format
            "978.1.2.3.4",  # Invalid Separator
            "978=1=2=3=4",  # Invalid Separator
            "978_1_2_3_4",  # Invalid Separator
            "978123456789X",  # invalid character
            "978-0-201-63385-X",  # invalid character
            "dsasdsadsadsa",  # invalid characters
            "I love sparrows!",  # invalid characters
            "979-1-234-567-89-6"  # format
        ]

    
    def test_ValidISBN10Format(self) -> None:
        pattern = re.compile(ISBNValidator.ISBN10_REGEX)
        for i in range(len(self.__validISBN10Format)):
            self.assertTrue(
                pattern.match(self.__validISBN10Format[i]),
                "Pattern[" + str(i) + "]=" + self.__validISBN10Format[i]
            )

    
    def test_InvalidISBN10Format(self) -> None:
        validator = ISBNValidator.getInstance0()
        pattern = re.compile(ISBNValidator.ISBN10_REGEX)
        for i in range(len(self.__invalidISBN10Format)):
            self.assertFalse(
                pattern.match(self.__invalidISBN10Format[i]),
                "Pattern[" + str(i) + "]=" + self.__invalidISBN10Format[i]
            )
            self.assertFalse(
                validator.isValidISBN10(self.__invalidISBN10Format[i]),
                "isValidISBN10[" + str(i) + "]=" + self.__invalidISBN10Format[i]
            )
            self.assertIsNone(
                validator.validateISBN10(self.__invalidISBN10Format[i]),
                "validateISBN10[" + str(i) + "]=" + self.__invalidISBN10Format[i]
            )

    
    def test_ValidISBN13Format(self) -> None:
        pattern = re.compile(ISBNValidator.ISBN13_REGEX)
        for i in range(len(self.__validISBN13Format)):
            self.assertTrue(
                pattern.match(self.__validISBN13Format[i]),
                "Pattern[" + str(i) + "]=" + self.__validISBN13Format[i]
            )

    
    def test_InvalidISBN13Format(self) -> None:
        pattern = re.compile(ISBNValidator.ISBN13_REGEX)
        validator = ISBNValidator.getInstance0()
        for i in range(len(self.__invalidISBN13Format)):
            self.assertFalse(
                pattern.match(self.__invalidISBN13Format[i]),
                "Pattern[" + str(i) + "]=" + self.__invalidISBN13Format[i]
            )
            self.assertFalse(
                validator.isValidISBN13(self.__invalidISBN13Format[i]),
                "isValidISBN13[" + str(i) + "]=" + self.__invalidISBN13Format[i]
            )
            self.assertIsNone(
                validator.validateISBN13(self.__invalidISBN13Format[i]),
                "validateISBN13[" + str(i) + "]=" + self.__invalidISBN13Format[i]
            )

    
    def test_IsValidISBN10(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertTrue(
            validator.isValidISBN10("1930110995"), "isValidISBN10-1"
        )
        self.assertTrue(
            validator.isValidISBN10("1-930110-99-5"), "isValidISBN10-2"
        )
        self.assertTrue(
            validator.isValidISBN10("1 930110 99 5"), "isValidISBN10-3"
        )
        self.assertTrue(
            validator.isValidISBN10("020163385X"), "isValidISBN10-4"
        )
        self.assertTrue(
            validator.isValidISBN10("0-201-63385-X"), "isValidISBN10-5"
        )
        self.assertTrue(
            validator.isValidISBN10("0 201 63385 X"), "isValidISBN10-6"
        )

        self.assertTrue(
            validator.isValid("1930110995"), "isValid-1"
        )
        self.assertTrue(
            validator.isValid("1-930110-99-5"), "isValid-2"
        )
        self.assertTrue(
            validator.isValid("1 930110 99 5"), "isValid-3"
        )
        self.assertTrue(
            validator.isValid("020163385X"), "isValid-4"
        )
        self.assertTrue(
            validator.isValid("0-201-63385-X"), "isValid-5"
        )
        self.assertTrue(
            validator.isValid("0 201 63385 X"), "isValid-6"
        )

    
    def test_IsValidISBN13(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertTrue(
            validator.isValidISBN13("9781930110991"), "isValidISBN13-1"
        )
        self.assertTrue(
            validator.isValidISBN13("978-1-930110-99-1"), "isValidISBN13-2"
        )
        self.assertTrue(
            validator.isValidISBN13("978 1 930110 99 1"), "isValidISBN13-3"
        )
        self.assertTrue(
            validator.isValidISBN13("9780201633856"), "isValidISBN13-4"
        )
        self.assertTrue(
            validator.isValidISBN13("978-0-201-63385-6"), "isValidISBN13-5"
        )
        self.assertTrue(
            validator.isValidISBN13("978 0 201 63385 6"), "isValidISBN13-6"
        )

        self.assertTrue(
            validator.isValid("9781930110991"), "isValid-1"
        )
        self.assertTrue(
            validator.isValid("978-1-930110-99-1"), "isValid-2"
        )
        self.assertTrue(
            validator.isValid("978 1 930110 99 1"), "isValid-3"
        )
        self.assertTrue(
            validator.isValid("9780201633856"), "isValid-4"
        )
        self.assertTrue(
            validator.isValid("978-0-201-63385-6"), "isValid-5"
        )
        self.assertTrue(
            validator.isValid("978 0 201 63385 6"), "isValid-6"
        )

    
    def test_ValidateISBN10(self) -> None:
        validator = ISBNValidator.getInstance1(False)
        self.assertEqual(
            "1930110995",
            validator.validateISBN10("1930110995"),
            "validateISBN10-1"
        )
        self.assertEqual(
            "1930110995",
            validator.validateISBN10("1-930110-99-5"),
            "validateISBN10-2"
        )
        self.assertEqual(
            "1930110995",
            validator.validateISBN10("1 930110 99 5"),
            "validateISBN10-3"
        )
        self.assertEqual(
            "020163385X",
            validator.validateISBN10("020163385X"),
            "validateISBN10-4"
        )
        self.assertEqual(
            "020163385X",
            validator.validateISBN10("0-201-63385-X"),
            "validateISBN10-5"
        )
        self.assertEqual(
            "020163385X",
            validator.validateISBN10("0 201 63385 X"),
            "validateISBN10-6"
        )

        self.assertEqual(
            "1930110995",
            validator.validate("1930110995"),
            "validate-1"
        )
        self.assertEqual(
            "1930110995",
            validator.validate("1-930110-99-5"),
            "validate-2"
        )
        self.assertEqual(
            "1930110995",
            validator.validate("1 930110 99 5"),
            "validate-3"
        )
        self.assertEqual(
            "020163385X",
            validator.validate("020163385X"),
            "validate-4"
        )
        self.assertEqual(
            "020163385X",
            validator.validate("0-201-63385-X"),
            "validate-5"
        )
        self.assertEqual(
            "020163385X",
            validator.validate("0 201 63385 X"),
            "validate-6"
        )

    
    def test_ValidateISBN10Convert(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertEqual(
            "9781930110991",
            validator.validate("1930110995"),
            "validate-1"
        )
        self.assertEqual(
            "9781930110991",
            validator.validate("1-930110-99-5"),
            "validate-2"
        )
        self.assertEqual(
            "9781930110991",
            validator.validate("1 930110 99 5"),
            "validate-3"
        )
        self.assertEqual(
            "9780201633856",
            validator.validate("020163385X"),
            "validate-4"
        )
        self.assertEqual(
            "9780201633856",
            validator.validate("0-201-63385-X"),
            "validate-5"
        )
        self.assertEqual(
            "9780201633856",
            validator.validate("0 201 63385 X"),
            "validate-6"
        )

    
    def test_ValidateISBN13(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertEqual(
            "9781930110991",
            validator.validateISBN13("9781930110991"),
            "validateISBN13-1"
        )
        self.assertEqual(
            "9781930110991",
            validator.validateISBN13("978-1-930110-99-1"),
            "validateISBN13-2"
        )
        self.assertEqual(
            "9781930110991",
            validator.validateISBN13("978 1 930110 99 1"),
            "validateISBN13-3"
        )
        self.assertEqual(
            "9780201633856",
            validator.validateISBN13("9780201633856"),
            "validateISBN13-4"
        )
        self.assertEqual(
            "9780201633856",
            validator.validateISBN13("978-0-201-63385-6"),
            "validateISBN13-5"
        )
        self.assertEqual(
            "9780201633856",
            validator.validateISBN13("978 0 201 63385 6"),
            "validateISBN13-6"
        )

        self.assertEqual(
            "9781930110991",
            validator.validate("9781930110991"),
            "validate-1"
        )
        self.assertEqual(
            "9781930110991",
            validator.validate("978-1-930110-99-1"),
            "validate-2"
        )
        self.assertEqual(
            "9781930110991",
            validator.validate("978 1 930110 99 1"),
            "validate-3"
        )
        self.assertEqual(
            "9780201633856",
            validator.validate("9780201633856"),
            "validate-4"
        )
        self.assertEqual(
            "9780201633856",
            validator.validate("978-0-201-63385-6"),
            "validate-5"
        )
        self.assertEqual(
            "9780201633856",
            validator.validate("978 0 201 63385 6"),
            "validate-6"
        )

    
    def test_Null(self) -> None:
        validator = ISBNValidator.getInstance0()
        self.assertFalse(
            validator.isValid(None),
            "isValid"
        )
        self.assertFalse(
            validator.isValidISBN10(None),
            "isValidISBN10"
        )
        self.assertFalse(
            validator.isValidISBN13(None),
            "isValidISBN13"
        )
        self.assertIsNone(
            validator.validate(None),
            "validate"
        )
        self.assertIsNone(
            validator.validateISBN10(None),
            "validateISBN10"
        )
        self.assertIsNone(
            validator.validateISBN13(None),
            "validateISBN13"
        )
        self.assertIsNone(
            validator.convertToISBN13(None),
            "convertToISBN13"
        )

    
    def test_Invalid(self) -> None:
        validator = ISBNValidator.getInstance0()
        base_code = "193011099"
        self.assertFalse(
            validator.isValid(base_code + "0"),
            "ISBN10-0"
        )
        self.assertFalse(
            validator.isValid(base_code + "1"),
            "ISBN10-1"
        )
        self.assertFalse(
            validator.isValid(base_code + "2"),
            "ISBN10-2"
        )
        self.assertFalse(
            validator.isValid(base_code + "3"),
            "ISBN10-3"
        )
        self.assertFalse(
            validator.isValid(base_code + "4"),
            "ISBN10-4"
        )
        self.assertTrue(
            validator.isValid(base_code + "5"),
            "ISBN10-5"
        )
        self.assertFalse(
            validator.isValid(base_code + "6"),
            "ISBN10-6"
        )
        self.assertFalse(
            validator.isValid(base_code + "7"),
            "ISBN10-7"
        )
        self.assertFalse(
            validator.isValid(base_code + "8"),
            "ISBN10-8"
        )
        self.assertFalse(
            validator.isValid(base_code + "9"),
            "ISBN10-9"
        )
        self.assertFalse(
            validator.isValid(base_code + "X"),
            "ISBN10-X"
        )

        base_code = "978193011099"
        self.assertFalse(
            validator.isValid(base_code + "0"),
            "ISBN13-0"
        )
        self.assertTrue(
            validator.isValid(base_code + "1"),
            "ISBN13-1"
        )
        self.assertFalse(
            validator.isValid(base_code + "2"),
            "ISBN13-2"
        )
        self.assertFalse(
            validator.isValid(base_code + "3"),
            "ISBN13-3"
        )
        self.assertFalse(
            validator.isValid(base_code + "4"),
            "ISBN13-4"
        )
        self.assertFalse(
            validator.isValid(base_code + "5"),
            "ISBN13-5"
        )
        self.assertFalse(
            validator.isValid(base_code + "6"),
            "ISBN13-6"
        )
        self.assertFalse(
            validator.isValid(base_code + "7"),
            "ISBN13-7"
        )
        self.assertFalse(
            validator.isValid(base_code + "8"),
            "ISBN13-8"
        )
        self.assertFalse(
            validator.isValid(base_code + "9"),
            "ISBN13-9"
        )

    
    def test_ConversionErrors(self) -> None:
        validator = ISBNValidator.getInstance0()
        inputs = [
            "123456789 ",
            "12345678901",
            "",
            "X234567890"
        ]
        for input in inputs:
            with self.assertRaises(
                ValueError,
                msg=f"Expected IllegalArgumentException for '{input}'"
            ):
                validator.convertToISBN13(input)
