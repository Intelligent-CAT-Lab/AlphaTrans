from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *


class CodeValidator:

    __checkdigit: CheckDigit = None

    __maxLength: int = 0

    __minLength: int = 0

    __regexValidator: RegexValidator = None

    __serialVersionUID: int = 446960910870938233

    def validate(self, input_: str) -> typing.Any:

        if input_ is None:
            return None

        code = input_.strip()
        if len(code) == 0:
            return None

        if self.__regexValidator is not None:
            code = self.__regexValidator.validate(code)
            if code is None:
                return None

        if (self.__minLength >= 0 and len(code) < self.__minLength) or (
            self.__maxLength >= 0 and len(code) > self.__maxLength
        ):
            return None

        if self.__checkdigit is not None and not self.__checkdigit.isValid(code):
            return None

        return code

    def isValid(self, input_: str) -> bool:

        return self.validate(input_) is not None

    def getRegexValidator(self) -> RegexValidator:
        return self.__regexValidator

    def getMaxLength(self) -> int:
        return self.__maxLength

    def getMinLength(self) -> int:
        return self.__minLength

    def getCheckDigit(self) -> CheckDigit:
        return self.__checkdigit

    @staticmethod
    def CodeValidator5(regex: str, checkdigit: CheckDigit) -> CodeValidator:
        return CodeValidator(1, checkdigit, -1, None, -1, regex)

    @staticmethod
    def CodeValidator4(
        regex: str, length: int, checkdigit: CheckDigit
    ) -> CodeValidator:
        return CodeValidator(1, checkdigit, length, None, length, regex)

    @staticmethod
    def CodeValidator2(
        regexValidator: RegexValidator, checkdigit: CheckDigit
    ) -> CodeValidator:
        return CodeValidator(0, checkdigit, -1, regexValidator, -1, None)

    @staticmethod
    def CodeValidator1(
        regexValidator: RegexValidator, length: int, checkdigit: CheckDigit
    ) -> CodeValidator:

        return CodeValidator(0, checkdigit, length, regexValidator, length, None)

    def __init__(
        self,
        constructorId: int,
        checkdigit: CheckDigit,
        maxLength: int,
        regexValidator: RegexValidator,
        minLength: int,
        regex: str,
    ) -> None:

        if constructorId == 0:
            self.__regexValidator = regexValidator
            self.__minLength = minLength
            self.__maxLength = maxLength
            self.__checkdigit = checkdigit
        else:
            if regex is not None and len(regex) > 0:
                self.__regexValidator = RegexValidator.RegexValidator3(regex)
            else:
                self.__regexValidator = None
            self.__minLength = minLength
            self.__maxLength = maxLength
            self.__checkdigit = checkdigit
