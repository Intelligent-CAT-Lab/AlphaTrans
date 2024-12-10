from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.checkdigit.ISSNCheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigit import *
from src.main.org.apache.commons.validator.routines.CodeValidator import *
import typing
from typing import *
import io

# Imports End


class ISSNValidator:

    # Class Fields Begin
    __serialVersionUID: int = None
    __ISSN_REGEX: str = None
    __ISSN_LEN: int = None
    __ISSN_PREFIX: str = None
    __EAN_ISSN_REGEX: str = None
    __EAN_ISSN_LEN: int = None
    __VALIDATOR: CodeValidator = None
    __EAN_VALIDATOR: CodeValidator = None
    __ISSN_VALIDATOR: ISSNValidator = None
    # Class Fields End

    # Class Methods Begin
    def extractFromEAN13(self, ean13: str) -> str:
        pass

    def convertToEAN13(self, issn: str, suffix: str) -> str:
        pass

    def validate(self, code: str) -> typing.Any:
        pass

    def isValid(self, code: str) -> bool:
        pass

    def validateEan(self, code: str) -> typing.Any:
        pass

    @staticmethod
    def getInstance() -> ISSNValidator:
        pass

    # Class Methods End
