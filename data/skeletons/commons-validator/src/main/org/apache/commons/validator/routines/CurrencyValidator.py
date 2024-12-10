from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
import typing
from typing import *
import io

# Imports End


class CurrencyValidator(BigDecimalValidator):

    # Class Fields Begin
    __serialVersionUID: int = None
    __VALIDATOR: CurrencyValidator = None
    __CURRENCY_SYMBOL: str = None
    # Class Fields End

    # Class Methods Begin
    def _parse(self, value: str, formatter: Format) -> typing.Any:
        pass

    @staticmethod
    def CurrencyValidator1() -> CurrencyValidator:
        pass

    def __init__(self, strict: bool, allowFractions: bool) -> None:
        pass

    @staticmethod
    def getInstance() -> BigDecimalValidator:
        pass

    # Class Methods End
