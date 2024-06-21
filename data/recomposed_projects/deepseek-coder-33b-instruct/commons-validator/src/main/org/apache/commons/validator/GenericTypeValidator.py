from __future__ import annotations
import sys
import io
import typing
from typing import *
import datetime
from src.main.org.apache.commons.logging.Log import *
from src.main.org.apache.commons.logging.LogFactory import *
from src.main.org.apache.commons.validator.GenericValidator import *


class GenericTypeValidator:

    __LOG: logging.Logger = LogFactory.getLog(GenericTypeValidator.__class__)

    __serialVersionUID: int = 5487162314134261703

    @staticmethod
    def formatCreditCard(value: str) -> int:

        if GenericValidator.isCreditCard(value):
            return int(value)
        else:
            return None

    @staticmethod
    def formatDate1(
        value: str, datePattern: str, strict: bool
    ) -> typing.Union[datetime.date, datetime.datetime]:

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
                    "Date parse failed value=["
                    + value
                    + "], "
                    + "pattern=["
                    + datePattern
                    + "], "
                    + "strict=["
                    + str(strict)
                    + "] "
                    + str(e)
                )

        return date

    @staticmethod
    def formatDate0(
        value: str, locale: typing.Any
    ) -> typing.Union[datetime.date, datetime.datetime]:

        date = None

        if value is None:
            return None

        try:
            formatterShort = None
            formatterDefault = None
            if locale is not None:
                formatterShort = dateutil.parser.parse(
                    value, dayfirst=True, fuzzy=False, locale=locale
                )
                formatterDefault = dateutil.parser.parse(
                    value, dayfirst=True, fuzzy=False, locale=locale
                )
            else:
                formatterShort = dateutil.parser.parse(
                    value, dayfirst=True, fuzzy=False
                )
                formatterDefault = dateutil.parser.parse(
                    value, dayfirst=True, fuzzy=False
                )

            try:
                date = formatterShort
            except ValueError:
                date = formatterDefault
        except ValueError as e:
            if GenericTypeValidator.__LOG.isEnabledFor(logging.DEBUG):
                GenericTypeValidator.__LOG.debug(
                    "Date parse failed value=[{0}], locale=[{1}] {2}".format(
                        value, locale, e
                    )
                )

        return date

    @staticmethod
    def formatDouble1(value: str, locale: typing.Any) -> float:

        result = None

        if value is not None:
            formatter = None
            if locale is not None:
                formatter = locale.get_number_system()
            else:
                formatter = locale.get_default()

            pos = formatter.parse(value)

            if (
                pos.error_index == -1
                and pos.index == len(value)
                and pos.value >= (float("-inf"))
                and pos.value <= float("inf")
            ):
                result = float(pos.value)

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
                formatter = locale.get_number_system()
            else:
                formatter = locale.get_default()

            pos = formatter.parse(value)

            if (
                pos.error_index == -1
                and pos.index == len(value)
                and pos.number >= (float("-inf"))
                and pos.number <= float("inf")
            ):
                result = float(pos.number)

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
                and num.doubleValue() >= Long.MIN_VALUE
                and num.doubleValue() <= Long.MAX_VALUE
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
                and num.doubleValue() >= Integer.MIN_VALUE
                and num.doubleValue() <= Integer.MAX_VALUE
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
                and num.doubleValue() >= Short.MIN_VALUE
                and num.doubleValue() <= Short.MAX_VALUE
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
                and num.doubleValue() >= Byte.MIN_VALUE
                and num.doubleValue() <= Byte.MAX_VALUE
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
