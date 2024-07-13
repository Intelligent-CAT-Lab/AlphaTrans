from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.util.Flags import *
import typing
from typing import *
import io

# Imports End


class CreditCardRange:

    # Class Fields Begin
    low: str = None
    high: str = None
    minLen: int = None
    maxLen: int = None
    lengths: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def __init__(
        self,
        constructorId: int,
        low: str,
        high: str,
        minLen: int,
        maxLen: int,
        lengths: typing.List[int],
    ) -> None:
        pass

    # Class Methods End


class CreditCardValidator:

    # Class Fields Begin
    NONE: int = None
    AMEX: int = None
    VISA: int = None
    MASTERCARD: int = None
    DISCOVER: int = None
    DINERS: int = None
    VPAY: int = None
    MASTERCARD_PRE_OCT2016: int = None
    __cardTypes: typing.List[CodeValidator] = None
    __LUHN_VALIDATOR: CheckDigit = None
    AMEX_VALIDATOR: CodeValidator = None
    DINERS_VALIDATOR: CodeValidator = None
    __DISCOVER_REGEX: RegexValidator = None
    DISCOVER_VALIDATOR: CodeValidator = None
    __MASTERCARD_REGEX: RegexValidator = None
    MASTERCARD_VALIDATOR: CodeValidator = None
    MASTERCARD_VALIDATOR_PRE_OCT2016: CodeValidator = None
    VISA_VALIDATOR: CodeValidator = None
    VPAY_VALIDATOR: CodeValidator = None
    __serialVersionUID: int = None
    __MIN_CC_LENGTH: int = None
    __MAX_CC_LENGTH: int = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def createRangeValidator(
        creditCardRanges: typing.List[CreditCardRange], digitCheck: CheckDigit
    ) -> CodeValidator:
        pass

    @staticmethod
    def validLength(valueLength: int, range_: CreditCardRange) -> bool:
        pass

    def validate(self, card: str) -> typing.Any:
        pass

    def isValid(self, card: str) -> bool:
        pass

    @staticmethod
    def genericCreditCardValidator2() -> CreditCardValidator:
        pass

    @staticmethod
    def genericCreditCardValidator1(length: int) -> CreditCardValidator:
        pass

    @staticmethod
    def genericCreditCardValidator0(minLen: int, maxLen: int) -> CreditCardValidator:
        pass

    def __init__(
        self,
        constructorId: int,
        options: int,
        creditCardRanges: typing.List[CreditCardRange],
        creditCardValidators: typing.List[CodeValidator],
    ) -> None:
        pass

    @staticmethod
    def CreditCardValidator0() -> CreditCardValidator:
        pass

    def __isOn(self, options: int, flag: int) -> bool:
        pass

    # Class Methods End
