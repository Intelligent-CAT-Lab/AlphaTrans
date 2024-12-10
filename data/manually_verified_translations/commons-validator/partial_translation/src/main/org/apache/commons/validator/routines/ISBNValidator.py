from __future__ import annotations
import re
import io
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit import *


class ISBNValidator:

    __convert: bool = False

    __ISBN_VALIDATOR_NO_CONVERT: ISBNValidator = None
    __ISBN_VALIDATOR: ISBNValidator = None
    __TITLE: str = "(\\d{1,6})"
    __PUBLISHER: str = "(\\d{1,7})"
    __GROUP: str = "(\\d{1,5})"
    __SEP: str = "(?:\\-|\\s)"
    __serialVersionUID: int = 4319515687976420405
    __ISBN_10_LEN: int = 10

    ISBN13_REGEX: str = None  # LLM could not translate this field

    ISBN10_REGEX: str = None  # LLM could not translate this field

    __isbn13Validator: CodeValidator = None
    __isbn10Validator: CodeValidator = None

    @staticmethod
    def initialize_fields() -> None:
        ISBNValidator.__ISBN_VALIDATOR_NO_CONVERT: ISBNValidator = ISBNValidator(False)

        ISBNValidator.__ISBN_VALIDATOR: ISBNValidator = ISBNValidator.ISBNValidator1()

        ISBNValidator.__isbn13Validator: CodeValidator = CodeValidator.CodeValidator4(
            ISBNValidator.ISBN13_REGEX, 13, EAN13CheckDigit.EAN13_CHECK_DIGIT
        )

        ISBNValidator.__isbn10Validator: CodeValidator = CodeValidator.CodeValidator4(
            ISBNValidator.ISBN10_REGEX, 10, ISBN10CheckDigit.ISBN10_CHECK_DIGIT
        )

    def convertToISBN13(self, isbn10: str) -> str:

        if isbn10 is None:
            return None

        input = isbn10.strip()
        if len(input) != self.__ISBN_10_LEN:
            raise ValueError(f"Invalid length {len(input)} for '{input}'")

        isbn13 = "978" + input[:-1]
        try:
            checkDigit = self.__isbn13Validator.getCheckDigit().calculate(isbn13)
            isbn13 += checkDigit
            return isbn13
        except CheckDigitException as e:
            raise ValueError(f"Check digit error for '{input}' - {str(e)}")

    def validateISBN13(self, code: str) -> str:

        result = self.__isbn13Validator.validate(code)
        return None if result is None else str(result)

    def validateISBN10(self, code: str) -> str:

        result = self.__isbn10Validator.validate(code)
        return None if result is None else str(result)

    def validate(self, code: str) -> str:

        result = self.validateISBN13(code)
        if result is None:
            result = self.validateISBN10(code)
            if result is not None and self.__convert:
                result = self.convertToISBN13(result)
        return result

    def isValidISBN13(self, code: str) -> bool:

        return self.__isbn13Validator.isValid(code)

    def isValidISBN10(self, code: str) -> bool:

        return self.__isbn10Validator.isValid(code)

    def isValid(self, code: str) -> bool:

        return self.isValidISBN13(code) or self.isValidISBN10(code)

    @staticmethod
    def ISBNValidator1() -> ISBNValidator:
        return ISBNValidator(True)

    def __init__(self, convert: bool) -> None:
        self.__convert = convert

    @staticmethod
    def getInstance1(convert: bool) -> ISBNValidator:
        return (
            ISBNValidator.__ISBN_VALIDATOR
            if convert
            else ISBNValidator.__ISBN_VALIDATOR_NO_CONVERT
        )

    @staticmethod
    def getInstance0() -> ISBNValidator:
        return ISBNValidator.__ISBN_VALIDATOR


ISBNValidator.initialize_fields()
