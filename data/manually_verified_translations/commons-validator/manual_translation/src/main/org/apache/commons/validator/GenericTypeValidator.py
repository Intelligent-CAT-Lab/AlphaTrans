from __future__ import annotations
import time
import locale
import re
import sys
import os
import decimal
import numbers
import io
import typing
from typing import *
import datetime
import logging

# from src.main.org.apache.commons.logging.Log import *
# from src.main.org.apache.commons.logging.LogFactory import *
from src.main.org.apache.commons.validator.GenericValidator import *


class GenericTypeValidator:

    __LOG: logging.Logger = logging.getLogger(__name__)
    __serialVersionUID: int = 5487162314134261703

    @staticmethod
    def formatCreditCard(value: str) -> int:
        return int(value) if GenericValidator.isCreditCard(value) else None

    @staticmethod
    def formatDate1(
        value: str, datePattern: str, strict: bool
    ) -> typing.Union[datetime.datetime, datetime.date]:

        date = None

        if value is None or datePattern is None or len(datePattern) == 0:
            return None

        try:
            formatter = datetime.datetime.strptime(value, datePattern)

            if strict and len(datePattern) != len(value):
                date = None
            else:
                date = formatter
        except ValueError as e:
            if GenericTypeValidator.__LOG.isEnabledFor(logging.DEBUG):
                GenericTypeValidator.__LOG.debug(
                    "Date parse failed value=[{0}], pattern=[{1}], strict=[{2}] {3}".format(
                        value, datePattern, strict, e
                    )
                )

        return date

    @staticmethod
    def formatDate0(
        value: str, locale: typing.Any
    ) -> typing.Union[datetime.datetime, datetime.date]:

        date = None

        if value is None:
            return None

        try:
            formatterShort = None
            formatterDefault = None
            if locale is not None:
                formatterShort = DateFormat.getDateInstance(3, locale)
                formatterDefault = DateFormat.getDateInstance(
                    DateFormat.DEFAULT, locale
                )
            else:
                formatterShort = DateFormat.getDateInstance(3, Locale.getDefault())
                formatterDefault = DateFormat.getDateInstance(
                    DateFormat.DEFAULT, Locale.getDefault()
                )

            formatterShort.setLenient(False)
            formatterDefault.setLenient(False)

            try:
                date = formatterShort.parse(value)
            except ParseException:
                date = formatterDefault.parse(value)
        except ParseException:
            if GenericTypeValidator.__LOG.isDebugEnabled():
                GenericTypeValidator.__LOG.debug(
                    "Date parse failed value=["
                    + value
                    + "], "
                    + "locale=["
                    + locale
                    + "] "
                )

        return date

    @staticmethod
    def formatDouble1(value: str, locale: typing.Any) -> float:

        result = None

        if value is not None:
            formatter = None
            if locale is not None:
                formatter = locale.get_number_system().get_decimal_formatter()
            else:
                formatter = (
                    locale.get_default().get_number_system().get_decimal_formatter()
                )
            pos = formatter.parse(value)

            if (
                pos.error_index == -1
                and pos.index == len(value)
                and pos.double_value >= (float("-inf"))
                and pos.double_value <= float("inf")
            ):
                result = pos.double_value

        return result

    @staticmethod
    def formatDouble0(value: str) -> float:

        if value is None:
            return None

        try:
            return float(value)
        except ValueError:
            return None

    @staticmethod
    def formatFloat1(value: str, locale: typing.Any) -> float:

        result = None

        if value is not None:
            formatter = None
            if locale is not None:
                formatter = locale.get_number_system().get_decimal_formatter()
            else:
                formatter = (
                    locale.get_default().get_number_system().get_decimal_formatter()
                )
            num = formatter.parse(value)

            if (
                num is not None
                and num.floatValue() >= (float("-inf"))
                and num.floatValue() <= float("inf")
            ):
                result = num.floatValue()

        return result

    @staticmethod
    def formatFloat0(value: str) -> float:

        if value is None:
            return None

        try:
            return float(value)
        except ValueError:
            return None

    @staticmethod
    def formatLong1(value: str, locale: typing.Any) -> int:

        result = None

        if value is not None:
            formatter = None
            if locale is not None:
                formatter = NumberFormat.getNumberInstance(locale)
            else:
                formatter = NumberFormat.getNumberInstance(Locale.getDefault())
            formatter.setParseIntegerOnly(True)
            pos = ParsePosition(0)
            num = formatter.parse(value, pos)

            if (
                pos.getErrorIndex() == -1
                and pos.getIndex() == len(value)
                and num.doubleValue() >= -9223372036854775808
                and num.doubleValue() <= 9223372036854775807
            ):
                result = Long.valueOf(num.longValue())

        return result

    @staticmethod
    def formatLong0(value: str) -> int:

        if value is None:
            return None

        try:
            return int(value)
        except ValueError:
            return None

    @staticmethod
    def formatInt1(value: str, locale: typing.Any) -> int:

        result = None

        if value is not None:
            formatter = None
            if locale is not None:
                formatter = NumberFormat.getNumberInstance(locale)
            else:
                formatter = NumberFormat.getNumberInstance(Locale.getDefault())
            formatter.setParseIntegerOnly(True)
            pos = ParsePosition(0)
            num = formatter.parse(value, pos)

            if (
                pos.getErrorIndex() == -1
                and pos.getIndex() == len(value)
                and num.doubleValue() >= -2147483648
                and num.doubleValue() <= 2147483647
            ):
                result = Integer.valueOf(num.intValue())

        return result

    @staticmethod
    def formatInt0(value: str) -> int:

        if value is None:
            return None

        try:
            return int(value)
        except ValueError:
            return None

    @staticmethod
    def formatShort1(value: str, locale: typing.Any) -> int:

        result = None

        if value is not None:
            formatter = None
            if locale is not None:
                formatter = NumberFormat.getNumberInstance(locale)
            else:
                formatter = NumberFormat.getNumberInstance(Locale.getDefault())
            formatter.setParseIntegerOnly(True)
            pos = ParsePosition(0)
            num = formatter.parse(value, pos)

            if (
                pos.getErrorIndex() == -1
                and pos.getIndex() == len(value)
                and num.doubleValue() >= -32768
                and num.doubleValue() <= 32767
            ):
                result = Short.valueOf(num.shortValue())

        return result

    @staticmethod
    def formatShort0(value: str) -> int:

        if value is None:
            return None

        try:
            return int(value)
        except ValueError:
            return None

    @staticmethod
    def formatByte1(value: str, locale: typing.Any) -> int:

        result = None

        if value is not None:
            formatter = None
            if locale is not None:
                formatter = NumberFormat.getNumberInstance(locale)
            else:
                formatter = NumberFormat.getNumberInstance(Locale.getDefault())
            formatter.setParseIntegerOnly(True)
            pos = ParsePosition(0)
            num = formatter.parse(value, pos)

            if (
                pos.getErrorIndex() == -1
                and pos.getIndex() == len(value)
                and num.doubleValue() >= -128
                and num.doubleValue() <= 127
            ):
                result = Byte.valueOf(num.byteValue())

        return result

    @staticmethod
    def formatByte0(value: str) -> int:

        if value is None:
            return None

        try:
            return int(value)
        except ValueError:
            return None
