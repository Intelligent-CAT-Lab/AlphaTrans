from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
import io

# Imports End


class ISBNValidator:

    # Class Fields Begin
    __ISBN_VALIDATOR: ISBNValidator = None
    __ISBN_VALIDATOR_NO_CONVERT: ISBNValidator = None
    __isbn10Validator: CodeValidator = None
    __isbn13Validator: CodeValidator = None
    __convert: bool = None
    __ISBN_10_LEN: int = None
    __serialVersionUID: int = None
    __SEP: str = None
    __GROUP: str = None
    __PUBLISHER: str = None
    __TITLE: str = None
    ISBN10_REGEX: str = None
    ISBN13_REGEX: str = None
    # Class Fields End

    # Class Methods Begin
    def convertToISBN13(self, isbn10: str) -> str:
        pass

    def validateISBN13(self, code: str) -> str:
        pass

    def validateISBN10(self, code: str) -> str:
        pass

    def validate(self, code: str) -> str:
        pass

    def isValidISBN13(self, code: str) -> bool:
        pass

    def isValidISBN10(self, code: str) -> bool:
        pass

    def isValid(self, code: str) -> bool:
        pass

    @staticmethod
    def ISBNValidator1() -> ISBNValidator:
        pass

    def __init__(self, convert: bool) -> None:
        pass

    @staticmethod
    def getInstance1(convert: bool) -> ISBNValidator:
        pass

    @staticmethod
    def getInstance0() -> ISBNValidator:
        pass

    # Class Methods End
