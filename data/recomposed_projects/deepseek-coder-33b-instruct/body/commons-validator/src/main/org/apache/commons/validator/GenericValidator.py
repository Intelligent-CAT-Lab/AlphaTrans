from __future__ import annotations
import locale
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.DateValidator import *
from src.main.org.apache.commons.validator.GenericTypeValidator import *
from src.main.org.apache.commons.validator.routines.CreditCardValidator import *
from src.main.org.apache.commons.validator.routines.DateValidator import *
from src.main.org.apache.commons.validator.routines.EmailValidator import *
from src.main.org.apache.commons.validator.routines.UrlValidator import *


class GenericValidator:

    __CREDIT_CARD_VALIDATOR: CreditCardValidator = (
        CreditCardValidator.CreditCardValidator0()
    )
    __URL_VALIDATOR: UrlValidator = UrlValidator.UrlValidator6()
    __serialVersionUID: int = -7212095066891517618

    @staticmethod
    def maxValue3(value: float, max: float) -> bool:
        return value <= max

    @staticmethod
    def maxValue2(value: float, max: float) -> bool:
        return value <= max

    @staticmethod
    def maxValue1(value: int, max: int) -> bool:
        return value <= max

    @staticmethod
    def maxValue0(value: int, max: int) -> bool:
        return value <= max

    @staticmethod
    def minValue3(value: float, min: float) -> bool:
        return value >= min

    @staticmethod
    def minValue2(value: float, min: float) -> bool:
        return value >= min

    @staticmethod
    def minValue1(value: int, min: int) -> bool:
        return value >= min

    @staticmethod
    def minValue0(value: int, min: int) -> bool:
        return value >= min

    @staticmethod
    def minLength1(value: str, min: int, lineEndLength: int) -> bool:

        adjustAmount: int = GenericValidator.__adjustForLineEnding(value, lineEndLength)
        return (len(value) + adjustAmount) >= min

    @staticmethod
    def minLength0(value: str, min: int) -> bool:
        return len(value) >= min

    @staticmethod
    def maxLength1(value: str, max: int, lineEndLength: int) -> bool:

        adjustAmount: int = GenericValidator.__adjustForLineEnding(value, lineEndLength)
        return (len(value) + adjustAmount) <= max

    @staticmethod
    def maxLength0(value: str, max: int) -> bool:
        return len(value) <= max

    @staticmethod
    def isUrl(value: str) -> bool:

        if value is None:
            return False

        try:
            uri = urlparse(value)
        except ValueError:
            return False

        scheme = uri.scheme
        if not GenericValidator.__URL_VALIDATOR._isValidScheme(scheme):
            return False

        authority = uri.netloc
        if scheme.lower() == "file" and (authority is None or authority == ""):
            return True
        elif scheme.lower() == "file" and authority is not None and ":" in authority:
            return False
        else:
            if not GenericValidator.__URL_VALIDATOR._isValidAuthority(authority):
                return False

        if not GenericValidator.__URL_VALIDATOR._isValidPath(uri.path):
            return False

        if not GenericValidator.__URL_VALIDATOR._isValidQuery(uri.query):
            return False

        if not GenericValidator.__URL_VALIDATOR._isValidFragment(uri.fragment):
            return False

        return True

    @staticmethod
    def isEmail(value: str) -> bool:
        return EmailValidator.getInstance0().isValid(value)

    @staticmethod
    def isCreditCard(value: str) -> bool:
        return GenericValidator.__CREDIT_CARD_VALIDATOR.isValid(value)

    @staticmethod
    def isInRange5(value: float, min: float, max: float) -> bool:
        return (value >= min) and (value <= max)

    @staticmethod
    def isInRange4(value: int, min: int, max: int) -> bool:
        return (value >= min) and (value <= max)

    @staticmethod
    def isInRange3(value: int, min: int, max: int) -> bool:
        return (value >= min) and (value <= max)

    @staticmethod
    def isInRange2(value: float, min: float, max: float) -> bool:
        return (value >= min) and (value <= max)

    @staticmethod
    def isInRange1(value: int, min: int, max: int) -> bool:
        return (value >= min) and (value <= max)

    @staticmethod
    def isInRange0(value: int, min: int, max: int) -> bool:
        return (value >= min) and (value <= max)

    @staticmethod
    def isDate1(value: str, datePattern: str, strict: bool) -> bool:
        return DateValidator.getInstance().isValid0(value, datePattern, strict)

    @staticmethod
    def isDate0(value: str, locale: typing.Any) -> bool:
        return DateValidator.getInstance().isValid2(value, locale)

    @staticmethod
    def isDouble(value: str) -> bool:
        return GenericTypeValidator.formatDouble0(value) is not None

    @staticmethod
    def isFloat(value: str) -> bool:
        return GenericTypeValidator.formatFloat0(value) is not None

    @staticmethod
    def isLong(value: str) -> bool:

        return GenericTypeValidator.formatLong0(value) is not None

    @staticmethod
    def isInt(value: str) -> bool:
        return GenericTypeValidator.formatInt0(value) is not None

    @staticmethod
    def isShort(value: str) -> bool:
        return GenericTypeValidator.formatShort0(value) is not None

    @staticmethod
    def isByte(value: str) -> bool:

        return GenericTypeValidator.formatByte0(value) is not None

    @staticmethod
    def matchRegexp(value: str, regexp: str) -> bool:

        import re

        if regexp is None or len(regexp) <= 0:
            return False

        return bool(re.match(regexp, value))

    @staticmethod
    def isBlankOrNull(value: str) -> bool:
        return (value is None) or (len(value.strip()) == 0)

    @staticmethod
    def __adjustForLineEnding(value: str, lineEndLength: int) -> int:

        nCount: int = 0
        rCount: int = 0

        for i in range(len(value)):
            if value[i] == "\n":
                nCount += 1
            if value[i] == "\r":
                rCount += 1

        return (nCount * lineEndLength) - (rCount + nCount)
