from __future__ import annotations
import time
import re
import numbers
import io
import typing
from typing import *
import decimal
import datetime
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

    def _parse(
        self, value: str, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:
        parsedValue = super()._parse(value, formatter)
        if parsedValue is not None or not isinstance(formatter, datetime.datetime):
            return parsedValue

        pattern = formatter.toPattern()
        if pattern.find(self.__PERCENT_SYMBOL) >= 0:
            buffer = ""
            for i in range(len(pattern)):
                if pattern[i] != self.__PERCENT_SYMBOL:
                    buffer += pattern[i]
            formatter.applyPattern(buffer)
            parsedValue = super()._parse(value, formatter)

            if parsedValue is not None:
                parsedValue = parsedValue * self.__POINT_ZERO_ONE
        return parsedValue

    @staticmethod
    def PercentValidator1() -> PercentValidator:
        return PercentValidator(True)

    def __init__(self, strict: bool) -> None:
        super().__init__(strict, self.PERCENT_FORMAT, True)

    @staticmethod
    def getInstance() -> BigDecimalValidator:
        return PercentValidator.__VALIDATOR


PercentValidator.initialize_fields()
