from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
import decimal
import typing
from typing import *
import io

# Imports End


class PercentValidator(BigDecimalValidator):

    # Class Fields Begin
    __serialVersionUID: int = None
    __VALIDATOR: PercentValidator = None
    __PERCENT_SYMBOL: str = None
    __POINT_ZERO_ONE: decimal.Decimal = None
    # Class Fields End

    # Class Methods Begin
    def _parse(self, value: str, formatter: Format) -> typing.Any:
        pass

    @staticmethod
    def PercentValidator1() -> PercentValidator:
        pass

    def __init__(self, strict: bool) -> None:
        pass

    @staticmethod
    def getInstance() -> BigDecimalValidator:
        pass

    # Class Methods End
