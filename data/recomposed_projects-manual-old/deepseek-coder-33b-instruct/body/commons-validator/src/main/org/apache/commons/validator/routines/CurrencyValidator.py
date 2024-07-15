from __future__ import annotations
import time
import re
import os
import numbers
from io import StringIO
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

        pos = io.StringIO(value).tell()
        parsedValue = formatter.parseObject(value, pos)
        if parsedValue.getErrorIndex() > -1:
            return None

        if self.isStrict() and pos.getIndex() < len(value):
            return None

        if parsedValue is not None:
            parsedValue = self._processParsedValue(parsedValue, formatter)

        return parsedValue

    @staticmethod
    def CurrencyValidator1() -> CurrencyValidator:
        return CurrencyValidator(True, True)

    def __init__(self, strict: bool, allowFractions: bool) -> None:
        super().__init__(
            strict, AbstractNumberValidator.CURRENCY_FORMAT, allowFractions
        )

    @staticmethod
    def getInstance() -> BigDecimalValidator:
        return CurrencyValidator.__VALIDATOR


CurrencyValidator.initialize_fields()
