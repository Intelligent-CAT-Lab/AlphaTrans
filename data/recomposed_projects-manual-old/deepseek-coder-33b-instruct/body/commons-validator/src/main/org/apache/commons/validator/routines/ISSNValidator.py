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
    __EAN_ISSN_LEN: int = 13
    __EAN_ISSN_REGEX: str = "^(977)(?:(\\d{10}))$"
    __ISSN_PREFIX: str = "977"
    __ISSN_LEN: int = 8
    __ISSN_REGEX: str = "(?:ISSN )?(\\d{4})-(\\d{3}[0-9X])$"
    __serialVersionUID: int = 4319515687976420405
    __EAN_VALIDATOR: CodeValidator = CodeValidator.CodeValidator4(
        __EAN_ISSN_REGEX, __EAN_ISSN_LEN, EAN13CheckDigit.EAN13_CHECK_DIGIT
    )
    __VALIDATOR: CodeValidator = CodeValidator.CodeValidator4(
        __ISSN_REGEX, __ISSN_LEN, ISSNCheckDigit.ISSN_CHECK_DIGIT
    )

    @staticmethod
    def initialize_fields() -> None:
        ISSNValidator.__ISSN_VALIDATOR: ISSNValidator = ISSNValidator()

    def extractFromEAN13(self, ean13: str) -> str:

        input = ean13.strip()
        if len(input) != self.__EAN_ISSN_LEN:
            raise ValueError(
                "Invalid length " + str(len(input)) + " for '" + input + "'"
            )
        if not input.startswith(self.__ISSN_PREFIX):
            raise ValueError(
                "Prefix must be "
                + self.__ISSN_PREFIX
                + " to contain an ISSN: '"
                + ean13
                + "'"
            )
        result = self.validateEan(input)
        if result is None:
            return None
        input = str(result)
        try:
            issnBase = input[3:10]  # TODO: how to derive these
            checkDigit = ISSNCheckDigit.ISSN_CHECK_DIGIT.calculate(issnBase)
            issn = issnBase + checkDigit
            return issn
        except CheckDigitException as e:  # Should not happen
            raise ValueError("Check digit error for '" + ean13 + "' - " + str(e))

    def convertToEAN13(self, issn: str, suffix: str) -> str:

        if suffix is None or not re.match("\\d\\d", suffix):
            raise ValueError("Suffix must be two digits: '" + suffix + "'")

        result = self.validate(issn)
        if result is None:
            return None

        input = result.toString()
        ean13 = self.__ISSN_PREFIX + input[0 : len(input) - 1] + suffix
        try:
            checkDigit = EAN13CheckDigit.EAN13_CHECK_DIGIT.calculate(ean13)
            ean13 += checkDigit
            return ean13
        except CheckDigitException as e:  # Should not happen
            raise ValueError("Check digit error for '" + ean13 + "' - " + str(e))

    def validate(self, code: str) -> typing.Any:

        pass  # LLM could not translate this method

    def isValid(self, code: str) -> bool:

        pass  # LLM could not translate this method

    def validateEan(self, code: str) -> typing.Any:

        pass  # LLM could not translate this method

    @staticmethod
    def getInstance() -> ISSNValidator:
        return ISSNValidator.__ISSN_VALIDATOR


ISSNValidator.initialize_fields()
