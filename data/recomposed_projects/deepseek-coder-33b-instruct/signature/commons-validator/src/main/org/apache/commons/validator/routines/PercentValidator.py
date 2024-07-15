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

        parsed_value = super()._parse(value, formatter)
        if parsed_value is not None or not isinstance(formatter, str):
            return parsed_value

        decimal_format = str(formatter)
        if self.__PERCENT_SYMBOL in decimal_format:
            buffer = []
            for char in decimal_format:
                if char != self.__PERCENT_SYMBOL:
                    buffer.append(char)
            decimal_format = "".join(buffer)
            parsed_value = super()._parse(value, decimal_format)

            if parsed_value is not None:
                parsed_value = parsed_value * self.__POINT_ZERO_ONE

        return parsed_value

    @staticmethod
    def PercentValidator1() -> PercentValidator:
        return PercentValidator(True)

    def __init__(self, strict: bool) -> None:
        super().__init__(strict, PERCENT_FORMAT, True)

    @staticmethod
    def getInstance() -> BigDecimalValidator:
        return PercentValidator.__VALIDATOR


PercentValidator.initialize_fields()
