from __future__ import annotations

# Imports Begin
from src.main.org.joda.convert.RenameHandler import *
from src.main.org.joda.convert.TypedStringConverter import *
import typing
from typing import *
import io

# Imports End


class JDKStringConverter(TypedStringConverter):

    # Class Fields Begin
    BYTE_ARRAY: JDKStringConverter = None
    CHARACTER: JDKStringConverter = None
    CHAR_ARRAY: JDKStringConverter = None
    BOOLEAN: JDKStringConverter = None
    DOUBLE: JDKStringConverter = None
    FLOAT: JDKStringConverter = None
    BIG_INTEGER: JDKStringConverter = None
    BIG_DECIMAL: JDKStringConverter = None
    ATOMIC_LONG: JDKStringConverter = None
    ATOMIC_INTEGER: JDKStringConverter = None
    ATOMIC_BOOLEAN: JDKStringConverter = None
    LOCALE: JDKStringConverter = None
    CLASS: JDKStringConverter = None
    PACKAGE: JDKStringConverter = None
    CURRENCY: JDKStringConverter = None
    TIME_ZONE: JDKStringConverter = None
    UUID: JDKStringConverter = None
    URL: JDKStringConverter = None
    URI: JDKStringConverter = None
    INET_ADDRESS: JDKStringConverter = None
    FILE: JDKStringConverter = None
    DATE: JDKStringConverter = None
    CALENDAR: JDKStringConverter = None
    __type: typing.Type[typing.Any] = None
    __base64Str: str = None
    __base64Array: typing.List[str] = None
    __MASK_8BIT: int = None
    __MASK_6BIT: int = None
    STRING: JDKStringConverter = None
    CHAR_SEQUENCE: JDKStringConverter = None
    STRING_BUFFER: JDKStringConverter = None
    STRING_BUILDER: JDKStringConverter = None
    LONG: JDKStringConverter = None
    INTEGER: JDKStringConverter = None
    SHORT: JDKStringConverter = None
    BYTE: JDKStringConverter = None
    # Class Fields End

    # Class Methods Begin
    def convertToString(self, object: typing.Any) -> str:
        pass

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    @staticmethod
    def __parseBase64Binary(str: str) -> typing.List[int]:
        pass

    @staticmethod
    def __printBase64Binary(array: typing.List[int]) -> str:
        pass

    def __init__(self, type: typing.Type[typing.Any]) -> None:
        pass

    def getType(self) -> typing.Type[typing.Any]:
        pass

    # Class Methods End
