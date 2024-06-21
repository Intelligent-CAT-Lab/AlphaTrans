from __future__ import annotations
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *


class CurrencyValidator(BigDecimalValidator):

    __CURRENCY_SYMBOL: str = "\u00A4"

    __VALIDATOR: CurrencyValidator = CurrencyValidator.CurrencyValidator1()

    __serialVersionUID: int = -4201640771171486514

    def _parse(
        self, value: str, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:

        parsedValue = super()._parse(value, formatter)
        if parsedValue is not None or not isinstance(formatter, DecimalFormat):
            return parsedValue

        decimalFormat = formatter
        pattern = decimalFormat.toPattern()
        if pattern.find(self.__CURRENCY_SYMBOL) >= 0:
            buffer = []
            for i in range(len(pattern)):
                if pattern[i] != self.__CURRENCY_SYMBOL:
                    buffer.append(pattern[i])
            decimalFormat.applyPattern("".join(buffer))
            parsedValue = super()._parse(value, decimalFormat)
        return parsedValue

    @staticmethod
    def CurrencyValidator1() -> CurrencyValidator:

        return CurrencyValidator(True, True)

    def __init__(self, strict: bool, allowFractions: bool) -> None:

        super().__init__(strict, CURRENCY_FORMAT, allowFractions)

    @staticmethod
    def getInstance() -> BigDecimalValidator:

        if not hasattr(CurrencyValidator, "__VALIDATOR"):
            CurrencyValidator.__VALIDATOR = BigDecimalValidator()

        return CurrencyValidator.__VALIDATOR
