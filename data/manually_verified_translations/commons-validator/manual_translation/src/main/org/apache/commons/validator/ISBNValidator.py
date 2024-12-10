from __future__ import annotations
from src.main.org.apache.commons.validator.routines.ISBNValidator import ISBNValidator as ISBNValidatorRef


class ISBNValidator:

    def isValid(self, isbn: str) -> bool:

        return ISBNValidatorRef.getInstance0().isValidISBN10(isbn)

    def __init__(self) -> None:
        super().__init__()
