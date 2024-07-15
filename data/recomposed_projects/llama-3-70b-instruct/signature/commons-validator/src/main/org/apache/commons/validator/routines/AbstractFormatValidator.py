from __future__ import annotations
import time
import locale
import re
import os
from io import StringIO
from abc import ABC
import io
import typing
from typing import *
import datetime


class AbstractFormatValidator(ABC):

    __strict: bool = False

    __serialVersionUID: int = -4690687565200568258

    def _parse(
        self, value: str, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:
        pos = io.StringIO(value)
        parsedValue = formatter.parseObject(value, pos)
        if pos.getErrorIndex() > -1:
            return None

        if self.isStrict() and pos.getIndex() < len(value):
            return None

        if parsedValue is not None:
            parsedValue = self._processParsedValue(parsedValue, formatter)

        return parsedValue

    def _format4(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> str:
        return formatter.format(value)

    def format3(self, value: typing.Any, pattern: str, locale: typing.Any) -> str:
        formatter = self._getFormat(pattern, locale)
        return self._format4(value, formatter)

    def format2(self, value: typing.Any, locale: typing.Any) -> str:
        return self.format3(value, None, locale)

    def format1(self, value: typing.Any, pattern: str) -> str:
        return self.format3(value, pattern, None)

    def format0(self, value: typing.Any) -> str:
        return self.format3(value, None, None)

    def isValid2(self, value: str, locale: typing.Any) -> bool:
        return self.isValid3(value, None, locale)

    def isValid1(self, value: str, pattern: str) -> bool:
        return self.isValid3(value, pattern, None)

    def isValid0(self, value: str) -> bool:
        return self.isValid3(value, None, None)

    def isStrict(self) -> bool:
        return self.__strict

    def __init__(self, strict: bool) -> None:
        self.__strict = strict

    def _getFormat(
        self, pattern: str, locale: typing.Any
    ) -> typing.Union[str, datetime.datetime]:
        return Format(pattern, locale)

    def _processParsedValue(
        self, value: typing.Any, formatter: typing.Union[str, datetime.datetime]
    ) -> typing.Any:
        return value

    def isValid3(self, value: str, pattern: str, locale: typing.Any) -> bool:
        return False
