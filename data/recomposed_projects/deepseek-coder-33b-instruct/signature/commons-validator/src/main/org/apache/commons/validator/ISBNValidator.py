from __future__ import annotations
import re
import io
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit import *


class ISBNValidator:

    def isValid(self, isbn: str) -> bool:

        # Check if the ISBN is a valid ISBN-10
        if len(isbn) == self.__ISBN_10_LEN:
            return self.__isbn10Validator.isValid(isbn)

        # Check if the ISBN is a valid ISBN-13
        elif len(isbn) == 13:
            return self.__isbn13Validator.isValid(isbn)

        # If the ISBN is not valid
        else:
            return False

    def __init__(self) -> None:

        self.codeValidator = CodeValidator()
        self.ean13CheckDigit = EAN13CheckDigit()
        self.isbn10CheckDigit = ISBN10CheckDigit()
