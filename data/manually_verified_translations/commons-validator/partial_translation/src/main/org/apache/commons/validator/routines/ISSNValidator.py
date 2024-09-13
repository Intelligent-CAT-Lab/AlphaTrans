from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.ISSNCheckDigit import *


class ISSNValidator:

    __ISSN_VALIDATOR: ISSNValidator = None
    __VALIDATOR: CodeValidator = CodeValidator.CodeValidator4(
        "(?:ISSN )?(\\d{4})-(\\d{3}[0-9X])$", 8, ISSNCheckDigit.ISSN_CHECK_DIGIT
    )
    __EAN_ISSN_LEN: int = 13
    __EAN_ISSN_REGEX: str = "^(977)(?:(\\d{10}))$"
    __ISSN_PREFIX: str = "977"
    __ISSN_LEN: int = 8
    __ISSN_REGEX: str = "(?:ISSN )?(\\d{4})-(\\d{3}[0-9X])$"
    __serialVersionUID: int = 4319515687976420405
    __EAN_VALIDATOR: CodeValidator = CodeValidator.CodeValidator4(
        __EAN_ISSN_REGEX, __EAN_ISSN_LEN, EAN13CheckDigit.EAN13_CHECK_DIGIT
    )

    @staticmethod
    def initialize_fields() -> None:
        ISSNValidator.__ISSN_VALIDATOR: ISSNValidator = ISSNValidator()

    def extractFromEAN13(self, ean13: str) -> str:

        input = ean13.strip()
        if len(input) != self.__EAN_ISSN_LEN:
            raise ValueError(f"Invalid length {len(input)} for '{input}'")
        if not input.startswith(self.__ISSN_PREFIX):
            raise ValueError(
                f"Prefix must be {self.__ISSN_PREFIX} to contain an ISSN: '{ean13}'"
            )
        result = self.validateEan(input)
        if result is None:
            return None
        input = str(result)
        try:
            issnBase = input[3:10]
            checkDigit = ISSNCheckDigit.ISSN_CHECK_DIGIT.calculate(issnBase)
            issn = issnBase + checkDigit
            return issn
        except CheckDigitException as e:
            raise ValueError(f"Check digit error for '{ean13}' - {str(e)}")

    def convertToEAN13(self, issn: str, suffix: str) -> str:

        if suffix is None or not suffix.isdigit() or len(suffix) != 2:
            raise ValueError("Suffix must be two digits: '" + suffix + "'")

        result = self.validate(issn)
        if result is None:
            return None

        input = result
        ean13 = self.__ISSN_PREFIX + input[:-1] + suffix
        try:
            checkDigit = EAN13CheckDigit.EAN13_CHECK_DIGIT.calculate(ean13)
            ean13 += checkDigit
            return ean13
        except CheckDigitException as e:  # Should not happen
            raise ValueError("Check digit error for '" + ean13 + "' - " + str(e))

    def validate(self, code: str) -> typing.Any:

        return self.__VALIDATOR.validate(code)

    def isValid(self, code: str) -> bool:

        return self.__VALIDATOR.isValid(code)

    def validateEan(self, code: str) -> typing.Any:

        if code is None:
            return None

        code = code.strip()
        if len(code) == 0:
            return None

        if self.__EAN_VALIDATOR.__regexValidator is not None:
            code = self.__EAN_VALIDATOR.__regexValidator.validate(code)
            if code is None:
                return None

        if (
            self.__EAN_VALIDATOR.__minLength >= 0
            and len(code) < self.__EAN_VALIDATOR.__minLength
        ) or (
            self.__EAN_VALIDATOR.__maxLength >= 0
            and len(code) > self.__EAN_VALIDATOR.__maxLength
        ):
            return None

        if (
            self.__EAN_VALIDATOR.__checkdigit is not None
            and not self.__EAN_VALIDATOR.__checkdigit.isValid(code)
        ):
            return None

        return code

    @staticmethod
    def getInstance() -> ISSNValidator:
        return ISSNValidator.__ISSN_VALIDATOR


ISSNValidator.initialize_fields()
