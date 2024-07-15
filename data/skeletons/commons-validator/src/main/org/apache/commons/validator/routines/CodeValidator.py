from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.RegexValidator import *
import typing
from typing import *
import io

# Imports End


class CodeValidator:

    # Class Fields Begin
    __serialVersionUID: int = None
    __regexValidator: RegexValidator = None
    __minLength: int = None
    __maxLength: int = None
    __checkdigit: CheckDigit = None
    # Class Fields End

    # Class Methods Begin
    def validate(self, input_: str) -> typing.Any:
        pass

    def isValid(self, input_: str) -> bool:
        pass

    def getRegexValidator(self) -> RegexValidator:
        pass

    def getMaxLength(self) -> int:
        pass

    def getMinLength(self) -> int:
        pass

    def getCheckDigit(self) -> CheckDigit:
        pass

    @staticmethod
    def CodeValidator5(regex: str, checkdigit: CheckDigit) -> CodeValidator:
        pass

    @staticmethod
    def CodeValidator4(
        regex: str, length: int, checkdigit: CheckDigit
    ) -> CodeValidator:
        pass

    @staticmethod
    def CodeValidator2(
        regexValidator: RegexValidator, checkdigit: CheckDigit
    ) -> CodeValidator:
        pass

    @staticmethod
    def CodeValidator1(
        regexValidator: RegexValidator, length: int, checkdigit: CheckDigit
    ) -> CodeValidator:
        pass

    def __init__(
        self,
        constructorId: int,
        checkdigit: CheckDigit,
        maxLength: int,
        regexValidator: RegexValidator,
        minLength: int,
        regex: str,
    ) -> None:
        pass

    # Class Methods End
