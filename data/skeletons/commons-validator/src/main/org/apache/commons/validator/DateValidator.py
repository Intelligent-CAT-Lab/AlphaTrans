from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *
import typing
from typing import *
import io

# Imports End


class DateValidator:

    # Class Fields Begin
    __DATE_VALIDATOR: DateValidator = None
    # Class Fields End

    # Class Methods Begin
    def isValid1(self, value: str, locale: typing.Any) -> bool:
        pass

    def isValid0(self, value: str, datePattern: str, strict: bool) -> bool:
        pass

    def __init__(self) -> None:
        pass

    @staticmethod
    def getInstance() -> DateValidator:
        pass

    # Class Methods End
