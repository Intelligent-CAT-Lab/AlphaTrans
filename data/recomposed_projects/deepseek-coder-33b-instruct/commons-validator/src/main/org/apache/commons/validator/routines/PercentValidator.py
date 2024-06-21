from __future__ import annotations
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

    __VALIDATOR: PercentValidator = PercentValidator.PercentValidator1()

    __serialVersionUID: int = -3508241924961535772

    def _parse(
        self, value: str, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        parsed_value = super()._parse(value, formatter)
        if parsed_value is not None or not isinstance(formatter, DecimalFormat):
            return parsed_value

        decimal_format = formatter
        pattern = decimal_format.to_pattern()
        if pattern.find(self.__PERCENT_SYMBOL) >= 0:
            buffer = []
            for i in range(len(pattern)):
                if pattern[i] != self.__PERCENT_SYMBOL:
                    buffer.append(pattern[i])
            decimal_format.apply_pattern("".join(buffer))
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

        if not hasattr(PercentValidator, "__VALIDATOR"):
            PercentValidator.__VALIDATOR = BigDecimalValidator()

        return PercentValidator.__VALIDATOR
