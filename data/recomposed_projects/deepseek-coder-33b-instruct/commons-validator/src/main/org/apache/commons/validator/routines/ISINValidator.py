from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISINCheckDigit import *


class ISINValidator:

    __checkCountryCode: bool = None

    __SPECIALS: typing.List[str] = ["EZ", "XS"]

    __CCODES: typing.List[str] = list(pycountry.countries)

    __ISIN_VALIDATOR_TRUE: ISINValidator = ISINValidator(True)

    __ISIN_VALIDATOR_FALSE: ISINValidator = ISINValidator(False)

    __VALIDATOR: CodeValidator = CodeValidator.CodeValidator4(
        ISIN_REGEX, 12, ISINCheckDigit.ISIN_CHECK_DIGIT
    )

    __ISIN_REGEX: str = "([A-Z]{2}[A-Z0-9]{9}[0-9])"

    __serialVersionUID: int = -5964391439144260936

    def validate(self, code: str) -> typing.Any:

        validate = self.__VALIDATOR.validate(code)
        if validate is not None and self.__checkCountryCode:
            return self.__checkCode(code[0:2]) if validate else None
        return validate

    def isValid(self, code: str) -> bool:

        valid = self.__VALIDATOR.isValid(code)
        if valid and self.__checkCountryCode:
            return self.__checkCode(code[0:2])
        return valid

    @staticmethod
    def getInstance(checkCountryCode: bool) -> ISINValidator:

        if checkCountryCode:
            return ISINValidator.__ISIN_VALIDATOR_TRUE
        else:
            return ISINValidator.__ISIN_VALIDATOR_FALSE

    def __checkCode(self, code: str) -> bool:

        def binary_search(arr: List[str], x: str) -> int:
            low = 0
            high = len(arr) - 1
            mid = 0

            while low <= high:

                mid = (high + low) // 2

                if arr[mid] < x:
                    low = mid + 1

                elif arr[mid] > x:
                    high = mid - 1

                else:
                    return mid

            return -1

        return (
            binary_search(self.__CCODES, code) >= 0
            or binary_search(self.__SPECIALS, code) >= 0
        )

    def __init__(self, checkCountryCode: bool) -> None:

        self.__checkCountryCode = checkCountryCode
