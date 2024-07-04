from __future__ import annotations
import time
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
    __base64Array: typing.List[str] = list(base64Str)
    __base64Str: str = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    )
    __type: typing.Type[typing.Any] = None

    @staticmethod
    def initialize_fields() -> None:
        JDKStringConverter.CALENDAR: JDKStringConverter = JDKStringConverter(Calendar)

        JDKStringConverter.DATE: JDKStringConverter = JDKStringConverter(Date)

        JDKStringConverter.LOCALE: JDKStringConverter = JDKStringConverter(Locale)

        JDKStringConverter.ATOMIC_INTEGER: JDKStringConverter = JDKStringConverter(
            AtomicInteger
        )

        JDKStringConverter.ATOMIC_LONG: JDKStringConverter = JDKStringConverter(
            AtomicLong
        )

        JDKStringConverter.CHARACTER: JDKStringConverter = JDKStringConverter(Character)

    def convertToString(self, object: typing.Any) -> str:

        if isinstance(object, Calendar):
            if not isinstance(object, GregorianCalendar):
                raise RuntimeError(
                    "Unable to convert calendar as it is not a GregorianCalendar"
                )
            cal = typing.cast(GregorianCalendar, object)
            f = SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSZ")
            f.setCalendar(cal)
            str_val = f.format(cal.getTime())
            return (
                str_val[:26]
                + ":"
                + str_val[26:]
                + "["
                + cal.getTimeZone().getID()
                + "]"
            )

        elif isinstance(object, Date):
            f = SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSZ")
            str_val = f.format(object)
            return str_val[:26] + ":" + str_val[26:]

        elif isinstance(object, File):
            return str(object)

        elif isinstance(object, InetAddress):
            return object.getHostAddress()

        elif isinstance(object, URI):
            return str(object)

        elif isinstance(object, URL):
            return str(object)

        elif isinstance(object, UUID):
            return str(object)

        elif isinstance(object, TimeZone):
            return object.getID()

        elif isinstance(object, Currency):
            return str(object)

        elif isinstance(object, Package):
            return object.getName()

        elif isinstance(object, Class):
            return object.__name__

        elif isinstance(object, Locale):
            return str(object)

        elif isinstance(object, AtomicBoolean):
            return str(object.get())

        elif isinstance(object, AtomicInteger):
            return str(object.get())

        elif isinstance(object, AtomicLong):
            return str(object.get())

        elif isinstance(object, BigDecimal):
            return str(object)

        elif isinstance(object, BigInteger):
            return str(object)

        elif isinstance(object, float):
            return str(object)

        elif isinstance(object, (int, float)):
            return str(object)

        elif isinstance(object, bool):
            return str(object)

        elif isinstance(object, (list, tuple)):
            return "".join(object)

        elif isinstance(object, bytes):
            return "".join(chr(i & 0xFF) for i in object)

        elif isinstance(object, (int, float)):
            return str(object)

        elif isinstance(object, str):
            return object

        elif isinstance(object, StringBuilder):
            return str(object)

        elif isinstance(object, StringBuffer):
            return str(object)

        elif isinstance(object, CharSequence):
            return str(object)

        elif isinstance(object, str):
            return object

        else:
            return object.toString()

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        return self.__type

    @staticmethod
    def __parseBase64Binary(str: str) -> typing.List[int]:

        if len(str) % 4 != 0:
            raise ValueError("Invalid Base64 string")

        parsedLen = (len(str) * 3) // 4
        decoded = [0] * parsedLen
        inChars = list(str)
        pos = 0

        for i in range(0, len(inChars), 4):
            bits = (
                (
                    JDKStringConverter.__base64Str.index(inChars[i])
                    & JDKStringConverter.__MASK_6BIT
                )
                << 18
                | (
                    JDKStringConverter.__base64Str.index(inChars[i + 1])
                    & JDKStringConverter.__MASK_6BIT
                )
                << 12
                | (
                    JDKStringConverter.__base64Str.index(inChars[i + 2])
                    & JDKStringConverter.__MASK_6BIT
                )
                << 6
                | (
                    JDKStringConverter.__base64Str.index(inChars[i + 3])
                    & JDKStringConverter.__MASK_6BIT
                )
            )

            decoded[pos] = (bits >> 16) & JDKStringConverter.__MASK_8BIT
            pos += 1
            decoded[pos] = (bits >> 8) & JDKStringConverter.__MASK_8BIT
            pos += 1
            decoded[pos] = bits & JDKStringConverter.__MASK_8BIT
            pos += 1

        if str.endswith("=="):
            return decoded[:-2]
        elif str.endswith("="):
            return decoded[:-1]

        return decoded

    @staticmethod
    def __printBase64Binary(array: typing.List[int]) -> str:

        len_array = len(array)
        buf = [""] * (((len_array + 2) // 3) * 4)
        pos = 0
        for i in range(0, len_array, 3):
            remaining = len_array - i
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

    def convertToString(self, object: typing.Any) -> str:
        pass

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        pass

    def parseBase64Binary(self, str: str) -> bytearray:
        pass

    def printBase64Binary(self, byteArray: bytearray) -> str:
        pass

    def getType(self) -> typing.Type[typing.Any]:
        return self.__type


JDKStringConverter.initialize_fields()
