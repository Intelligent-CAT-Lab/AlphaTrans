from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.IBANCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.ValidatorResources import *
import typing
from typing import *
import io

# Imports End


class Validator:

    # Class Fields Begin
    __MIN_LEN: int = None
    __MAX_LEN: int = None
    countryCode: str = None
    validator: RegexValidator = None
    lengthOfIBAN: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, cc: str, len_: int, format_: str) -> None:
        pass

    # Class Methods End


class IBANValidator:

    # Class Fields Begin
    __DEFAULT_FORMATS: typing.List[Validator] = None
    DEFAULT_IBAN_VALIDATOR: IBANValidator = None
    __formatValidators: typing.Dict[str, Validator] = None
    # Class Fields End

    # Class Methods Begin
    def setValidator1(self, countryCode: str, length: int, format_: str) -> Validator:
        pass

    def setValidator0(self, validator: Validator) -> Validator:
        pass

    def getValidator(self, code: str) -> Validator:
        pass

    def getDefaultValidators(self) -> typing.List[Validator]:
        pass

    def hasValidator(self, code: str) -> bool:
        pass

    def isValid(self, code: str) -> bool:
        pass

    @staticmethod
    def IBANValidator1() -> IBANValidator:
        pass

    def __init__(self, formatMap: typing.List[Validator]) -> None:
        pass

    @staticmethod
    def getInstance() -> IBANValidator:
        pass

    def __createValidators(
        self, formatMap: typing.List[Validator]
    ) -> typing.Dict[str, Validator]:
        pass

    # Class Methods End
