from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io
from abc import ABC

# Imports End


class AbstractFormatValidator(ABC):

    # Class Fields Begin
    __serialVersionUID: int = None
    __strict: bool = None
    # Class Fields End

    # Class Methods Begin
    def _parse(self, value: str, formatter: Format) -> typing.Any:
        pass

    def _format4(self, value: typing.Any, formatter: Format) -> str:
        pass

    def format3(self, value: typing.Any, pattern: str, locale: typing.Any) -> str:
        pass

    def format2(self, value: typing.Any, locale: typing.Any) -> str:
        pass

    def format1(self, value: typing.Any, pattern: str) -> str:
        pass

    def format0(self, value: typing.Any) -> str:
        pass

    def isValid2(self, value: str, locale: typing.Any) -> bool:
        pass

    def isValid1(self, value: str, pattern: str) -> bool:
        pass

    def isValid0(self, value: str) -> bool:
        pass

    def isStrict(self) -> bool:
        pass

    def __init__(self, strict: bool) -> None:
        pass

    def _getFormat(self, pattern: str, locale: typing.Any) -> Format:
        pass

    def _processParsedValue(self, value: typing.Any, formatter: Format) -> typing.Any:
        pass

    def isValid3(self, value: str, pattern: str, locale: typing.Any) -> bool:
        pass

    # Class Methods End
