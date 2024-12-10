from __future__ import annotations
import re
import numbers
import io
import typing
from typing import *
import decimal
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *


class PercentValidator(BigDecimalValidator):

    __POINT_ZERO_ONE: decimal.Decimal = decimal.Decimal("0.01")
    __PERCENT_SYMBOL: str = "%"
    __VALIDATOR: PercentValidator = None
    __serialVersionUID: int = -3508241924961535772

    @staticmethod
    def initialize_fields() -> None:
        PercentValidator.__VALIDATOR: PercentValidator = (
            PercentValidator.PercentValidator1()
        )

    @staticmethod
    def PercentValidator1() -> PercentValidator:
        return PercentValidator(True)

    def __init__(self, strict: bool) -> None:
        super().__init__(strict, self.PERCENT_FORMAT, True)

    @staticmethod
    def getInstance() -> BigDecimalValidator:
        return PercentValidator.__VALIDATOR


PercentValidator.initialize_fields()
