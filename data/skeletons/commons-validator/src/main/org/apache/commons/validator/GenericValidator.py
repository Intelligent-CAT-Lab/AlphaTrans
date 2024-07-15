from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.UrlValidator import *
from src.main.org.apache.commons.validator.routines.EmailValidator import *
from src.main.org.apache.commons.validator.routines.DateValidator import *
from src.main.org.apache.commons.validator.routines.CreditCardValidator import *
from src.main.org.apache.commons.validator.GenericTypeValidator import *
from src.main.org.apache.commons.validator.DateValidator import *
import typing
from typing import *
import io

# Imports End


class GenericValidator:

    # Class Fields Begin
    __serialVersionUID: int = None
    __URL_VALIDATOR: UrlValidator = None
    __CREDIT_CARD_VALIDATOR: CreditCardValidator = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def maxValue3(value: float, max_: float) -> bool:
        pass

    @staticmethod
    def maxValue2(value: float, max_: float) -> bool:
        pass

    @staticmethod
    def maxValue1(value: int, max_: int) -> bool:
        pass

    @staticmethod
    def maxValue0(value: int, max_: int) -> bool:
        pass

    @staticmethod
    def minValue3(value: float, min_: float) -> bool:
        pass

    @staticmethod
    def minValue2(value: float, min_: float) -> bool:
        pass

    @staticmethod
    def minValue1(value: int, min_: int) -> bool:
        pass

    @staticmethod
    def minValue0(value: int, min_: int) -> bool:
        pass

    @staticmethod
    def minLength1(value: str, min_: int, lineEndLength: int) -> bool:
        pass

    @staticmethod
    def minLength0(value: str, min_: int) -> bool:
        pass

    @staticmethod
    def maxLength1(value: str, max_: int, lineEndLength: int) -> bool:
        pass

    @staticmethod
    def maxLength0(value: str, max_: int) -> bool:
        pass

    @staticmethod
    def isUrl(value: str) -> bool:
        pass

    @staticmethod
    def isEmail(value: str) -> bool:
        pass

    @staticmethod
    def isCreditCard(value: str) -> bool:
        pass

    @staticmethod
    def isInRange5(value: float, min_: float, max_: float) -> bool:
        pass

    @staticmethod
    def isInRange4(value: int, min_: int, max_: int) -> bool:
        pass

    @staticmethod
    def isInRange3(value: int, min_: int, max_: int) -> bool:
        pass

    @staticmethod
    def isInRange2(value: float, min_: float, max_: float) -> bool:
        pass

    @staticmethod
    def isInRange1(value: int, min_: int, max_: int) -> bool:
        pass

    @staticmethod
    def isInRange0(value: int, min_: int, max_: int) -> bool:
        pass

    @staticmethod
    def isDate1(value: str, datePattern: str, strict: bool) -> bool:
        pass

    @staticmethod
    def isDate0(value: str, locale: typing.Any) -> bool:
        pass

    @staticmethod
    def isDouble(value: str) -> bool:
        pass

    @staticmethod
    def isFloat(value: str) -> bool:
        pass

    @staticmethod
    def isLong(value: str) -> bool:
        pass

    @staticmethod
    def isInt(value: str) -> bool:
        pass

    @staticmethod
    def isShort(value: str) -> bool:
        pass

    @staticmethod
    def isByte(value: str) -> bool:
        pass

    @staticmethod
    def matchRegexp(value: str, regexp: str) -> bool:
        pass

    @staticmethod
    def isBlankOrNull(value: str) -> bool:
        pass

    @staticmethod
    def __adjustForLineEnding(value: str, lineEndLength: int) -> int:
        pass

    # Class Methods End
