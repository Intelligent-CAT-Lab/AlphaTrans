from __future__ import annotations
import re
import os
from abc import ABC
import io
import typing
from typing import *
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.RenameHandler import *


class JDKStringConverter(TypedStringConverter):

    CALENDAR: JDKStringConverter = None
    DATE: JDKStringConverter = None
    FILE: JDKStringConverter = None

    INET_ADDRESS: JDKStringConverter = None

    URI: JDKStringConverter = None

    URL: JDKStringConverter = None

    UUID: JDKStringConverter = None

    TIME_ZONE: JDKStringConverter = None

    CURRENCY: JDKStringConverter = None

    PACKAGE: JDKStringConverter = None

    CLASS: JDKStringConverter = None

    LOCALE: JDKStringConverter = None
    ATOMIC_BOOLEAN: JDKStringConverter = None

    ATOMIC_INTEGER: JDKStringConverter = None
    ATOMIC_LONG: JDKStringConverter = None
    BIG_DECIMAL: JDKStringConverter = None

    BIG_INTEGER: JDKStringConverter = None

    FLOAT: JDKStringConverter = None

    DOUBLE: JDKStringConverter = None

    BOOLEAN: JDKStringConverter = None

    CHAR_ARRAY: JDKStringConverter = None

    CHARACTER: JDKStringConverter = None
    BYTE_ARRAY: JDKStringConverter = None

    BYTE: JDKStringConverter = None

    SHORT: JDKStringConverter = None

    INTEGER: JDKStringConverter = None

    LONG: JDKStringConverter = None

    STRING_BUILDER: JDKStringConverter = None

    STRING_BUFFER: JDKStringConverter = None

    CHAR_SEQUENCE: JDKStringConverter = None

    STRING: JDKStringConverter = None

    __MASK_6BIT: int = 0x3F
    __MASK_8BIT: int = 0xFF
    __base64Array: List[str] = list(base64Str)
    __base64Str: str = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    )
    __type: typing.Type[typing.Any] = None

    @staticmethod
    def initialize_fields() -> None:
        JDKStringConverter.CALENDAR: JDKStringConverter = JDKStringConverter(
            lambda object: self.convertToString(object),
            lambda cls, str: self.convertFromString(cls, str),
        )

        JDKStringConverter.DATE: JDKStringConverter = JDKStringConverter(Date)

        JDKStringConverter.LOCALE: JDKStringConverter = JDKStringConverter(
            cls=Locale, convert_from_string=lambda cls, str: cls(*str.split("_", 2))
        )

        JDKStringConverter.ATOMIC_LONG: JDKStringConverter = JDKStringConverter(
            AtomicLong
        )

        JDKStringConverter.CHARACTER: JDKStringConverter = JDKStringConverter(Character)

    def convertToString(self, object: typing.Any) -> str:
        return str(object)

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return self.__type

    @staticmethod
    def __parseBase64Binary(str: str) -> typing.List[int]:

        MASK_6BIT = 0x3F
        MASK_8BIT = 0xFF
        base64Str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

        if len(str) % 4 != 0:
            raise ValueError("Invalid Base64 string")
        parsedLen = (len(str) * 3) // 4
        decoded = [0] * parsedLen
        inChars = list(str)
        pos = 0
        for i in range(0, len(inChars), 4):
            bits = (
                (base64Str.index(inChars[i]) & MASK_6BIT) << 18
                | (base64Str.index(inChars[i + 1]) & MASK_6BIT) << 12
                | (base64Str.index(inChars[i + 2]) & MASK_6BIT) << 6
                | (base64Str.index(inChars[i + 3]) & MASK_6BIT)
            )
            decoded[pos] = (bits >> 16) & MASK_8BIT
            decoded[pos + 1] = (bits >> 8) & MASK_8BIT
            decoded[pos + 2] = bits & MASK_8BIT
            pos += 3
        if str.endswith("=="):
            return decoded[:-2]
        elif str.endswith("="):
            return decoded[:-1]
        return decoded

    @staticmethod
    def __printBase64Binary(array: typing.List[int]) -> str:

        len_ = len(array)
        buf = [""] * (((len_ + 2) // 3) * 4)
        pos = 0
        for i in range(0, len_, 3):
            remaining = len_ - i
            if remaining >= 3:
                bits = (
                    (array[i] & JDKStringConverter.__MASK_8BIT) << 16
                    | (array[i + 1] & JDKStringConverter.__MASK_8BIT) << 8
                    | (array[i + 2] & JDKStringConverter.__MASK_8BIT)
                )
                buf[pos] = JDKStringConverter.__base64Array[
                    (bits >> 18) & JDKStringConverter.__MASK_6BIT
                ]
                pos += 1
                buf[pos] = JDKStringConverter.__base64Array[
                    (bits >> 12) & JDKStringConverter.__MASK_6BIT
                ]
                pos += 1
                buf[pos] = JDKStringConverter.__base64Array[
                    (bits >> 6) & JDKStringConverter.__MASK_6BIT
                ]
                pos += 1
                buf[pos] = JDKStringConverter.__base64Array[
                    bits & JDKStringConverter.__MASK_6BIT
                ]
                pos += 1
            elif remaining == 2:
                bits = (array[i] & JDKStringConverter.__MASK_8BIT) << 16 | (
                    array[i + 1] & JDKStringConverter.__MASK_8BIT
                ) << 8
                buf[pos] = JDKStringConverter.__base64Array[
                    (bits >> 18) & JDKStringConverter.__MASK_6BIT
                ]
                pos += 1
                buf[pos] = JDKStringConverter.__base64Array[
                    (bits >> 12) & JDKStringConverter.__MASK_6BIT
                ]
                pos += 1
                buf[pos] = JDKStringConverter.__base64Array[
                    (bits >> 6) & JDKStringConverter.__MASK_6BIT
                ]
                pos += 1
                buf[pos] = "="
                pos += 1
            else:
                bits = (array[i] & JDKStringConverter.__MASK_8BIT) << 16
                buf[pos] = JDKStringConverter.__base64Array[
                    (bits >> 18) & JDKStringConverter.__MASK_6BIT
                ]
                pos += 1
                buf[pos] = JDKStringConverter.__base64Array[
                    (bits >> 12) & JDKStringConverter.__MASK_6BIT
                ]
                pos += 1
                buf[pos] = "="
                pos += 1
                buf[pos] = "="
                pos += 1
        return "".join(buf)

    def __init__(self, type: typing.Type[typing.Any]) -> None:
        self.__type = type

    def getType(self) -> typing.Type[typing.Any]:
        return self.__type


JDKStringConverter.initialize_fields()
