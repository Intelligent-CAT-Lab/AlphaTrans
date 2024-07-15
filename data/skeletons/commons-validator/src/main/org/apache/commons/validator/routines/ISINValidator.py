from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.ISINCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
import typing
from typing import *
import io

# Imports End


class ISINValidator:

    # Class Fields Begin
    __serialVersionUID: int = None
    __ISIN_REGEX: str = None
    __VALIDATOR: CodeValidator = None
    __ISIN_VALIDATOR_FALSE: ISINValidator = None
    __ISIN_VALIDATOR_TRUE: ISINValidator = None
    __CCODES: typing.List[typing.List[str]] = None
    __SPECIALS: typing.List[typing.List[str]] = None
    __checkCountryCode: bool = None
    # Class Fields End

    # Class Methods Begin
    def validate(self, code: str) -> typing.Any:
        pass

    def isValid(self, code: str) -> bool:
        pass

    @staticmethod
    def getInstance(checkCountryCode: bool) -> ISINValidator:
        pass

    def __checkCode(self, code: str) -> bool:
        pass

    def __init__(self, checkCountryCode: bool) -> None:
        pass

    # Class Methods End
