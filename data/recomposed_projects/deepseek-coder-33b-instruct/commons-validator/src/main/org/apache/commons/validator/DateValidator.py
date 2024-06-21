from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.validator.routines.AbstractCalendarValidator import *


class DateValidator:

    __DATE_VALIDATOR: DateValidator = DateValidator()

    def isValid1(self, value: str, locale: typing.Any) -> bool:

        if value is None:
            return False

        formatter = None
        if locale is not None:
            formatter = DateFormat.getDateInstance(DateFormat.SHORT, locale)
        else:
            formatter = DateFormat.getDateInstance(
                DateFormat.SHORT, Locale.getDefault()
            )

        formatter.setLenient(False)

        try:
            formatter.parse(value)
        except ParseException:
            return False

        return True

    def isValid0(self, value: str, datePattern: str, strict: bool) -> bool:

        if value is None or datePattern is None or len(datePattern) <= 0:
            return False

        try:
            datetime.datetime.strptime(value, datePattern)
        except ValueError:
            return False

        if strict and (len(datePattern) != len(value)):
            return False

        return True

    def __init__(self) -> None:

        super().__init__()

    @staticmethod
    def getInstance() -> DateValidator:

        if not hasattr(DateValidator, "__DATE_VALIDATOR"):
            DateValidator.__DATE_VALIDATOR = DateValidator()

        return DateValidator.__DATE_VALIDATOR
