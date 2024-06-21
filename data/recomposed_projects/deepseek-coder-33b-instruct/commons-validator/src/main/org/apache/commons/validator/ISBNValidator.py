from __future__ import annotations
import io
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit import *


class ISBNValidator:

    def isValid(self, isbn: str) -> bool:

        # Create an instance of ISBNValidator
        validator = ISBNValidator.getInstance0()

        # Check if the ISBN is valid
        return validator.isValidISBN10(isbn)

    def __init__(self) -> None:

        self.codeValidator = CodeValidator()
        self.ean13CheckDigit = EAN13CheckDigit()
        self.isbn10CheckDigit = ISBN10CheckDigit()
