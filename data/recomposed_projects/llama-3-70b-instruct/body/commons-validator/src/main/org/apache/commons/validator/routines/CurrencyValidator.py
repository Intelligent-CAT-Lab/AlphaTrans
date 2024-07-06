from __future__ import annotations
import time
import re
import decimal
import numbers
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
from src.main.org.apache.commons.validator.routines.BigDecimalValidator import *


class CurrencyValidator(BigDecimalValidator):

    __CURRENCY_SYMBOL: str = "\u00A4"
    __VALIDATOR: CurrencyValidator = None
    __serialVersionUID: int = -4201640771171486514

    @staticmethod
    def initialize_fields() -> None:
        CurrencyValidator.__VALIDATOR: CurrencyValidator = (
            CurrencyValidator.CurrencyValidator1()
        )

    def _parse(
        self, value: str, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:
        parsedValue = super()._parse(value, formatter)
        if parsedValue is not None or not isinstance(
            formatter, AbstractFormatValidator
        ):
            return parsedValue

        decimalFormat = formatter
        pattern = decimalFormat.toPattern()
        if pattern.find(CurrencyValidator.__CURRENCY_SYMBOL) >= 0:
            buffer = []
            for i in range(len(pattern)):
                if pattern[i] != CurrencyValidator.__CURRENCY_SYMBOL:
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
        return CurrencyValidator.__VALIDATOR


CurrencyValidator.initialize_fields()
