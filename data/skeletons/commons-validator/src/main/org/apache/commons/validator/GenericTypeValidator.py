from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.GenericValidator import *

# from src.main.org.apache.commons.logging.LogFactory import *
# from src.main.org.apache.commons.logging.Log import *
import logging
import datetime
import typing
from typing import *
import io

# Imports End


class GenericTypeValidator:

    # Class Fields Begin
    __serialVersionUID: int = None
    __LOG: logging.Logger = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def formatCreditCard(value: str) -> int:
        pass

    @staticmethod
    def formatDate1(
        value: str, datePattern: str, strict: bool
    ) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    @staticmethod
    def formatDate0(
        value: str, locale: typing.Any
    ) -> typing.Union[datetime.datetime, datetime.date]:
        pass

    @staticmethod
    def formatDouble1(value: str, locale: typing.Any) -> float:
        pass

    @staticmethod
    def formatDouble0(value: str) -> float:
        pass

    @staticmethod
    def formatFloat1(value: str, locale: typing.Any) -> float:
        pass

    @staticmethod
    def formatFloat0(value: str) -> float:
        pass

    @staticmethod
    def formatLong1(value: str, locale: typing.Any) -> int:
        pass

    @staticmethod
    def formatLong0(value: str) -> int:
        pass

    @staticmethod
    def formatInt1(value: str, locale: typing.Any) -> int:
        pass

    @staticmethod
    def formatInt0(value: str) -> int:
        pass

    @staticmethod
    def formatShort1(value: str, locale: typing.Any) -> int:
        pass

    @staticmethod
    def formatShort0(value: str) -> int:
        pass

    @staticmethod
    def formatByte1(value: str, locale: typing.Any) -> int:
        pass

    @staticmethod
    def formatByte0(value: str) -> int:
        pass

    # Class Methods End
